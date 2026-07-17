"""Branding API tests (maps to TC-105)."""
import pytest

from api_tests.config.config import config


@pytest.mark.regression
def test_get_branding(client):
    resp = client.get(config.BRANDING)
    assert resp.status_code == 200
    body = resp.json()
    assert "name" in body
    assert "contact" in body
