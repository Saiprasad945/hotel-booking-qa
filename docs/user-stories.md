# User Stories — Hotel Booking Application

**AUT:** Restful Booker Platform — https://automationintesting.online
Format: *As a [role], I want [goal] so that [benefit].*
Each story lists **Acceptance Criteria (AC)** that become test cases in Sprint 2.

---

## Epic 1 — Room Browsing

### US-01 — View available rooms
**As a** guest, **I want** to see the list of rooms on the homepage **so that** I can choose one to book.
_Traces to: REQ-01, REQ-02_

**Acceptance Criteria**
- AC1: Homepage displays each room with type, description, image, price, and amenities.
- AC2: Clicking a room shows its full details.
- AC3: If no rooms exist, a suitable "no rooms available" state is shown.

### US-02 — Check availability by date
**As a** guest, **I want** to check whether rooms are free for my dates **so that** I only try to book available rooms.
_Traces to: REQ-03_

**Acceptance Criteria**
- AC1: Selecting a check-in and check-out date filters/indicates available rooms.
- AC2: Check-out earlier than or equal to check-in is rejected with a message.
- AC3: Past dates are not selectable for check-in.

---

## Epic 2 — Room Booking

### US-03 — Book an available room
**As a** guest, **I want** to book an available room **so that** I can reserve my stay.
_Traces to: REQ-04, REQ-05, REQ-06, REQ-08_

**Acceptance Criteria**
- AC1: Booking requires firstname, lastname, email, phone, check-in, check-out.
- AC2: Check-out date must be after check-in date.
- AC3: Email must be a valid format; phone must meet length rules.
- AC4: On success, a confirmation is shown with the booked dates.
- AC5: The booked dates become unavailable for that room.

### US-04 — Prevent invalid or incomplete bookings
**As a** guest, **I want** clear errors when my booking data is wrong **so that** I can correct it.
_Traces to: REQ-06, REQ-09_

**Acceptance Criteria**
- AC1: Submitting with any required field empty shows a validation error naming the field(s).
- AC2: Invalid email format is rejected.
- AC3: Firstname/lastname below minimum length are rejected.
- AC4: The form is not submitted while validation errors exist.

### US-05 — Prevent double-booking
**As a** guest, **I want** the system to block overlapping bookings **so that** I never reserve an already-taken room.
_Traces to: REQ-07_

**Acceptance Criteria**
- AC1: A room booked for a date range cannot be booked again for overlapping dates.
- AC2: Attempting an overlapping booking is rejected with a clear message.
- AC3: Non-overlapping (adjacent) dates for the same room are allowed.

---

## Epic 3 — Contact / Enquiry

### US-06 — Send a contact message
**As a** guest, **I want** to send an enquiry via the contact form **so that** I can ask the hotel a question.
_Traces to: REQ-10, REQ-12_

**Acceptance Criteria**
- AC1: Form accepts name, email, phone, subject, message.
- AC2: On valid submission, a success confirmation is shown.
- AC3: The submitted message appears in the admin Messages area.

### US-07 — Validate contact form input
**As a** guest, **I want** validation on the contact form **so that** I know when my input is wrong.
_Traces to: REQ-11, REQ-13_

**Acceptance Criteria**
- AC1: Empty required fields produce validation errors.
- AC2: Invalid email format is rejected.
- AC3: Fields below/above allowed length are rejected (e.g. subject and message minimum length).
- AC4: The form is not submitted while errors exist.

---

## Epic 4 — Admin Authentication

### US-08 — Admin login
**As an** admin, **I want** to log in **so that** I can manage the hotel.
_Traces to: REQ-14, REQ-15, REQ-16_

**Acceptance Criteria**
- AC1: Valid credentials (`admin` / `password`) grant access to the admin area.
- AC2: Invalid username or password is rejected with an error message.
- AC3: Empty username or password is rejected.

### US-09 — Admin logout & protected pages
**As an** admin, **I want** to log out and have admin pages protected **so that** unauthorized users cannot access management functions.
_Traces to: REQ-17, REQ-18_

**Acceptance Criteria**
- AC1: Logging out ends the session and returns to a public/login view.
- AC2: Accessing an admin URL without a session redirects to login.
- AC3: An expired/invalid session token is rejected.

---

## Epic 5 — Room Management (Admin)

### US-10 — Create a room
**As an** admin, **I want** to add a new room **so that** guests can book it.
_Traces to: REQ-19, REQ-22_

**Acceptance Criteria**
- AC1: A room can be created with room number, type, accessibility, price, amenities.
- AC2: Room number must be numeric; price must be a valid number.
- AC3: Missing required fields are rejected with validation errors.
- AC4: The new room appears in the room list.

### US-11 — Edit a room
**As an** admin, **I want** to edit a room **so that** I can keep details accurate.
_Traces to: REQ-20_

**Acceptance Criteria**
- AC1: Existing room details load into an editable form.
- AC2: Saved changes are persisted and reflected in the list.
- AC3: Invalid edits (e.g. non-numeric price) are rejected.

### US-12 — Delete a room
**As an** admin, **I want** to delete a room **so that** obsolete rooms are removed.
_Traces to: REQ-21_

**Acceptance Criteria**
- AC1: Deleting a room removes it from the list.
- AC2: A deleted room can no longer be retrieved.

---

## Epic 6 — Booking Management (Admin)

### US-13 — View & manage bookings
**As an** admin, **I want** to view and manage bookings **so that** I can run the front desk.
_Traces to: REQ-23, REQ-24, REQ-25_

**Acceptance Criteria**
- AC1: Existing bookings are visible on a calendar/report view.
- AC2: An admin can create a booking for a guest.
- AC3: An admin can delete a booking, freeing the dates.

---

## Epic 7 — Message Management (Admin)

### US-14 — Manage contact messages
**As an** admin, **I want** to read and manage guest messages **so that** I can respond to enquiries.
_Traces to: REQ-26, REQ-27, REQ-28_

**Acceptance Criteria**
- AC1: All submitted messages are listed.
- AC2: Unread messages are indicated; opening one marks it read.
- AC3: A message can be deleted.

---

## Epic 8 — Branding (Admin)

### US-15 — Edit site branding
**As an** admin, **I want** to update hotel branding **so that** the site reflects current information.
_Traces to: REQ-29_

**Acceptance Criteria**
- AC1: Hotel name, description, contact details, and map can be edited.
- AC2: Saved branding changes appear on the public homepage.
