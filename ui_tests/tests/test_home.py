"""Homepage UI tests (maps to TC-001, TC-003)."""
import pytest

from ui_tests.pages.home_page import HomePage


@pytest.mark.ui
@pytest.mark.smoke
def test_homepage_loads(driver):
    home = HomePage(driver).load()
    assert "restful-booker" in driver.title.lower()


@pytest.mark.ui
@pytest.mark.smoke
def test_rooms_are_listed(driver):
    home = HomePage(driver).load()
    assert home.room_count() >= 1, "Expected at least one bookable room"


@pytest.mark.ui
@pytest.mark.regression
def test_navigate_to_room_booking(driver):
    home = HomePage(driver).load()
    home.go_to_first_room()
    assert "/reservation/" in driver.current_url, (
        f"Expected reservation URL, got {driver.current_url}"
    )
