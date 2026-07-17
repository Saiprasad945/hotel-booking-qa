"""Selenium fixtures + screenshot-on-failure hook."""
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ui_tests.config import ui_config

SCREENSHOT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "screenshots"
)
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


@pytest.fixture
def driver():
    opts = Options()
    if ui_config.HEADLESS:
        opts.add_argument("--headless=new")
    opts.add_argument(f"--window-size={ui_config.WINDOW[0]},{ui_config.WINDOW[1]}")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    # Selenium Manager auto-resolves a matching ChromeDriver (reliable in CI).
    driver = webdriver.Chrome(options=opts)
    driver.implicitly_wait(2)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Save a screenshot when a test that uses the driver fixture fails."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver")
        if drv is not None:
            path = os.path.join(SCREENSHOT_DIR, f"{item.name}.png")
            try:
                drv.save_screenshot(path)
                print(f"\n📸 Screenshot saved: {path}")
            except Exception:  # noqa: BLE001
                pass
