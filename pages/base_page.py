"""Shared functionality for all page objects."""
from playwright.sync_api import Page


class BasePage:
    """Common helpers that every page object can build on."""

    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str) -> None:
        """Navigate to the given URL."""
        self.page.goto(url)

    def get_title(self) -> str:
        """Get the current page title."""
        return self.page.title()

    def get_url(self) -> str:
        """Get the current page URL."""
        return self.page.url
