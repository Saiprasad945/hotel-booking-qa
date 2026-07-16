# Test Plan — Hotel Booking Application

**AUT:** Restful Booker Platform — https://automationintesting.online
**Document version:** 1.0
**Prepared by:** QA Lead
**Based on:** IEEE 829 test plan structure (tailored)

---

## 1. Introduction
This test plan defines the strategy, scope, resources, schedule, and exit
criteria for testing the Hotel Booking application across manual, API,
database, and UI-automation layers. It traces to the requirements
(`requirements.md`) and user stories (`user-stories.md`).

## 2. Objectives
- Verify all functional requirements (REQ-01–29) and key non-functional requirements.
- Validate data integrity between the API and the database.
- Establish an automated regression suite (API + UI) runnable in CI.
- Provide measurable quality metrics for release decisions.

## 3. Scope

### 3.1 In scope
- Guest flows: room browsing, availability, booking, contact form.
- Admin flows: authentication, room/booking/message management, branding.
- REST API: auth, room, booking, message, branding, report endpoints.
- Database validation of bookings, rooms, and messages.
- Cross-browser UI smoke (Chrome primary; Firefox/Edge spot-checks).

### 3.2 Out of scope
- Payment processing (not implemented in the AUT).
- Load/stress testing beyond a basic performance sanity check.
- Penetration/security testing beyond auth and session basics.

## 4. Test strategy

| Test type | Layer | Approach | Sprint |
|-----------|-------|----------|--------|
| Functional / manual | UI | Test cases from acceptance criteria | 2 |
| API testing | API | Postman collection (positive, negative, auth) | 3 |
| Database validation | DB | SQL queries + Python checks | 4 |
| API automation | API | Python + Requests + Pytest, data-driven | 5 |
| UI automation | UI | Selenium + Page Object Model | 6 |
| Regression | API+UI | Automated suites run in CI on every push | 5–7 |
| Smoke | API+UI | Critical-path subset, tagged for fast runs | 2, 5, 6 |

### 4.1 Test design techniques
- **Equivalence Partitioning** and **Boundary Value Analysis** (e.g. date ranges, field lengths).
- **Decision tables** for booking validation combinations.
- **State transition** for booking availability (free → booked → free after delete).
- **Error guessing / exploratory** for edge cases (leveraging domain experience).

## 5. Test environment

| Item | Detail |
|------|--------|
| AUT URL | https://automationintesting.online |
| API base | Same host, REST endpoints (see requirements §6) |
| Admin creds | `admin` / `password` |
| Database | Local MySQL 8.x (Sprint 4 validation DB) |
| Automation | Python 3.11, Pytest, Requests, Selenium, ChromeDriver |
| CI | GitHub Actions (Ubuntu runner) |
| Browsers | Chrome (primary), Firefox, Edge |

## 6. Entry & exit criteria

### 6.1 Entry criteria
- Requirements and user stories reviewed and baselined.
- AUT is accessible and stable in the test environment.
- Test data and admin credentials available.

### 6.2 Exit criteria
- 100% of planned test cases executed.
- 100% of Critical/High defects closed; no open Blocker defects.
- ≥ 95% pass rate on the automated regression suite.
- RTM shows every requirement covered by ≥ 1 test case.
- Test Summary Report signed off.

## 7. Test deliverables
- Test plan (this document)
- Test cases (`test-cases.md`) & RTM (`rtm.md`)
- Postman collection + environment (`postman/`)
- Automated API & UI suites with HTML reports (`api_tests/`, `ui_tests/`, `reports/`)
- Defect reports (`bug-reports.md`)
- Test Summary Report (`test-summary-report.md`)

## 8. Roles & responsibilities

| Role | Responsibility |
|------|----------------|
| QA Lead | Strategy, plan, review, RTM, sign-off, metrics |
| QA Engineer | Test design, execution, defect reporting, automation |
| Developer | Fixes, code review of automation, environment support |
| Scrum Master | Facilitates ceremonies, removes blockers |

## 9. Schedule (4-day sprint mapping)

| Sprint | Focus | Target |
|--------|-------|--------|
| 1 | Requirements & user stories | ✅ Done |
| 2 | Test plan, test cases, RTM | Day 1 |
| 3 | Postman API tests | Day 2 |
| 4 | MySQL & SQL validation | Day 2 |
| 5 | API automation (Pytest) | Day 3 |
| 6 | UI automation (Selenium) | Day 3 |
| 7 | CI/CD, docs, summary report | Day 4 |

## 10. Defect management

Defects are tracked with a standard lifecycle:

```
NEW → ASSIGNED → OPEN (in progress) → FIXED → RETEST → CLOSED
                                   ↘ REJECTED / DEFERRED / DUPLICATE
```

**Severity** (impact) and **Priority** (urgency) are assigned to every defect:

| Severity | Meaning |
|----------|---------|
| Blocker | Testing cannot proceed |
| Critical | Core function broken, no workaround |
| Major | Important function impaired, workaround exists |
| Minor | Cosmetic / low impact |

Each defect report includes: ID, title, module, severity, priority, environment,
steps to reproduce, expected vs actual, evidence (screenshot/log), status.

## 11. Risks & mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Shared test env data resets | High | Medium | Create/tear down own test data per run |
| Public AUT downtime | Medium | High | Retry logic; run when stable; local Docker option |
| Flaky UI selectors | Medium | Medium | Stable locators, explicit waits, POM |
| Limited time (4-day plan) | High | Medium | Prioritize smoke + high-risk flows first |

## 12. Metrics (reported in Sprint 7)
- Test case execution % (executed / planned)
- Pass / fail / blocked counts
- Defect density by module
- Defect severity distribution
- Automation coverage (automated / total regression cases)
- Requirement coverage (from RTM)
