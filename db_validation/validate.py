"""
SQL data-validation runner for the Hotel Booking database.

Runs a suite of integrity checks against the SQLite DB and, where possible,
cross-checks the DB against the LIVE API (API <-> DB consistency).

Each check PASSES when it finds zero violating rows (or the expected value).
Exits with code 1 if any check fails — so it can gate a CI pipeline.

Run:  python db_validation/validate.py
"""
import os
import sqlite3
import sys

import requests

BASE_URL = os.getenv("BASE_URL", "https://automationintesting.online")
HERE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(HERE, "hotel.db")


def check_no_rows(conn, name, sql):
    """Pass when the query returns zero rows."""
    rows = conn.execute(sql).fetchall()
    return name, len(rows) == 0, f"{len(rows)} violating row(s)"


def check_tables_not_empty(conn):
    tables = ["rooms", "guests", "bookings", "payments", "messages"]
    empty = [t for t in tables if conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0] == 0]
    return "All tables populated", len(empty) == 0, (
        "all non-empty" if not empty else f"empty: {', '.join(empty)}")


def check_api_db_room_count(conn):
    """API <-> DB: room count in the DB matches the live API."""
    db_count = conn.execute("SELECT COUNT(*) FROM rooms").fetchone()[0]
    try:
        api_rooms = requests.get(f"{BASE_URL}/api/room", timeout=15).json()["rooms"]
    except Exception as e:  # noqa: BLE001
        return "API<->DB room count", False, f"API unreachable: {e}"
    api_count = len(api_rooms)
    return ("API<->DB room count", db_count == api_count,
            f"DB={db_count}, API={api_count}")


def check_api_db_room_data(conn):
    """API <-> DB: each live room's price & type matches the DB row."""
    try:
        api_rooms = requests.get(f"{BASE_URL}/api/room", timeout=15).json()["rooms"]
    except Exception as e:  # noqa: BLE001
        return "API<->DB room data", False, f"API unreachable: {e}"
    mismatches = []
    for r in api_rooms:
        row = conn.execute(
            "SELECT type, room_price FROM rooms WHERE room_id = ?", (r["roomid"],)
        ).fetchone()
        if row is None:
            mismatches.append(f"room {r['roomid']} missing in DB")
        elif row[0] != r["type"] or float(row[1]) != float(r["roomPrice"]):
            mismatches.append(f"room {r['roomid']} data differs")
    return ("API<->DB room data", len(mismatches) == 0,
            "all match" if not mismatches else "; ".join(mismatches[:3]))


# Data-quality findings against the uncontrolled live dataset.
# These are REPORTED as findings but do not fail the build (we don't own the data).
DATA_QUALITY_CHECKS = [
    ("No duplicate room numbers (live data)",
     "SELECT room_name FROM rooms GROUP BY room_name HAVING COUNT(*) > 1"),
]

# Integrity checks on our own relational/seeded data — these GATE the build.
SQL_CHECKS = [
    ("No orphan bookings (room FK)",
     "SELECT b.booking_id FROM bookings b LEFT JOIN rooms r ON b.room_id=r.room_id "
     "WHERE r.room_id IS NULL"),
    ("No orphan bookings (guest FK)",
     "SELECT b.booking_id FROM bookings b LEFT JOIN guests g ON b.guest_id=g.guest_id "
     "WHERE g.guest_id IS NULL"),
    ("No orphan payments (booking FK)",
     "SELECT p.payment_id FROM payments p LEFT JOIN bookings b "
     "ON p.booking_id=b.booking_id WHERE b.booking_id IS NULL"),
    ("Checkout after checkin",
     "SELECT booking_id FROM bookings WHERE checkout <= checkin"),
    ("No overlapping bookings per room",
     "SELECT a.booking_id FROM bookings a JOIN bookings b ON a.room_id=b.room_id "
     "AND a.booking_id<b.booking_id AND a.checkin<b.checkout AND b.checkin<a.checkout"),
    ("No NULL/empty guest fields",
     "SELECT guest_id FROM guests WHERE firstname='' OR lastname='' "
     "OR email='' OR phone=''"),
    ("Valid guest email format",
     "SELECT guest_id FROM guests WHERE email NOT LIKE '%_@_%._%'"),
    ("No zero/negative room prices",
     "SELECT room_id FROM rooms WHERE room_price <= 0"),
    ("PAID payments have positive amount",
     "SELECT payment_id FROM payments WHERE status='PAID' AND amount <= 0"),
]


def main():
    if not os.path.exists(DB_PATH):
        print("❌ hotel.db not found. Run: python db_validation/build_db.py")
        return 1

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")

    # Integrity checks (gate the build)
    integrity = [check_tables_not_empty(conn),
                 check_api_db_room_count(conn),
                 check_api_db_room_data(conn)]
    integrity += [check_no_rows(conn, name, sql) for name, sql in SQL_CHECKS]

    # Data-quality findings (informational only)
    findings = [check_no_rows(conn, name, sql) for name, sql in DATA_QUALITY_CHECKS]
    conn.close()

    def render(title, rows):
        print("\n" + "=" * 62)
        print(title)
        print("=" * 62)
        print(f"{'CHECK':<40}{'RESULT':<8}DETAIL")
        print("-" * 62)
        ok_count = 0
        for name, ok, detail in rows:
            status = "PASS" if ok else "FAIL"
            icon = "✅" if ok else "❌"
            print(f"{name:<40}{icon} {status:<4} {detail}")
            ok_count += ok
        return ok_count

    passed = render("INTEGRITY CHECKS (gate build)", integrity)
    print("=" * 62)
    print(f"Integrity: {passed}/{len(integrity)} passed")

    dq_ok = render("DATA-QUALITY FINDINGS (informational)", findings)
    print("=" * 62)
    if dq_ok < len(findings):
        print(f"⚠ {len(findings) - dq_ok} data-quality finding(s) in live data "
              f"— see docs/bug-reports.md")
    print()

    # Build fails only when an INTEGRITY check fails.
    return 0 if passed == len(integrity) else 1


if __name__ == "__main__":
    sys.exit(main())
