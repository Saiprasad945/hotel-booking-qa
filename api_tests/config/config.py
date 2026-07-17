"""Central configuration. Values come from environment variables with sane
defaults, so the same suite runs locally and in CI without code changes."""
import os


class Config:
    BASE_URL = os.getenv("BASE_URL", "https://automationintesting.online")
    USERNAME = os.getenv("ADMIN_USER", "admin")
    PASSWORD = os.getenv("ADMIN_PASS", "password")
    TIMEOUT = int(os.getenv("HTTP_TIMEOUT", "15"))

    # Endpoint paths (kept in one place so a path change is a one-line edit)
    AUTH_LOGIN = "/api/auth/login"
    ROOM = "/api/room"
    BOOKING = "/api/booking"
    MESSAGE = "/api/message"
    BRANDING = "/api/branding"


config = Config()
