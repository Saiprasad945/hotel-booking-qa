# Test Cases — Hotel Booking Application

**AUT:** Restful Booker Platform — https://automationintesting.online
**Total cases:** 110
**Legend — Type:** SM = Smoke, RG = Regression, NG = Negative | **Priority:** P1 (High), P2 (Medium), P3 (Low)
Each case traces to a user story (US) / acceptance criterion (AC) / requirement (REQ).

---

## Module 1 — Room Browsing (US-01, US-02)

| TC ID | Title | Preconditions | Steps | Test Data | Expected Result | Type | Pri | Traces |
|-------|-------|---------------|-------|-----------|-----------------|------|-----|--------|
| TC-001 | Homepage loads room list | AUT reachable | Open homepage | — | Rooms shown with type, image, price, amenities | SM | P1 | US-01/AC1 |
| TC-002 | Room shows amenities | Rooms exist | View a room card | — | Amenities (WiFi/TV/etc.) displayed | RG | P2 | US-01/AC1 |
| TC-003 | Open room details | Rooms exist | Click "Book this room"/details | — | Room detail/booking view opens | RG | P2 | US-01/AC2 |
| TC-004 | Price displayed per room | Rooms exist | Inspect each room card | — | Price shown as a number/currency | RG | P2 | US-01/AC1 |
| TC-005 | No-rooms empty state | All rooms deleted (admin) | Open homepage | — | Suitable "no rooms" state, no crash | RG | P3 | US-01/AC3 |
| TC-006 | Check availability valid range | Rooms exist | Select check-in and later check-out | 2026-08-01 → 2026-08-05 | Availability reflected/room bookable | SM | P1 | US-02/AC1 |
| TC-007 | Checkout before checkin rejected | On booking view | Set checkout ≤ checkin | in=2026-08-05, out=2026-08-01 | Rejected with message | NG | P1 | US-02/AC2 |
| TC-008 | Past check-in date blocked | On booking view | Try to select a past date | 2020-01-01 | Past date not selectable/rejected | NG | P2 | US-02/AC3 |

## Module 2 — Room Booking (US-03, US-04, US-05)

| TC ID | Title | Preconditions | Steps | Test Data | Expected Result | Type | Pri | Traces |
|-------|-------|---------------|-------|-----------|-----------------|------|-----|--------|
| TC-009 | Book room with valid data | Room available | Fill all fields, submit | valid guest, in=2026-08-10, out=2026-08-12 | Booking confirmed, dates shown | SM | P1 | US-03/AC1,AC4 |
| TC-010 | Booked dates become unavailable | TC-009 done | Retry same room/dates | same as TC-009 | Room shown unavailable | RG | P1 | US-03/AC5 |
| TC-011 | Firstname required | On booking form | Leave firstname empty, submit | firstname="" | Validation error for firstname | NG | P1 | US-04/AC1 |
| TC-012 | Lastname required | On booking form | Leave lastname empty, submit | lastname="" | Validation error for lastname | NG | P1 | US-04/AC1 |
| TC-013 | Email required | On booking form | Leave email empty, submit | email="" | Validation error for email | NG | P1 | US-04/AC1 |
| TC-014 | Phone required | On booking form | Leave phone empty, submit | phone="" | Validation error for phone | NG | P1 | US-04/AC1 |
| TC-015 | Invalid email format rejected | On booking form | Enter bad email, submit | email="abc" | Email format error | NG | P1 | US-04/AC2 |
| TC-016 | Firstname min length | On booking form | Enter 2-char firstname | firstname="Al" | Rejected (min 3) | NG | P2 | US-04/AC3 |
| TC-017 | Firstname max length | On booking form | Enter 19-char+ firstname | 25 chars | Rejected (max 18) | NG | P3 | US-04/AC3 |
| TC-018 | Phone min length | On booking form | Enter 10-char phone | 10 digits | Rejected (min 11) | NG | P2 | US-04/AC2 |
| TC-019 | Phone max length | On booking form | Enter 22-char+ phone | 25 digits | Rejected (max 21) | NG | P3 | US-04/AC2 |
| TC-020 | Boundary: firstname = 3 chars | On booking form | Enter exactly 3 chars | firstname="Ann" | Accepted | RG | P2 | US-04/AC3 |
| TC-021 | Boundary: phone = 11 digits | On booking form | Enter exactly 11 digits | 11 digits | Accepted | RG | P2 | US-04/AC2 |
| TC-022 | Form not submitted with errors | On booking form | Submit with multiple errors | multiple invalid | No booking created | NG | P1 | US-04/AC4 |
| TC-023 | Double booking prevented | Room booked for range | Book overlapping range | overlap of TC-009 | Rejected / not double-booked | RG | P1 | US-05/AC1,AC2 |
| TC-024 | Partial overlap prevented | Room booked 10–12 | Book 11–13 | in=11, out=13 | Rejected (overlap) | RG | P1 | US-05/AC1 |
| TC-025 | Adjacent dates allowed | Room booked 10–12 | Book 12–14 | in=12, out=14 | Allowed (no overlap) | RG | P2 | US-05/AC3 |
| TC-026 | Same-day checkin/checkout | On booking form | in=out | in=out=2026-08-10 | Rejected (min 1 night) | NG | P2 | US-02/AC2 |

