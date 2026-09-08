"""Page object for Saucedemo inventory/products page."""
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

INVENTORY_URL = "https://www.saucedemo.com/inventory.html"


class InventoryPage(BasePage):
    """Represents the Saucedemo inventory page (product listing)."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def load(self) -> None:
        """Navigate to the inventory page."""
        self.goto(INVENTORY_URL)

    def product_card(self, product_name: str):
        """Returns the product card for a given product name."""
        return self.page.locator("div.inventory_item").filter(has_text=product_name)

    def get_product_price(self, product_name: str) -> str:
        """Get the price of a specific product."""
        card = self.product_card(product_name)
        return card.locator(".inventory_item_price").inner_text()

    def click_product(self, product_name: str) -> None:
        """Click on a product to view its details."""
        card = self.product_card(product_name)
        # Use .first to avoid strict mode violation (multiple links with same name)
        card.get_by_role("link", name=product_name).first.click()

    def add_product_to_cart(self, product_name: str) -> None:
        """Add a product to the cart."""
        card = self.product_card(product_name)
        card.get_by_role("button", name="Add to cart").click()

    def remove_product_from_cart(self, product_name: str) -> None:
        """Remove a product from the cart."""
        card = self.product_card(product_name)
        card.get_by_role("button", name="Remove").click()

    def get_cart_count(self) -> str:
        """Get the current cart item count."""
        return self.cart_badge.inner_text()

    def expect_cart_count(self, expected: str) -> None:
        """Assert the cart count matches the expected value."""
        expect(self.cart_badge).to_contain_text(expected)

    def open_cart(self) -> None:
        """Click the cart icon to navigate to the cart page."""
        self.cart_link.click()

    def sort_by(self, sort_option: str) -> None:
        """Sort the product list by the specified option.

        Args:
            sort_option: One of 'az', 'za', 'lohi', 'hilo'
        """
        # Find the sort dropdown by class name
        sort_dropdown = self.page.locator("select.product_sort_container")
        sort_dropdown.select_option(sort_option)

    def get_product_names(self) -> list[str]:
        """Get all product names in on-screen order (row 1 left-to-right, then row 2, ...)."""
        return self.page.locator(".inventory_item_name").all_inner_texts()

    def get_product_prices(self) -> list[float]:
        """Get all product prices as floats, in on-screen order."""
        prices = self.page.locator(".inventory_item_price").all_inner_texts()
        return [float(price.replace("$", "")) for price in prices]
