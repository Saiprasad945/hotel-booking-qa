"""HomePage page object — hotel homepage: room listing + contact form.
Locators are based on the live DOM (data-testid attributes on the contact form)."""
from selenium.webdriver.common.by import By

from ui_tests.pages.base_page import BasePage


class HomePage(BasePage):
    # --- locators ---
    BOOK_NOW_LINKS = (By.XPATH, "//a[normalize-space()='Book now']")
    HERO_BOOK_NOW = (By.XPATH, "//a[normalize-space()='Book Now']")

    CONTACT_NAME = (By.CSS_SELECTOR, "[data-testid='ContactName']")
    CONTACT_EMAIL = (By.CSS_SELECTOR, "[data-testid='ContactEmail']")
    CONTACT_PHONE = (By.CSS_SELECTOR, "[data-testid='ContactPhone']")
    CONTACT_SUBJECT = (By.CSS_SELECTOR, "[data-testid='ContactSubject']")
    CONTACT_DESCRIPTION = (By.CSS_SELECTOR, "[data-testid='ContactDescription']")
    SUBMIT_BTN = (By.XPATH, "//button[normalize-space()='Submit']")
    ALERT_DANGER = (By.CSS_SELECTOR, ".alert-danger")

    def load(self):
        return self.open("/")

    # --- rooms ---
    def room_count(self):
        return self.count(self.BOOK_NOW_LINKS)

    def go_to_first_room(self):
        self.click(self.BOOK_NOW_LINKS)

    # --- contact form ---
    def fill_contact(self, name, email, phone, subject, description):
        self.type(self.CONTACT_NAME, name)
        self.type(self.CONTACT_EMAIL, email)
        self.type(self.CONTACT_PHONE, phone)
        self.type(self.CONTACT_SUBJECT, subject)
        self.type(self.CONTACT_DESCRIPTION, description)
        return self

    def submit_contact(self):
        self.click(self.SUBMIT_BTN)

    def submit_empty_contact(self):
        """Click submit without filling anything to trigger validation."""
        self.click(self.SUBMIT_BTN)

    def contact_success_shown(self, name):
        # After success the platform shows "Thanks for getting in touch {name}!"
        return self.is_visible(
            (By.XPATH, "//*[contains(text(),'Thanks for getting in touch')]"),
            timeout=10,
        )

    def validation_errors(self):
        """Return the list of validation error messages shown."""
        return [e.text for e in self.driver.find_elements(*self.ALERT_DANGER)]
