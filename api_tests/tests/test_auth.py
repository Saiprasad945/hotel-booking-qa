"""Auth API tests (maps to TC-081, TC-082)."""
import pytest

from api_tests.config.config import config


@pytest.mark.smoke
def test_login_valid_returns_token(client):
    resp = client.post(
        config.AUTH_LOGIN,
        json={"username": config.USERNAME, "password": config.PASSWORD},
    )
    assert resp.status_code == 200
    assert resp.json().get("token"), "Expected a token in the response"


@pytest.mark.negative
@pytest.mark.parametrize(
    "username,password",
    [
        ("admin", "wrongpassword"),
        ("wronguser", "password"),
        ("", ""),
    ],
    ids=["wrong_password", "wrong_username", "empty_creds"],
)
def test_login_invalid_is_rejected(client, username, password):
    resp = client.post(
        config.AUTH_LOGIN, json={"username": username, "password": password}
    )
    assert resp.status_code in (400, 401, 403)
    body = resp.json() if resp.headers.get("content-type", "").startswith("application/json") else {}
    assert not body.get("token"), "No token should be returned for invalid login"
