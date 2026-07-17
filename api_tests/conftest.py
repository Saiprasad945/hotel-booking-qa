"""Shared pytest fixtures for the API automation suite."""
import pytest

from api_tests.config.config import config
from api_tests.utils.api_client import APIClient
from api_tests.utils.logger import get_logger

log = get_logger()


@pytest.fixture(scope="session")
def client():
    """An unauthenticated API client, shared across the session."""
    return APIClient()


@pytest.fixture(scope="session")
def auth_token(client):
    """Log in once and return the admin auth token."""
    resp = client.post(
        config.AUTH_LOGIN,
        json={"username": config.USERNAME, "password": config.PASSWORD},
    )
    assert resp.status_code == 200, f"Login failed: {resp.status_code}"
    token = resp.json().get("token")
    assert token, "No token returned from login"
    return token


@pytest.fixture(scope="session")
def auth_cookies(auth_token):
    """Cookies dict carrying the token for protected endpoints."""
    return {"token": auth_token}


@pytest.fixture(scope="session")
def room_id(client):
    """Return an existing room id from the live API (skip if none)."""
    resp = client.get(config.ROOM)
    rooms = resp.json().get("rooms", [])
    if not rooms:
        pytest.skip("No rooms available in the environment")
    return rooms[0]["roomid"]


@pytest.fixture
def created_booking(client, room_id, auth_cookies):
    """Create a booking, yield its id, then clean it up (create/teardown)."""
    payload = {
        "roomid": room_id,
        "firstname": "Sai", "lastname": "Tester", "depositpaid": True,
        "email": "sai@example.com", "phone": "01234567890",
        "bookingdates": {"checkin": "2027-07-01", "checkout": "2027-07-04"},
    }
    resp = client.post(config.BOOKING, json=payload)
    assert resp.status_code in (200, 201), f"Setup booking failed: {resp.status_code}"
    booking_id = resp.json()["bookingid"]
    yield booking_id
    # teardown — delete the booking so the suite is repeatable
    client.delete(f"{config.BOOKING}/{booking_id}", cookies=auth_cookies)
