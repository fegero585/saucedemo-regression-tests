"""Page object for Saucedemo login page."""
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

LOGIN_URL = "https://www.saucedemo.com/"


class LoginPage(BasePage):
    """Represents the Saucedemo login page."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    def load(self) -> None:
        """Navigate to the login page."""
        self.goto(LOGIN_URL)

    def login(self, username: str, password: str) -> None:
        """
        Perform login with the given credentials.
        
        Args:
            username: The username to login with
            password: The password to login with
        """
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def expect_error_message(self, expected_text: str) -> None:
        """Assert that an error message appears with the expected text."""
        expect(self.error_message).to_contain_text(expected_text)

    def expect_error_not_present(self) -> None:
        """Assert that no error message is displayed."""
        expect(self.error_message).not_to_be_visible()
