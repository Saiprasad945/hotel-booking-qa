"""Reusable API client. Wraps requests.Session, prepends the base URL,
applies a default timeout, and logs every request and response."""
from api_tests.config.config import config
from api_tests.utils.logger import get_logger


class APIClient:
    def __init__(self, base_url=None):
        self.base_url = base_url or config.BASE_URL
        self.session = requests_session()
        self.log = get_logger()

    def _request(self, method, path, **kwargs):
        url = f"{self.base_url}{path}"
        kwargs.setdefault("timeout", config.TIMEOUT)
        # Log the request (omit noisy internals)
        safe = {k: v for k, v in kwargs.items() if k in ("json", "params", "cookies")}
        self.log.info(f"--> {method} {url} {safe if safe else ''}".rstrip())
        resp = self.session.request(method, url, **kwargs)
        ms = resp.elapsed.total_seconds() * 1000
        self.log.info(f"<-- {resp.status_code} ({ms:.0f} ms)")
        return resp

    def get(self, path, **kwargs):
        return self._request("GET", path, **kwargs)

    def post(self, path, **kwargs):
        return self._request("POST", path, **kwargs)

    def put(self, path, **kwargs):
        return self._request("PUT", path, **kwargs)

    def delete(self, path, **kwargs):
        return self._request("DELETE", path, **kwargs)


def requests_session():
    """Session with retries for transient connection/5xx errors.
    read=0 so genuine read-timeouts (e.g. BUG-03 server hang) are not retried."""
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry

    session = requests.Session()
    retry = Retry(
        total=2, connect=2, read=0, backoff_factor=0.5,
        status_forcelist=[502, 503, 504],
        allowed_methods=["GET", "POST", "PUT", "DELETE"],
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session
