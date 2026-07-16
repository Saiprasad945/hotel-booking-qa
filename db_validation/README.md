# Database Validation — Hotel Booking

SQL data-validation framework. Uses **SQLite** (zero-install, ships with Python)
so it runs anywhere; the SQL is standard and runs unchanged on **MySQL** in
production (see "MySQL equivalent" note below).

## What it does
1. Builds a relational hotel schema (rooms, guests, bookings, payments, messages) with foreign keys.
2. Loads **real room data from the live API** (`GET /api/room`) into the DB — the API↔DB load.
3. Runs a suite of validation checks and reports PASS/FAIL, exiting non-zero if any **integrity** check fails (CI-ready).

## Files
| File | Purpose |
|------|---------|
| `schema.sql` | Table definitions with FKs and CHECK constraints |
| `build_db.py` | Creates DB, loads live rooms, seeds guests/bookings/payments/messages |
| `validate.py` | Runs integrity + API↔DB + data-quality checks |
| `queries/validation_queries.sql` | The raw, documented SQL validation queries |

## How to run
```bash
source .venv/bin/activate          # from project root
python db_validation/build_db.py   # build + load from API
python db_validation/validate.py   # validate  (exit 0 = all integrity checks pass)
```
> Always run **build then validate together**. The AUT is a shared public server
> whose data changes frequently; building and validating in one flow keeps the
> API↔DB comparison consistent (see the lesson in the project README).

## Checks performed

**Integrity (gate the build):**
- All tables populated
- API↔DB room count matches
- API↔DB room data matches (type, price)
- Foreign-key integrity: no orphan bookings (room, guest) or payments
- `checkout > checkin` on every booking
- No overlapping bookings per room (double-booking)
- No NULL/empty required guest fields
- Valid guest email format
- No zero/negative room prices
- PAID payments have a positive amount

**Data-quality findings (reported, non-blocking):**
- Duplicate room numbers in the live dataset → see `docs/bug-reports.md` (BUG-01)

## MySQL equivalent
The schema uses SQLite syntax; for MySQL:
- `INTEGER PRIMARY KEY AUTOINCREMENT` → `INT AUTO_INCREMENT PRIMARY KEY`
- Connect with `mysql-connector-python` / `PyMySQL` instead of `sqlite3`
- All validation queries in `queries/validation_queries.sql` run **unchanged**.
