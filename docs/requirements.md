# Requirements Specification — Hotel Booking Application

**Application Under Test (AUT):** Restful Booker Platform — https://automationintesting.online
**Document version:** 1.0
**Author:** QA Team

---

## 1. Purpose

This document defines the functional and non-functional requirements for the
Hotel Booking application. Each requirement has a unique ID (`REQ-xx`) and is
traced to user stories and test cases in later sprints (see the RTM).

## 2. Scope

The application allows **guests** to view rooms, check availability, and make
bookings, and to send enquiries via a contact form. It allows **hotel
administrators** to log in and manage rooms, bookings, contact messages, and
site branding.

## 3. Actors

| Actor | Description |
|-------|-------------|
| Guest | An unauthenticated visitor who browses and books rooms and sends enquiries. |
| Admin | An authenticated hotel staff member who manages rooms, bookings, and messages. |

---

## 4. Functional Requirements

### 4.1 Room browsing (Guest)

| ID | Requirement |
|----|-------------|
| REQ-01 | The system shall display a list of available rooms on the homepage, each showing room type, description, image, price, and amenities. |
| REQ-02 | The system shall allow a guest to view the details of an individual room. |
| REQ-03 | The system shall allow a guest to check room availability for a selected date range. |

### 4.2 Room booking (Guest)

| ID | Requirement |
|----|-------------|
| REQ-04 | The system shall allow a guest to book an available room by providing firstname, lastname, email, phone, check-in date, and check-out date. |
| REQ-05 | The system shall validate that check-out date is after check-in date. |
| REQ-06 | The system shall validate that all required booking fields are provided and correctly formatted (valid email, phone length within allowed range). |
| REQ-07 | The system shall prevent a room from being double-booked for overlapping dates. |
| REQ-08 | The system shall display a booking confirmation on success. |
| REQ-09 | The system shall display clear validation error messages when booking data is invalid or incomplete. |

### 4.3 Contact / enquiry (Guest)

| ID | Requirement |
|----|-------------|
| REQ-10 | The system shall provide a contact form accepting name, email, phone, subject, and message. |
| REQ-11 | The system shall validate all contact form fields, including a valid email format and minimum/maximum field lengths. |
| REQ-12 | The system shall confirm to the guest that a message was sent successfully. |
| REQ-13 | The system shall reject a contact submission with missing or invalid fields and display validation errors. |

### 4.4 Admin authentication (Admin)

| ID | Requirement |
|----|-------------|
| REQ-14 | The system shall provide an admin login page requiring a username and password. |
| REQ-15 | The system shall grant access to the admin area only with valid credentials. |
| REQ-16 | The system shall reject invalid credentials and display an error message. |
| REQ-17 | The system shall allow an authenticated admin to log out, ending the session. |
| REQ-18 | The system shall protect admin pages from unauthenticated access. |

### 4.5 Room management (Admin)

| ID | Requirement |
|----|-------------|
| REQ-19 | The system shall allow an admin to create a new room specifying room number, type, accessibility, price, and amenities (WiFi, TV, radio, refreshments, safe, views). |
| REQ-20 | The system shall allow an admin to edit an existing room's details. |
| REQ-21 | The system shall allow an admin to delete a room. |
| REQ-22 | The system shall validate room fields, including a numeric room number and a valid price. |

### 4.6 Booking management (Admin)

| ID | Requirement |
|----|-------------|
| REQ-23 | The system shall allow an admin to view existing bookings on a calendar/report view. |
| REQ-24 | The system shall allow an admin to create a booking on behalf of a guest. |
| REQ-25 | The system shall allow an admin to delete a booking. |

### 4.7 Message management (Admin)

| ID | Requirement |
|----|-------------|
| REQ-26 | The system shall allow an admin to view all contact messages submitted by guests. |
| REQ-27 | The system shall indicate unread messages and allow an admin to mark a message as read. |
| REQ-28 | The system shall allow an admin to delete a message. |

### 4.8 Branding (Admin)

| ID | Requirement |
|----|-------------|
| REQ-29 | The system shall allow an admin to edit site branding: hotel name, description, contact details, and map location. |

---

## 5. Non-Functional Requirements

| ID | Requirement |
|----|-------------|
| NFR-01 | **Usability:** All forms shall display inline validation messages within 2 seconds of submission. |
| NFR-02 | **Performance:** Homepage room list shall load within 3 seconds on a standard broadband connection. |
| NFR-03 | **Security:** Admin session shall be protected by a token; expired/invalid tokens shall be rejected. |
| NFR-04 | **Compatibility:** The UI shall function on the latest versions of Chrome, Firefox, and Edge. |
| NFR-05 | **Reliability:** The REST API shall return appropriate HTTP status codes (2xx success, 4xx client error, 5xx server error). |

---

## 6. API surface (for API testing sprints)

The platform exposes REST endpoints used in Sprints 3 & 5:

| Area | Method & Endpoint (base: `/`) |
|------|-------------------------------|
| Auth | `POST /auth/login`, `POST /auth/validate`, `POST /auth/logout` |
| Rooms | `GET /room`, `GET /room/{id}`, `POST /room`, `PUT /room/{id}`, `DELETE /room/{id}` |
| Booking | `GET /booking`, `GET /booking/{id}`, `POST /booking`, `PUT /booking/{id}`, `DELETE /booking/{id}` |
| Report | `GET /report` |
| Message | `GET /message`, `GET /message/{id}`, `POST /message`, `PUT /message/{id}`, `DELETE /message/{id}` |
| Branding | `GET /branding`, `PUT /branding` |

> Note: exact paths may vary by deployment; they are confirmed against live responses during Sprint 3.

---

## 7. Assumptions & constraints

- The AUT is a shared public test environment; data may be reset periodically.
- Default admin credentials are `admin` / `password`.
- No real payments are processed; booking is reservation-only.
