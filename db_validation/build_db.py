"""
Build the hotel booking SQLite database.

- Creates the schema from schema.sql
- Loads REAL room data from the live API (GET /api/room)
- Seeds guests, bookings, payments and messages

Run:  python db_validation/build_db.py
"""
import os
import sqlite3
import sys

import requests

BASE_URL = os.getenv("BASE_URL", "https://automationintesting.online")
HERE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(HERE, "hotel.db")
SCHEMA_PATH = os.path.join(HERE, "schema.sql")


def create_schema(conn):
    with open(SCHEMA_PATH) as f:
        conn.executescript(f.read())
    print("✔ Schema created")


def load_rooms_from_api(conn):
    """Fetch live rooms and insert them — this is the API -> DB load."""
    try:
        resp = requests.get(f"{BASE_URL}/api/room", timeout=15)
        resp.raise_for_status()
        rooms = resp.json().get("rooms", [])
    except requests.RequestException as e:
        print(f"⚠ Could not reach API ({e}); falling back to sample rooms")
        rooms = [
            {"roomid": 1, "roomName": "101", "type": "Single", "accessible": True,
             "roomPrice": 100, "description": "Sample room"},
            {"roomid": 2, "roomName": "102", "type": "Double", "accessible": True,
             "roomPrice": 150, "description": "Sample room"},
        ]

    for r in rooms:
        conn.execute(
            "INSERT OR REPLACE INTO rooms "
            "(room_id, room_name, type, accessible, room_price, description) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (r["roomid"], r["roomName"], r["type"], int(bool(r["accessible"])),
             r["roomPrice"], r.get("description", "")),
        )
    print(f"✔ Loaded {len(rooms)} rooms from API")
    return rooms


def seed_guests(conn):
    guests = [
        ("Sai", "Kumar", "sai.kumar@example.com", "01234567890"),
        ("Priya", "Sharma", "priya.sharma@example.com", "01234567891"),
        ("John", "Smith", "john.smith@example.com", "01234567892"),
        ("Aisha", "Khan", "aisha.khan@example.com", "01234567893"),
    ]
    conn.executemany(
        "INSERT INTO guests (firstname, lastname, email, phone) VALUES (?, ?, ?, ?)",
        guests,
    )
    print(f"✔ Seeded {len(guests)} guests")


def seed_bookings(conn, room_ids):
    r1 = room_ids[0]
    r2 = room_ids[1] if len(room_ids) > 1 else room_ids[0]
    bookings = [
        (r1, 1, "2026-08-01", "2026-08-05", 1),
        (r2, 2, "2026-08-03", "2026-08-06", 1),
        (r1, 3, "2026-09-10", "2026-09-12", 0),
        (r2, 4, "2026-09-15", "2026-09-20", 1),
    ]
    conn.executemany(
        "INSERT INTO bookings (room_id, guest_id, checkin, checkout, deposit_paid) "
        "VALUES (?, ?, ?, ?, ?)",
        bookings,
    )
    print(f"✔ Seeded {len(bookings)} bookings")


def seed_payments(conn):
    payments = [
        (1, 400.0, "PAID"),
        (2, 450.0, "PAID"),
        (3, 200.0, "PENDING"),
        (4, 750.0, "PAID"),
    ]
    conn.executemany(
        "INSERT INTO payments (booking_id, amount, status) VALUES (?, ?, ?)",
        payments,
    )
    print(f"✔ Seeded {len(payments)} payments")


def seed_messages(conn):
    messages = [
        ("Sai Kumar", "sai.kumar@example.com", "01234567890",
         "Late checkout", "Is a late checkout possible for my booking? Thanks."),
        ("Priya Sharma", "priya.sharma@example.com", "01234567891",
         "Parking query", "Do you have on-site parking available for guests?"),
    ]
    conn.executemany(
        "INSERT INTO messages (name, email, phone, subject, description) "
        "VALUES (?, ?, ?, ?, ?)",
        messages,
    )
    print(f"✔ Seeded {len(messages)} messages")


def main():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        create_schema(conn)
        rooms = load_rooms_from_api(conn)
        room_ids = [r["roomid"] for r in rooms] or [1, 2]
        seed_guests(conn)
        seed_bookings(conn, room_ids)
        seed_payments(conn)
        seed_messages(conn)
        conn.commit()
    finally:
        conn.close()
    print(f"\n✅ Database built at {DB_PATH}")


if __name__ == "__main__":
    sys.exit(main())
