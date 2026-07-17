"""Test data for data-driven (parametrized) tests.

Each tuple is (case_id, payload, expected_status_options). Keeping data
separate from test logic lets us add cases without touching the test code."""

# --- Booking negative cases ---
# Valid room id is injected by the test at runtime (see test_booking.py).
INVALID_BOOKINGS = [
    (
        "checkout_before_checkin",
        {
            "firstname": "Sai", "lastname": "Tester", "depositpaid": True,
            "email": "sai@example.com", "phone": "01234567890",
            "bookingdates": {"checkin": "2027-05-10", "checkout": "2027-05-05"},
        },
        (400, 409, 500),
    ),
    (
        "missing_firstname",
        {
            "lastname": "Tester", "depositpaid": True,
            "email": "sai@example.com", "phone": "01234567890",
            "bookingdates": {"checkin": "2027-06-01", "checkout": "2027-06-03"},
        },
        (400,),
    ),
    # NOTE: the "missing bookingdates entirely" case is covered by a dedicated
    # xfail test in test_booking.py because the server HANGS on it (see BUG-03),
    # which is not a clean status-code assertion.
]

# --- Message negative cases ---
BASE_MESSAGE = {
    "name": "Sai Test", "email": "sai@example.com", "phone": "01234567890",
    "subject": "API enquiry test",
    "description": "This is a QA automation test message over twenty chars.",
}

INVALID_MESSAGES = [
    ("invalid_email", {**BASE_MESSAGE, "email": "not-an-email"}, (400,)),
    ("empty_name", {**BASE_MESSAGE, "name": ""}, (400,)),
    ("short_subject", {**BASE_MESSAGE, "subject": "Hi"}, (400,)),
    ("short_description", {**BASE_MESSAGE, "description": "too short"}, (400,)),
]

# --- Room negative cases (require auth) ---
INVALID_ROOMS = [
    ("missing_roomName", {"type": "Double", "accessible": True, "roomPrice": 150}, (400,)),
    ("non_numeric_price",
     {"roomName": "901", "type": "Double", "accessible": True,
      "roomPrice": "free", "features": []}, (400,)),
]
