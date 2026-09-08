"""Page object for Saucedemo checkout info page (step 1)."""
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Represents the Saucedemo checkout information page (step 1)."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.cancel_button = page.locator("#cancel")
        self.error_message = page.locator("[data-test='error']")

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Fill in the checkout information form."""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_to_overview(self) -> None:
        """Click the continue button to proceed to checkout overview."""
        self.continue_button.click()

    def cancel_checkout(self) -> None:
        """Click the cancel button to return to the cart."""
        self.cancel_button.click()

    def expect_error_message(self, text: str) -> None:
        """Assert that an error message is displayed with specific text."""
        expect(self.error_message).to_contain_text(text)

    def expect_error_not_present(self) -> None:
        """Assert that no error message is displayed."""
        expect(self.error_message).not_to_be_visible()
