"""Contact form UI tests (maps to TC-027, TC-029..TC-034)."""
import pytest

from ui_tests.pages.home_page import HomePage


@pytest.mark.ui
@pytest.mark.smoke
def test_contact_form_valid_submission(driver):
    home = HomePage(driver).load()
    home.fill_contact(
        name="Sai Kumar",
        email="sai.kumar@example.com",
        phone="01234567890",
        subject="UI automation enquiry",
        description="This is a Selenium UI automation test message over 20 chars.",
    )
    home.submit_contact()
    assert home.contact_success_shown("Sai Kumar"), (
        "Expected the 'Thanks for getting in touch' confirmation"
    )


@pytest.mark.ui
@pytest.mark.negative
def test_contact_form_validation_on_empty_submit(driver):
    home = HomePage(driver).load()
    home.submit_empty_contact()
    errors = home.validation_errors()
    assert errors, "Expected validation error messages on empty submit"
