-- =====================================================================
-- SQL Data Validation Queries — Hotel Booking DB
-- These are the checks a QA engineer runs to verify data integrity.
-- Each query should return ZERO rows (or the expected count) if data is valid.
-- SQLite dialect; all of these run unchanged on MySQL.
-- =====================================================================

-- 1. Record counts per table (sanity — none should be empty)
SELECT 'rooms'    AS table_name, COUNT(*) AS row_count FROM rooms
UNION ALL SELECT 'guests',   COUNT(*) FROM guests
UNION ALL SELECT 'bookings', COUNT(*) FROM bookings
UNION ALL SELECT 'payments', COUNT(*) FROM payments
UNION ALL SELECT 'messages', COUNT(*) FROM messages;

-- 2. Duplicate room numbers (should return 0 rows)
SELECT room_name, COUNT(*) AS cnt
FROM rooms
GROUP BY room_name
HAVING COUNT(*) > 1;

-- 3. Orphan bookings — room_id not present in rooms (FK integrity; expect 0)
SELECT b.booking_id, b.room_id
FROM bookings b
LEFT JOIN rooms r ON b.room_id = r.room_id
WHERE r.room_id IS NULL;

-- 4. Orphan bookings — guest_id not present in guests (expect 0)
SELECT b.booking_id, b.guest_id
FROM bookings b
LEFT JOIN guests g ON b.guest_id = g.guest_id
WHERE g.guest_id IS NULL;

-- 5. Orphan payments — booking_id not present in bookings (expect 0)
SELECT p.payment_id, p.booking_id
FROM payments p
LEFT JOIN bookings b ON p.booking_id = b.booking_id
WHERE b.booking_id IS NULL;

-- 6. Date consistency — checkout must be after checkin (expect 0)
SELECT booking_id, checkin, checkout
FROM bookings
WHERE checkout <= checkin;

-- 7. Overlapping bookings for the same room (double-booking; expect 0)
SELECT a.booking_id AS booking_a, b.booking_id AS booking_b, a.room_id
FROM bookings a
JOIN bookings b
  ON a.room_id = b.room_id
 AND a.booking_id < b.booking_id
 AND a.checkin < b.checkout
 AND b.checkin < a.checkout;

-- 8. NULL / empty required fields in guests (expect 0)
SELECT guest_id
FROM guests
WHERE firstname IS NULL OR firstname = ''
   OR lastname  IS NULL OR lastname  = ''
   OR email     IS NULL OR email     = ''
   OR phone     IS NULL OR phone     = '';

-- 9. Basic email format check — must contain '@' and '.' (expect 0 invalid)
SELECT guest_id, email
FROM guests
WHERE email NOT LIKE '%_@_%._%';

-- 10. Negative or zero prices (expect 0)
SELECT room_id, room_name, room_price
FROM rooms
WHERE room_price <= 0;

-- 11. Payment amount vs stay length sanity
--     (amount should be > 0 for PAID bookings; expect 0 violations)
SELECT p.payment_id, p.status, p.amount
FROM payments p
WHERE p.status = 'PAID' AND p.amount <= 0;
