-- Hotel Booking database schema (SQLite dialect)
-- MySQL equivalent: INTEGER PRIMARY KEY AUTOINCREMENT -> INT AUTO_INCREMENT PRIMARY KEY,
-- and the same FOREIGN KEY constraints apply.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS messages;
DROP TABLE IF EXISTS guests;
DROP TABLE IF EXISTS rooms;

-- Rooms (populated from the live API: GET /api/room)
CREATE TABLE rooms (
    room_id     INTEGER PRIMARY KEY,          -- matches API roomid
    room_name   TEXT    NOT NULL,             -- API roomName (e.g. "101")
    type        TEXT    NOT NULL,             -- Single / Double / Suite ...
    accessible  INTEGER NOT NULL,             -- 0/1
    room_price  REAL    NOT NULL CHECK (room_price >= 0),
    description TEXT
);

-- Guests who make bookings
CREATE TABLE guests (
    guest_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname  TEXT NOT NULL,
    email     TEXT NOT NULL,
    phone     TEXT NOT NULL
);

-- Bookings link a guest to a room for a date range
CREATE TABLE bookings (
    booking_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    room_id      INTEGER NOT NULL,
    guest_id     INTEGER NOT NULL,
    checkin      DATE    NOT NULL,
    checkout     DATE    NOT NULL,
    deposit_paid INTEGER NOT NULL,            -- 0/1
    FOREIGN KEY (room_id)  REFERENCES rooms(room_id),
    FOREIGN KEY (guest_id) REFERENCES guests(guest_id),
    CHECK (checkout > checkin)                -- data-integrity rule
);

-- Payments belong to a booking
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id INTEGER NOT NULL,
    amount     REAL    NOT NULL CHECK (amount >= 0),
    status     TEXT    NOT NULL,              -- PAID / PENDING / REFUNDED
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
);

-- Contact messages (populated via the contact form / API)
CREATE TABLE messages (
    message_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    email       TEXT NOT NULL,
    phone       TEXT,
    subject     TEXT NOT NULL,
    description TEXT NOT NULL
);
