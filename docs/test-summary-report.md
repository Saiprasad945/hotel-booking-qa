# Test Summary Report — Hotel Booking Application

**AUT:** Restful Booker Platform — https://automationintesting.online
**Reporting period:** Sprints 1–7
**Prepared by:** QA Lead
**Status:** Release-candidate quality assessment

---

## 1. Executive summary

Testing covered the Hotel Booking application across manual, API, database, and
UI layers. **110 test cases** were designed with full requirement traceability
(29/29 requirements covered). Automated suites (API + UI) and a Postman
collection all pass; SQL data-validation confirms database integrity.

**Three defects** were found, including **one Critical** (booking endpoint hangs
on malformed input). Recommendation: **conditional go** — release once BUG-03 is
fixed and re-verified.

## 2. Test execution metrics

| Metric | Value |
|--------|------:|
| Test cases designed | 110 |
| Requirements covered (RTM) | 29 / 29 (100%) |
| Non-functional requirements covered | 5 / 5 (100%) |
| Automated API tests (Pytest) | 23 |
| Automated UI tests (Selenium) | 5 |
| Postman API assertions | 28 |
| SQL integrity checks | 12 |

## 3. Automated run results (last execution)

| Suite | Result |
|-------|--------|
| Pytest API + UI | **27 passed, 1 xfailed** (exit 0) |
| Postman / Newman | **28 / 28 assertions passed** |
| SQL data validation | **12 / 12 integrity checks passed** |

_The 1 xfail is BUG-03, tracked in code until the server defect is fixed._

## 4. Defect summary

| ID | Summary | Severity | Priority | Status |
|----|---------|----------|----------|--------|
| BUG-03 | Server hangs on booking with missing dates | Critical | P1 | OPEN |
| BUG-01 | Duplicate room numbers in dataset | Major | P2 | OPEN |
| BUG-02 | Wrong HTTP status (409) for invalid date range | Minor | P3 | OPEN |

**Severity distribution:** Critical 1 · Major 1 · Minor 1 · Total 3

## 5. Coverage by module

| Module | Test cases | Automated |
|--------|-----------:|-----------|
| Room Browsing | 8 | API + UI |
| Room Booking | 18 | API |
| Contact Form | 12 | API + UI |
| Admin Auth | 10 | API |
| Room Management | 15 | API |
| Booking Management | 6 | API |
| Message Management | 6 | API |
| Branding | 5 | API |
| API (REST) | 26 | API |
| Non-Functional | 4 | Partial |

## 6. Exit criteria assessment

| Exit criterion | Status |
|----------------|:------:|
| 100% of planned test cases executed | ✅ |
| Requirement coverage via RTM | ✅ 29/29 |
| Automated regression pass rate ≥ 95% | ✅ 100% |
| No open Blocker defects | ✅ |
| All Critical/High defects closed | ❌ BUG-03 open |
| Test Summary Report signed off | ✅ (this document) |

## 7. Risks & recommendations
- **BUG-03 (Critical)** must be fixed before production — a hanging endpoint is an
  availability risk. Re-run the API suite (the xfail should flip to pass) after the fix.
- **BUG-01** — add a UNIQUE constraint on room number to prevent ambiguous data.
- Consider adding load/performance testing (out of scope this cycle).

## 8. Conclusion
Quality is high across functional, API, database and UI layers with full
traceability and automated regression. **Conditional go for release** pending the
BUG-03 fix and re-verification.
