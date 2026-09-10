"""Shared functionality for all API clients."""
import logging
import requests

DEFAULT_TIMEOUT = 10
logger = logging.getLogger("api")


class BaseClient:
    """Thin wrapper around requests.Session that every API client builds on."""

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

    def _request(self, method: str, path: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{path}"
        response = self.session.request(method, url, timeout=DEFAULT_TIMEOUT, **kwargs)

        logger.info("--> %s %s", method, url)
        if "params" in kwargs:
            logger.info("    query params: %s", kwargs["params"])
        if "json" in kwargs:
            logger.info("    request body: %s", kwargs["json"])
        logger.info("<-- %s %s", response.status_code, response.reason)
        logger.info("    response body: %s", response.text)

        return response

    def get(self, path: str, **kwargs) -> requests.Response:
        return self._request("GET", path, **kwargs)

    def post(self, path: str, **kwargs) -> requests.Response:
        return self._request("POST", path, **kwargs)

    def put(self, path: str, **kwargs) -> requests.Response:
        return self._request("PUT", path, **kwargs)

    def patch(self, path: str, **kwargs) -> requests.Response:
        return self._request("PATCH", path, **kwargs)

    def delete(self, path: str, **kwargs) -> requests.Response:
        return self._request("DELETE", path, **kwargs)
