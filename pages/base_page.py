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

    def has_horizontal_scroll(self) -> bool:
        """True if content is wider than the viewport.

        A snapshot - only call it after waiting for the page to render.
        """
        return self.page.evaluate(
            "document.documentElement.scrollWidth > document.documentElement.clientWidth"
        )
