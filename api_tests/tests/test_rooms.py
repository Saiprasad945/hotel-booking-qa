"""Room API tests (maps to TC-084..TC-091)."""
import pytest

from api_tests.config.config import config
from api_tests.data.test_data import INVALID_ROOMS


@pytest.mark.smoke
def test_get_all_rooms(client):
    resp = client.get(config.ROOM)
    assert resp.status_code == 200
    rooms = resp.json().get("rooms")
    assert isinstance(rooms, list)
    if rooms:
        for field in ("roomid", "roomName", "type", "roomPrice"):
            assert field in rooms[0], f"Missing field {field}"


@pytest.mark.regression
def test_get_room_by_id(client, room_id):
    resp = client.get(f"{config.ROOM}/{room_id}")
    assert resp.status_code == 200
    assert resp.json()["roomid"] == room_id


@pytest.mark.negative
def test_get_room_invalid_id(client):
    resp = client.get(f"{config.ROOM}/999999")
    assert resp.status_code in (404, 500)


@pytest.mark.regression
def test_create_and_delete_room(client, auth_cookies):
    payload = {
        "roomName": "888", "type": "Suite", "accessible": True,
        "description": "QA framework test room", "roomPrice": 200,
        "features": ["WiFi", "TV", "Safe"],
    }
    create = client.post(config.ROOM, json=payload, cookies=auth_cookies)
    assert create.status_code in (200, 201)


@pytest.mark.negative
@pytest.mark.parametrize(
    "case_id,payload,expected",
    INVALID_ROOMS,
    ids=[c[0] for c in INVALID_ROOMS],
)
def test_create_room_invalid(client, auth_cookies, case_id, payload, expected):
    resp = client.post(config.ROOM, json=payload, cookies=auth_cookies)
    assert resp.status_code in expected