## Module 3 — Contact / Enquiry (US-06, US-07)

| TC ID | Title | Preconditions | Steps | Test Data | Expected Result | Type | Pri | Traces |
|-------|-------|---------------|-------|-----------|-----------------|------|-----|--------|
| TC-027 | Send valid contact message | Homepage open | Fill all fields, submit | valid data | Success confirmation shown | SM | P1 | US-06/AC1,AC2 |
| TC-028 | Message appears in admin | TC-027 done | Login admin → Messages | — | Message listed | RG | P1 | US-06/AC3 |
| TC-029 | Name required | Contact form | Empty name, submit | name="" | Validation error | NG | P1 | US-07/AC1 |
| TC-030 | Email required | Contact form | Empty email, submit | email="" | Validation error | NG | P1 | US-07/AC1 |
| TC-031 | Phone required | Contact form | Empty phone, submit | phone="" | Validation error | NG | P1 | US-07/AC1 |
| TC-032 | Subject required | Contact form | Empty subject, submit | subject="" | Validation error | NG | P1 | US-07/AC1 |
| TC-033 | Message required | Contact form | Empty message, submit | message="" | Validation error | NG | P1 | US-07/AC1 |
| TC-034 | Invalid email rejected | Contact form | Bad email, submit | email="test@" | Email format error | NG | P1 | US-07/AC2 |
| TC-035 | Subject min length | Contact form | 4-char subject | "Hiii" (min 5) | Rejected | NG | P2 | US-07/AC3 |
| TC-036 | Message min length | Contact form | 19-char message | 19 chars (min 20) | Rejected | NG | P2 | US-07/AC3 |
| TC-037 | Message max length | Contact form | 2001-char message | 2001 chars | Rejected (max 2000) | NG | P3 | US-07/AC3 |
| TC-038 | Phone length boundaries | Contact form | 10 and 22 digit phone | 10 / 22 digits | Both rejected | NG | P2 | US-07/AC3 |

## Module 4 — Admin Authentication (US-08, US-09)

| TC ID | Title | Preconditions | Steps | Test Data | Expected Result | Type | Pri | Traces |
|-------|-------|---------------|-------|-----------|-----------------|------|-----|--------|
| TC-039 | Login with valid creds | On /admin | Enter valid creds, submit | admin/password | Admin dashboard shown | SM | P1 | US-08/AC1 |
| TC-040 | Login wrong password | On /admin | Valid user, wrong pass | admin/wrong | Error, no access | NG | P1 | US-08/AC2 |
| TC-041 | Login wrong username | On /admin | Wrong user, valid pass | bad/password | Error, no access | NG | P1 | US-08/AC2 |
| TC-042 | Login empty username | On /admin | Empty user | ""/password | Rejected | NG | P2 | US-08/AC3 |
| TC-043 | Login empty password | On /admin | Empty pass | admin/"" | Rejected | NG | P2 | US-08/AC3 |
| TC-044 | Login both empty | On /admin | Submit blank | ""/"" | Rejected | NG | P2 | US-08/AC3 |
| TC-045 | Logout ends session | Logged in | Click logout | — | Returned to login/public | SM | P1 | US-09/AC1 |
| TC-046 | Protected page needs auth | Logged out | Open admin URL directly | /admin | Redirect to login | NG | P1 | US-09/AC2 |
| TC-047 | Back button after logout | Logged out | Press browser Back | — | No admin data exposed | NG | P2 | US-09/AC2 |
| TC-048 | Case-sensitive password | On /admin | Enter PASSWORD | admin/PASSWORD | Rejected | NG | P3 | US-08/AC2 |

## Module 5 — Room Management (Admin) (US-10, US-11, US-12)

