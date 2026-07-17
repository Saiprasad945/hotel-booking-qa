# API Automation Framework — Pytest + Requests

A layered API test automation framework for the Restful Booker Platform API.

## Design (why it's a framework, not a script)

```
api_tests/
├── config/config.py     # env-driven config + endpoint paths (one place to change)
├── utils/
│   ├── api_client.py     # reusable requests wrapper: base URL, timeout, retries, logging
│   └── logger.py         # console + file logging (logs/api_tests.log)
├── data/test_data.py     # test data separated from logic (data-driven tests)
├── conftest.py           # shared fixtures: client, auth token, room_id, create/teardown
└── tests/                # test modules by feature
    ├── test_auth.py
    ├── test_rooms.py
    ├── test_booking.py
    ├── test_message.py
    └── test_branding.py
```

Key framework features:
- **Reusable API client** wrapping `requests.Session` with base URL, default timeout,
  connection retries (transient 5xx / connect errors) and request/response logging.
- **Fixtures** (`conftest.py`) for session-scoped auth token capture and
  create-then-teardown of test data (repeatable, no leftover records).
- **Data-driven tests** via `@pytest.mark.parametrize` fed from `data/test_data.py`.
- **Markers**: `smoke`, `regression`, `negative` — run subsets on demand.
- **HTML reporting** via `pytest-html` and file logging.
- **Defect tracking in code**: a known server bug is captured as an `xfail`
  test (see BUG-03) so it is tracked until fixed without breaking the build.

## How to run
```bash
source .venv/bin/activate          # from project root

pytest                             # everything, with HTML report
pytest -m smoke                    # smoke suite only
pytest -m negative                 # negative tests only
pytest api_tests/tests/test_booking.py   # one module
```

Reports: `reports/pytest-report.html` · Logs: `logs/api_tests.log`

## Configuration
All settings come from environment variables (with defaults), so the same suite
runs locally and in CI:

| Variable | Default |
|----------|---------|
| `BASE_URL` | https://automationintesting.online |
| `ADMIN_USER` | admin |
| `ADMIN_PASS` | password |
| `HTTP_TIMEOUT` | 15 |

## Last verified run
**22 passed, 1 xfailed** (BUG-03 documented), exit code 0.
