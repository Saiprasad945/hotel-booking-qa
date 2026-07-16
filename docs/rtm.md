# Requirements Traceability Matrix (RTM) — Hotel Booking Application

Maps every requirement → user story → test case(s), and confirms coverage.
Bidirectional: use it to check *"is every requirement tested?"* and
*"which requirement does this test cover?"*

**Coverage summary:** 29/29 functional requirements covered · 5/5 NFRs covered · 110 test cases.

---

## Functional requirements

| REQ ID | Requirement (short) | User Story | Test Cases | Covered |
|--------|---------------------|-----------|------------|:-------:|
| REQ-01 | Display room list | US-01 | TC-001, TC-002, TC-004, TC-084 | ✅ |
| REQ-02 | View room details | US-01 | TC-003, TC-085, TC-086 | ✅ |
| REQ-03 | Check availability | US-02 | TC-006, TC-007, TC-008 | ✅ |
| REQ-04 | Book with required fields | US-03 | TC-009, TC-093 | ✅ |
| REQ-05 | Checkout after checkin | US-03, US-02 | TC-007, TC-026, TC-094 | ✅ |
| REQ-06 | Validate booking fields | US-03, US-04 | TC-011–TC-021, TC-095 | ✅ |
| REQ-07 | Prevent double-booking | US-05 | TC-023, TC-024, TC-025, TC-096 | ✅ |
| REQ-08 | Booking confirmation | US-03 | TC-009 | ✅ |
| REQ-09 | Validation error messages | US-04 | TC-011–TC-022 | ✅ |
| REQ-10 | Contact form | US-06 | TC-027, TC-100 | ✅ |
| REQ-11 | Validate contact fields | US-07 | TC-029–TC-038, TC-101 | ✅ |
| REQ-12 | Contact success confirmation | US-06 | TC-027 | ✅ |
| REQ-13 | Reject invalid contact | US-07 | TC-029–TC-038 | ✅ |
| REQ-14 | Admin login page | US-08 | TC-039 | ✅ |
| REQ-15 | Grant access valid creds | US-08 | TC-039, TC-081 | ✅ |
| REQ-16 | Reject invalid creds | US-08 | TC-040, TC-041, TC-048, TC-082 | ✅ |
| REQ-17 | Admin logout | US-09 | TC-045 | ✅ |
| REQ-18 | Protect admin pages | US-09 | TC-046, TC-047, TC-083 | ✅ |
| REQ-19 | Create room | US-10 | TC-049, TC-050, TC-087 | ✅ |
| REQ-20 | Edit room | US-11 | TC-058, TC-059, TC-061, TC-090 | ✅ |
| REQ-21 | Delete room | US-12 | TC-062, TC-063, TC-091 | ✅ |
| REQ-22 | Validate room fields | US-10 | TC-051–TC-057, TC-088, TC-089 | ✅ |
| REQ-23 | View bookings | US-13 | TC-064, TC-069, TC-092 | ✅ |
| REQ-24 | Admin create booking | US-13 | TC-065, TC-097, TC-098 | ✅ |
| REQ-25 | Admin delete booking | US-13 | TC-066, TC-067, TC-099 | ✅ |
| REQ-26 | View messages | US-14 | TC-070, TC-073, TC-102 | ✅ |
| REQ-27 | Mark message read | US-14 | TC-071, TC-072, TC-103 | ✅ |
| REQ-28 | Delete message | US-14 | TC-074, TC-075, TC-104 | ✅ |
| REQ-29 | Edit branding | US-15 | TC-076–TC-080, TC-105, TC-106 | ✅ |

## Non-functional requirements

| NFR ID | Requirement (short) | Test Cases | Covered |
|--------|---------------------|------------|:-------:|
| NFR-01 | Inline validation < 2s | TC-011–TC-038 (observed) | ✅ |
| NFR-02 | Homepage load < 3s | TC-107 | ✅ |
| NFR-03 | Session token protection | TC-046, TC-083 | ✅ |
| NFR-04 | Cross-browser support | TC-108, TC-109 | ✅ |
| NFR-05 | Correct HTTP status codes | TC-110, TC-082–TC-106 | ✅ |

---

## Coverage by module

| Module | Test cases | Smoke | Negative |
|--------|-----------:|------:|---------:|
| Room Browsing | 8 | 2 | 2 |
| Room Booking | 18 | 2 | 11 |
| Contact Form | 12 | 1 | 10 |
| Admin Auth | 10 | 2 | 7 |
| Room Management | 15 | 2 | 7 |
| Booking Management | 6 | 1 | 0 |
| Message Management | 6 | 1 | 0 |
| Branding | 5 | 0 | 1 |
| API | 26 | 4 | 8 |
| Non-Functional | 4 | 1 | 0 |
| **Total** | **110** | **16** | **46** |
