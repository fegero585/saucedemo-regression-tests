"""Page object for individual product detail page."""
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class ProductPage(BasePage):
    """Represents a single product detail page."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.product_title = page.locator(".inventory_details_name")
        self.product_price = page.locator(".inventory_details_price")
        self.product_description = page.locator(".inventory_details_desc")
        self.add_to_cart_button = page.locator("button[name='add-to-cart']")
        self.back_button = page.locator("#back-to-products")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def get_product_title(self) -> str:
        """Get the product title."""
        return self.product_title.inner_text()

    def get_product_price(self) -> str:
        """Get the product price."""
        return self.product_price.inner_text()

    def get_product_description(self) -> str:
        """Get the product description."""
        return self.product_description.inner_text()

    def add_to_cart(self) -> None:
        """Click the add to cart button."""
        self.add_to_cart_button.click()

    def expect_add_button_text(self, expected_text: str) -> None:
        """Assert the add to cart button has specific text."""
        expect(self.add_to_cart_button).to_contain_text(expected_text)

    def go_back(self) -> None:
        """Click the back to products button."""
        self.back_button.click()
