"""Page object for Saucedemo checkout overview page (step 2)."""
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    """Represents the Saucedemo checkout overview page (step 2)."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.finish_button = page.locator("#finish")
        self.cancel_button = page.locator("#cancel")
        self.item_total = page.locator("[data-test='subtotal-label']")
        self.tax = page.locator("[data-test='tax-label']")
        self.total = page.locator("[data-test='total-label']")

    def get_item_total(self) -> float:
        """Get the item subtotal as a float."""
        text = self.item_total.inner_text()
        # Extract price from "Item total: $XX.XX"
        return float(text.split("$")[1])

    def get_tax(self) -> float:
        """Get the tax amount as a float."""
        text = self.tax.inner_text()
        # Extract price from "Tax: $X.XX"
        return float(text.split("$")[1])

    def get_total(self) -> float:
        """Get the total amount as a float."""
        text = self.total.inner_text()
        # Extract price from "Total: $XXX.XX"
        return float(text.split("$")[1])

    def finish_checkout(self) -> None:
        """Click the finish button to complete the order."""
        self.finish_button.click()

    def cancel_checkout(self) -> None:
        """Click the cancel button to return to the cart."""
        self.cancel_button.click()

    def verify_totals_calculation(self) -> bool:
        """Verify that item_total + tax = total."""
        item_total = self.get_item_total()
        tax = self.get_tax()
        total = self.get_total()
        
        # Account for floating point precision
        calculated_total = round(item_total + tax, 2)
        return calculated_total == total
