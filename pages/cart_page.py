"""Page object for Saucedemo shopping cart page."""
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

CART_URL = "https://www.saucedemo.com/cart.html"


class CartPage(BasePage):
    """Represents the Saucedemo shopping cart page."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_items_container = page.locator(".cart_contents_container")
        self.checkout_button = page.locator("#checkout")
        self.continue_shopping_button = page.locator("#continue-shopping")

    def load(self) -> None:
        """Navigate to the cart page."""
        self.goto(CART_URL)

    def cart_item(self, product_name: str):
        """Returns the cart item row for a given product."""
        return self.page.locator(".cart_item").filter(has_text=product_name)

    def expect_item_present(self, product_name: str) -> None:
        """Assert that a product is in the cart."""
        expect(self.cart_item(product_name)).to_be_visible()

    def expect_item_not_present(self, product_name: str) -> None:
        """Assert that a product is NOT in the cart."""
        expect(self.cart_item(product_name)).not_to_be_visible()

    def get_item_quantity(self, product_name: str) -> str:
        """Get the quantity of a specific item in the cart."""
        item = self.cart_item(product_name)
        return item.locator(".cart_quantity").inner_text()

    def get_item_price(self, product_name: str) -> str:
        """Get the price of a specific item in the cart."""
        item = self.cart_item(product_name)
        return item.locator(".inventory_item_price").inner_text()

    def remove_item(self, product_name: str) -> None:
        """Remove a product from the cart."""
        item = self.cart_item(product_name)
        item.get_by_role("button", name="Remove").click()

    def checkout(self) -> None:
        """Click the checkout button."""
        self.checkout_button.click()

    def continue_shopping(self) -> None:
        """Click the continue shopping button."""
        self.continue_shopping_button.click()

    def is_empty(self) -> bool:
        """Check if the cart is empty."""
        cart_items = self.page.locator(".cart_item")
        return cart_items.count() == 0
