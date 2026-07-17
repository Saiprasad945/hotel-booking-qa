# UI Automation — Selenium + Page Object Model

Selenium UI automation for the Hotel Booking web app, built with the
**Page Object Model (POM)** pattern.

## Design

```
ui_tests/
├── config.py            # env-driven config (BASE_URL, HEADLESS, waits)
├── conftest.py          # driver fixture + screenshot-on-failure hook
├── pages/
│   ├── base_page.py      # shared Selenium actions (waits, click, type, scroll)
│   └── home_page.py      # HomePage object: rooms + contact form (locators here)
└── tests/
    ├── test_home.py      # homepage loads, rooms listed, navigate to booking
    └── test_contact.py   # contact form valid submit + empty-submit validation
```

Why this is a proper POM framework:
- **Page objects** own all locators and page actions; tests read like plain English
  and never touch raw Selenium calls.
- **BasePage** centralises waits and interactions — explicit `WebDriverWait`,
  scroll-into-view before click, and a JS-click fallback for intercepted elements.
- **Locators** use stable `data-testid` attributes where available.
- **Screenshot on failure** — `conftest.py` captures a PNG into `screenshots/`
  for any failing test (invaluable for debugging CI failures).
- **Headless by default** (CI-friendly); set `HEADLESS=false` to watch locally.
- **webdriver-manager** auto-downloads the ChromeDriver matching the installed Chrome.

## How to run
```bash
source .venv/bin/activate          # from project root

pytest ui_tests/tests              # headless (default)
HEADLESS=false pytest ui_tests/tests   # watch the browser
pytest -m ui                       # all UI tests via marker
```

Reports: `reports/pytest-report.html` · Failure screenshots: `screenshots/`

## Requirements
- Google Chrome installed (any recent version).
- ChromeDriver is fetched automatically by `webdriver-manager` — no manual setup.

## Last verified run
**5 passed** (headless, Chrome 150). Combined with the API suite: **27 passed, 1 xfailed**.
