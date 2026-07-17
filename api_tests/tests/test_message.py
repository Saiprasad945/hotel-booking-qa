"""Message API tests (maps to TC-100, TC-101)."""
import pytest

from api_tests.config.config import config
from api_tests.data.test_data import BASE_MESSAGE, INVALID_MESSAGES


@pytest.mark.smoke
def test_create_message_valid(client):
    resp = client.post(config.MESSAGE, json=BASE_MESSAGE)
    assert resp.status_code in (200, 201)
    assert resp.json().get("success") is True


@pytest.mark.negative
@pytest.mark.parametrize(
    "case_id,payload,expected",
    INVALID_MESSAGES,
    ids=[c[0] for c in INVALID_MESSAGES],
)
def test_create_message_invalid(client, case_id, payload, expected):
    resp = client.post(config.MESSAGE, json=payload)
    assert resp.status_code in expected
