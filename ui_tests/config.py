"""UI test configuration (env-driven)."""
import os


class UIConfig:
    BASE_URL = os.getenv("BASE_URL", "https://automationintesting.online")
    # HEADLESS=false to watch the browser locally; default headless for CI.
    HEADLESS = os.getenv("HEADLESS", "true").lower() != "false"
    EXPLICIT_WAIT = int(os.getenv("UI_WAIT", "15"))
    WINDOW = (1400, 1000)


ui_config = UIConfig()
