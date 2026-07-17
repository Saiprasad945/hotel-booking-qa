# 🏨 Hotel Booking — End-to-End QA Project

[![QA CI](https://github.com/YOUR_USERNAME/hotel-booking-qa/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/hotel-booking-qa/actions/workflows/ci.yml)

A complete quality-assurance project for a hotel booking application, spanning
**manual testing, API testing, SQL data validation, API automation, UI automation,
and CI/CD** — the full QA lifecycle in one repository.

> **Application Under Test:** [automationintesting.online](https://automationintesting.online)
> (the Restful Booker Platform — a real hotel booking web app + REST API).

---

## 🎯 What this project demonstrates

| Area | Tools & techniques |
|------|--------------------|
| **Manual testing** | Requirements, user stories, test plan, 110 test cases, RTM, defect reports |
| **API testing** | Postman collection + Newman (16 requests, 28 assertions) |
| **API automation** | Python · Requests · Pytest · fixtures · data-driven · HTML reports |
| **Database validation** | SQL · schema with FKs · API↔DB consistency checks |
| **UI automation** | Selenium · Page Object Model · screenshot-on-failure |
| **CI/CD** | GitHub Actions (API + SQL + Postman + UI jobs) |
| **Process** | Agile sprints, defect lifecycle, test metrics, traceability |

## 📊 Results

| Suite | Result |
|-------|--------|
| Pytest (API + UI) | **27 passed, 1 xfailed** |
| Postman / Newman | **28 / 28 assertions passed** |
| SQL data validation | **12 / 12 integrity checks passed** |
| Requirement coverage | **29 / 29 (100%)** |
| Defects found | **3** (1 Critical, 1 Major, 1 Minor) |

## 🏗️ Architecture

```
                    ┌─────────────────────────────┐
                    │  Application Under Test       │
                    │  automationintesting.online   │
                    │      (UI  +  REST API)        │
                    └──────────────┬──────────────┘
                                   │
      ┌───────────────┬───────────┼───────────┬───────────────┐
      ▼               ▼           ▼           ▼               ▼
  Manual QA       Postman     Pytest API   SQL (SQLite)   Selenium UI
  (docs/)        (postman/)   (api_tests/) (db_validation) (ui_tests/)
      │               │           │           │               │
      └───────────────┴───────────┴─────┬─────┴───────────────┘
                                         ▼
                              GitHub Actions CI
                              (.github/workflows)
```

## 📁 Repository structure

```
hotel-booking-qa/
├── docs/            # Requirements, user stories, test plan, 110 test cases,
│                    #   RTM, defect reports, test summary report
├── postman/         # Postman collection + environment (Newman-ready)
├── api_tests/       # Pytest + Requests API automation framework
├── db_validation/   # SQL schema + API↔DB validation (SQLite; MySQL-compatible)
├── ui_tests/        # Selenium Page Object Model UI framework
├── .github/         # GitHub Actions CI workflow
├── requirements.txt
└── README.md
```

## 🚀 How to run

### Setup (once)
```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### API automation (Pytest)
```bash
pytest -m "not ui"                 # API tests + HTML report
```

### SQL data validation
```bash
python db_validation/build_db.py   # build DB + load live rooms from API
python db_validation/validate.py   # run integrity checks
```

### UI automation (Selenium)
```bash
pytest -m ui                       # headless (default)
HEADLESS=false pytest -m ui        # watch the browser
```

### Postman API tests (Newman)
```bash
npm install -g newman newman-reporter-htmlextra
newman run postman/HotelBooking.postman_collection.json \
  -e postman/HotelBooking.postman_environment.json \
  -r cli,htmlextra --reporter-htmlextra-export reports/newman-report.html
```

Reports land in `reports/` · logs in `logs/` · failure screenshots in `screenshots/`.

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [Requirements](docs/requirements.md) | 29 functional + 5 non-functional requirements |
| [User Stories](docs/user-stories.md) | 15 stories with acceptance criteria |
| [Test Plan](docs/test-plan.md) | Strategy, scope, entry/exit criteria, defect lifecycle |
| [Test Cases](docs/test-cases.md) | 110 test cases (smoke / regression / negative) |
| [RTM](docs/rtm.md) | Requirements Traceability Matrix |
| [Defect Reports](docs/bug-reports.md) | 3 documented defects |
| [Test Summary Report](docs/test-summary-report.md) | Metrics & release assessment |

## 🐞 Key defects found by this project

- **BUG-03 (Critical):** the booking endpoint **hangs indefinitely** on a request
  with missing dates instead of returning `400` — an availability/DoS risk.
  Found by the Pytest suite and tracked in code as an `xfail`.
- **BUG-01 (Major):** duplicate room numbers exist in the dataset (no uniqueness
  constraint). Found by SQL data validation.
- **BUG-02 (Minor):** the API returns `409` (not `400`) for an invalid date range.

## ✅ Project progress

- [x] Sprint 1 — Requirements & user stories
- [x] Sprint 2 — Test plan, 110 test cases & RTM
- [x] Sprint 3 — Postman API tests
- [x] Sprint 4 — SQL validation (SQLite; MySQL-compatible)
- [x] Sprint 5 — API automation (Python + Pytest)
- [x] Sprint 6 — UI automation (Selenium + POM)
- [x] Sprint 7 — CI/CD, documentation & summary report
