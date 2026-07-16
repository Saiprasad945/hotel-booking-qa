# Defect Reports — Hotel Booking Application

Defects follow the lifecycle defined in `test-plan.md` §10.
Format: ID · Summary · Module · Severity · Priority · Status · Steps · Expected vs Actual · Evidence.

---

## BUG-01 — Duplicate room numbers exist in the room dataset

| Field | Value |
|-------|-------|
| **ID** | BUG-01 |
| **Module** | Rooms / Data integrity |
| **Severity** | Major |
| **Priority** | P2 |
| **Status** | OPEN |
| **Environment** | https://automationintesting.online (live API), SQLite validation DB |
| **Found by** | SQL data-validation suite (`db_validation/validate.py`) |
| **Related TC** | TC-057 |

**Steps to reproduce**
1. `GET /api/room` and load the response into the `rooms` table.
2. Run: `SELECT room_name, COUNT(*) FROM rooms GROUP BY room_name HAVING COUNT(*) > 1;`

**Expected:** Room numbers (`room_name`) are unique — a hotel cannot have two
different physical rooms with the same number.

**Actual:** The same room number (e.g. `"101"`) appears multiple times with
different `type` and `roomid` values, indicating no uniqueness constraint on
room number.

**Impact:** Guests and admins cannot reliably identify a room by its number;
reporting and availability logic keyed on room number would be ambiguous.

**Recommendation:** Add a UNIQUE constraint on `room_name` (or validate
uniqueness on room creation, ref REQ-22).

---

## BUG-02 — Inconsistent HTTP status for invalid booking date range

| Field | Value |
|-------|-------|
| **ID** | BUG-02 |
| **Module** | Booking API |
| **Severity** | Minor |
| **Priority** | P3 |
| **Status** | OPEN |
| **Environment** | https://automationintesting.online (live API) |
| **Found by** | Postman/Newman API run (Sprint 3) |
| **Related TC** | TC-094 |

**Steps to reproduce**
1. `POST /api/booking` with `checkin` later than `checkout`.

**Expected:** A `400 Bad Request` for client-side validation failure (invalid input).

**Actual:** The API returns `409 Conflict`.

**Impact:** `409` semantically means a resource conflict (e.g. double-booking),
not invalid input. Clients relying on status codes to distinguish validation
errors from conflicts may misclassify the error.

**Recommendation:** Return `400` for malformed date ranges; reserve `409` for
genuine availability conflicts.

---

## Bug metrics (running)

| Severity | Count |
|----------|------:|
| Blocker | 0 |
| Critical | 0 |
| Major | 1 |
| Minor | 1 |
| **Total** | **2** |

_More defects to be added during UI automation (Sprint 6)._