| TC ID | Title | Preconditions | Steps | Test Data | Expected Result | Type | Pri | Traces |
|-------|-------|---------------|-------|-----------|-----------------|------|-----|--------|
| TC-049 | Create room valid | Logged in | Fill room form, save | 101, Single, £100 | Room created & listed | SM | P1 | US-10/AC1,AC4 |
| TC-050 | Create room all amenities | Logged in | Check WiFi/TV/etc., save | all amenities | Room saved with amenities | RG | P2 | US-10/AC1 |
| TC-051 | Room number must be numeric | Logged in | Enter text room no. | "ABC" | Rejected | NG | P1 | US-10/AC2 |
| TC-052 | Price must be numeric | Logged in | Enter text price | price="free" | Rejected | NG | P1 | US-10/AC2 |
| TC-053 | Room number required | Logged in | Empty room no., save | "" | Validation error | NG | P1 | US-10/AC3 |
| TC-054 | Price required | Logged in | Empty price, save | "" | Validation error | NG | P1 | US-10/AC3 |
| TC-055 | Negative price rejected | Logged in | Enter -50 | price=-50 | Rejected | NG | P2 | US-10/AC2 |
| TC-056 | Zero price boundary | Logged in | Enter 0 | price=0 | Per rules (rejected/allowed) | RG | P3 | US-10/AC2 |
| TC-057 | Duplicate room number | Room 101 exists | Create another 101 | 101 | Handled (reject/allow per rules) | RG | P2 | US-10/AC2 |
| TC-058 | Edit room type | Room exists | Edit type, save | Single→Double | Change persisted | RG | P1 | US-11/AC2 |
| TC-059 | Edit room price | Room exists | Edit price, save | £100→£150 | Change persisted | RG | P1 | US-11/AC2 |
| TC-060 | Edit invalid price rejected | Room exists | Set price to text | "abc" | Rejected | NG | P2 | US-11/AC3 |
| TC-061 | Edit loads current values | Room exists | Open edit form | — | Fields pre-filled | RG | P2 | US-11/AC1 |
| TC-062 | Delete room | Room exists | Delete room | — | Removed from list | SM | P1 | US-12/AC1 |
| TC-063 | Deleted room not retrievable | TC-062 done | GET the room | deleted id | Not found | RG | P2 | US-12/AC2 |

## Module 6 — Booking Management (Admin) (US-13)

| TC ID | Title | Preconditions | Steps | Test Data | Expected Result | Type | Pri | Traces |
|-------|-------|---------------|-------|-----------|-----------------|------|-----|--------|
| TC-064 | View bookings calendar | Logged in | Open report/calendar | — | Existing bookings visible | SM | P1 | US-13/AC1 |
| TC-065 | Admin creates booking | Logged in | Add booking for guest | valid data | Booking created | RG | P1 | US-13/AC2 |
| TC-066 | Admin deletes booking | Booking exists | Delete booking | — | Booking removed, dates freed | RG | P1 | US-13/AC3 |
| TC-067 | Freed dates re-bookable | TC-066 done | Book same dates | freed range | Booking succeeds | RG | P2 | US-13/AC3 |
| TC-068 | Booking shows guest name | Booking exists | Open booking | — | Guest details shown | RG | P2 | US-13/AC1 |
| TC-069 | Calendar reflects new booking | New booking made | Refresh calendar | — | Booking appears on dates | RG | P2 | US-13/AC1 |

## Module 7 — Message Management (Admin) (US-14)

| TC ID | Title | Preconditions | Steps | Test Data | Expected Result | Type | Pri | Traces |
|-------|-------|---------------|-------|-----------|-----------------|------|-----|--------|
| TC-070 | List all messages | Logged in | Open Messages | — | Messages listed | SM | P1 | US-14/AC1 |
| TC-071 | Unread indicator shown | Unread msg exists | View list | — | Unread marker present | RG | P2 | US-14/AC2 |
| TC-072 | Open marks read | Unread msg exists | Open message | — | Marked read, indicator cleared | RG | P2 | US-14/AC2 |
| TC-073 | Message content correct | TC-027 sent | Open that message | — | Name/subject/message match input | RG | P1 | US-14/AC1 |
| TC-074 | Delete message | Message exists | Delete | — | Removed from list | RG | P2 | US-14/AC3 |
| TC-075 | Deleted message not retrievable | TC-074 done | GET message | deleted id | Not found | RG | P3 | US-14/AC3 |

## Module 8 — Branding (Admin) (US-15)

| TC ID | Title | Preconditions | Steps | Test Data | Expected Result | Type | Pri | Traces |
|-------|-------|---------------|-------|-----------|-----------------|------|-----|--------|
| TC-076 | Edit hotel name | Logged in | Change name, save | "Sai Grand Hotel" | Saved | RG | P2 | US-15/AC1 |
| TC-077 | Edit description | Logged in | Change description, save | new text | Saved | RG | P2 | US-15/AC1 |
| TC-078 | Edit contact details | Logged in | Change phone/email/address | valid | Saved | RG | P2 | US-15/AC1 |
| TC-079 | Branding reflects on homepage | TC-076 done | Open homepage | — | New name shown | RG | P1 | US-15/AC2 |
| TC-080 | Invalid contact email rejected | Logged in | Bad email, save | "x@" | Rejected | NG | P3 | US-15/AC1 |

