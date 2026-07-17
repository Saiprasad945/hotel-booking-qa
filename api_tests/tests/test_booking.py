"""Booking API tests (maps to TC-093..TC-099)."""
import pytest
import requests

from api_tests.config.config import config
from api_tests.data.test_data import INVALID_BOOKINGS


@pytest.mark.smoke
def test_create_booking_valid(client, room_id, auth_cookies):
    payload = {
        "roomid": room_id,
        "firstname": "Sai", "lastname": "Tester", "depositpaid": True,
        "email": "sai@example.com", "phone": "01234567890",
        "bookingdates": {"checkin": "2027-08-01", "checkout": "2027-08-05"},
    }
    resp = client.post(config.BOOKING, json=payload)
    assert resp.status_code in (200, 201)
    body = resp.json()
    assert body.get("bookingid"), "Expected a bookingid"
    assert body["firstname"] == "Sai"
    # cleanup
    client.delete(f"{config.BOOKING}/{body['bookingid']}", cookies=auth_cookies)


@pytest.mark.negative
@pytest.mark.parametrize(
    "case_id,payload,expected",
    INVALID_BOOKINGS,
    ids=[c[0] for c in INVALID_BOOKINGS],
)
def test_create_booking_invalid(client, room_id, case_id, payload, expected):
    body = {"roomid": room_id, **payload}
    resp = client.post(config.BOOKING, json=body)
    assert resp.status_code in expected


@pytest.mark.negative
@pytest.mark.xfail(
    reason="BUG-03: server hangs (no response) instead of returning 400 "
           "when bookingdates is missing",
    raises=requests.exceptions.RequestException,
    strict=False,
)
def test_booking_missing_dates_should_return_400(client, room_id):
    """A booking with no bookingdates SHOULD be rejected with 400.
    Currently the server hangs (BUG-03), so this is an expected failure."""
    body = {
        "roomid": room_id, "firstname": "Sai", "lastname": "Tester",
        "depositpaid": True, "email": "sai@example.com", "phone": "01234567890",
    }
    resp = client.post(config.BOOKING, json=body)
    assert resp.status_code == 400


@pytest.mark.regression
def test_get_booking_by_id(client, created_booking, auth_cookies):
    resp = client.get(f"{config.BOOKING}/{created_booking}", cookies=auth_cookies)
    assert resp.status_code == 200
    assert "firstname" in resp.json()


@pytest.mark.negative
def test_delete_booking_without_auth(client, created_booking):
    resp = client.delete(f"{config.BOOKING}/{created_booking}")
    assert resp.status_code in (401, 403)


@pytest.mark.regression
def test_full_booking_lifecycle(client, room_id, auth_cookies):
    """Create -> read -> delete -> verify gone (end-to-end CRUD)."""
    payload = {
        "roomid": room_id,
        "firstname": "Life", "lastname": "Cycle", "depositpaid": False,
        "email": "life@example.com", "phone": "01234567890",
        "bookingdates": {"checkin": "2027-09-01", "checkout": "2027-09-03"},
    }
    created = client.post(config.BOOKING, json=payload)
    assert created.status_code in (200, 201)
    bid = created.json()["bookingid"]

    read = client.get(f"{config.BOOKING}/{bid}", cookies=auth_cookies)
    assert read.status_code == 200

    deleted = client.delete(f"{config.BOOKING}/{bid}", cookies=auth_cookies)
    assert deleted.status_code in (200, 201, 202)

    gone = client.get(f"{config.BOOKING}/{bid}", cookies=auth_cookies)
    assert gone.status_code in (404, 500)
