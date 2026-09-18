"""Page object for Saucedemo checkout complete page (order confirmation)."""
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    """Represents the Saucedemo order confirmation page."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.confirmation_header = page.locator(".complete-header")
        self.back_home_button = page.locator("#back-to-products")

    def expect_order_confirmed(self) -> None:
        """Assert the order confirmation message is displayed."""
        expect(self.confirmation_header).to_have_text("Thank you for your order!")

    def back_home(self) -> None:
        """Click Back Home to return to the inventory page."""
        self.back_home_button.click()