## Module 9 — API Tests (REST) — Sprints 3 & 5

| TC ID | Title | Preconditions | Steps | Test Data | Expected Result | Type | Pri | Traces |
|-------|-------|---------------|-------|-----------|-----------------|------|-----|--------|
| TC-081 | POST /auth/login valid | — | POST valid creds | admin/password | 200 + token | SM | P1 | REQ-15 |
| TC-082 | POST /auth/login invalid | — | POST bad creds | bad/bad | 401/403, no token | NG | P1 | REQ-16 |
| TC-083 | Access protected API no token | — | DELETE /room/{id} without token | — | 401/403 | NG | P1 | REQ-18 |
| TC-084 | GET /room list | — | GET /room | — | 200 + rooms array | SM | P1 | REQ-01 |
| TC-085 | GET /room/{id} valid | Room exists | GET by id | valid id | 200 + room object | RG | P1 | REQ-02 |
| TC-086 | GET /room/{id} invalid | — | GET nonexistent id | 999999 | 404 | NG | P2 | REQ-02 |
| TC-087 | POST /room valid | Token | Create room | valid body | 200/201 + room | RG | P1 | REQ-19 |
| TC-088 | POST /room missing field | Token | Create w/o roomName | partial body | 400 validation | NG | P1 | REQ-22 |
| TC-089 | POST /room non-numeric price | Token | Create bad price | price="x" | 400 | NG | P2 | REQ-22 |
| TC-090 | PUT /room/{id} update | Token, room | Update room | new price | 200 + updated | RG | P1 | REQ-20 |
| TC-091 | DELETE /room/{id} | Token, room | Delete room | valid id | 200/202 | RG | P1 | REQ-21 |
| TC-092 | GET /booking list | — | GET /booking | — | 200 + bookings | RG | P2 | REQ-23 |
| TC-093 | POST /booking valid | Room exists | Create booking | valid body | 200/201 + booking | SM | P1 | REQ-04 |
| TC-094 | POST /booking checkout<checkin | Room exists | Bad dates | out<in | 400/500 rejected | NG | P1 | REQ-05 |
| TC-095 | POST /booking missing name | Room exists | Omit firstname | partial | 400 | NG | P1 | REQ-06 |
| TC-096 | POST /booking overlap | Booking exists | Overlapping dates | overlap | Rejected/conflict | RG | P1 | REQ-07 |
| TC-097 | GET /booking/{id} | Booking exists | GET by id | valid id | 200 + booking | RG | P2 | REQ-24 |
| TC-098 | PUT /booking/{id} | Token, booking | Update booking | new dates | 200 + updated | RG | P2 | REQ-24 |
| TC-099 | DELETE /booking/{id} | Token, booking | Delete | valid id | 200/202 | RG | P1 | REQ-25 |
| TC-100 | POST /message valid | — | Submit message | valid body | 200/201 | RG | P2 | REQ-10 |
| TC-101 | POST /message invalid email | — | Bad email | "x@" | 400 | NG | P2 | REQ-11 |
| TC-102 | GET /message list | Token | GET /message | — | 200 + messages | RG | P2 | REQ-26 |
| TC-103 | PUT /message/{id} mark read | Token, msg | Mark read | id | 200, read=true | RG | P3 | REQ-27 |
| TC-104 | DELETE /message/{id} | Token, msg | Delete | id | 200/202 | RG | P3 | REQ-28 |
| TC-105 | GET /branding | — | GET /branding | — | 200 + branding | RG | P3 | REQ-29 |
| TC-106 | PUT /branding update | Token | Update branding | new name | 200 + updated | RG | P3 | REQ-29 |

## Module 10 — Non-Functional & Cross-Platform

| TC ID | Title | Preconditions | Steps | Test Data | Expected Result | Type | Pri | Traces |
|-------|-------|---------------|-------|-----------|-----------------|------|-----|--------|
| TC-107 | Homepage load time | — | Measure load | — | < 3s (NFR-02) | RG | P2 | NFR-02 |
| TC-108 | Cross-browser booking (Chrome) | — | Book in Chrome | valid | Works | SM | P1 | NFR-04 |
| TC-109 | Cross-browser booking (Firefox) | — | Book in Firefox | valid | Works | RG | P2 | NFR-04 |
| TC-110 | API status codes correct | — | Hit each endpoint | — | 2xx/4xx/5xx as appropriate | RG | P2 | NFR-05 |
