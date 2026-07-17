"""BasePage — common Selenium actions shared by all page objects.
Every page object inherits these, so tests never touch raw Selenium calls."""
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ui_tests.config import ui_config


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, ui_config.EXPLICIT_WAIT)

    # --- navigation ---
    def open(self, path=""):
        self.driver.get(f"{ui_config.BASE_URL}{path}")
        return self

    @property
    def current_url(self):
        return self.driver.current_url

    # --- element interactions (with explicit waits) ---
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        # Scroll into view (elements below the fold get click-intercepted otherwise)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", el
        )
        try:
            el.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", el)

    def type(self, locator, text):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", el
        )
        el.clear()
        el.send_keys(text)

    def text_of(self, locator):
        return self.find(locator).text

    def is_visible(self, locator, timeout=None):
        try:
            wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:  # noqa: BLE001
            return False

    def count(self, locator):
        return len(self.driver.find_elements(*locator))

    def wait_for_text(self, text, timeout=None):
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return wait.until(
            lambda d: text.lower() in d.find_element("tag name", "body").text.lower()
        )
