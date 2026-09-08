"""Shared pytest fixtures for Saucedemo tests.

pytest-playwright already provides the `page` fixture (a fresh browser page
per test). These fixtures build page objects on top of it.

Mobile device emulation is supported via pytest-playwright's built-in
--device flag (e.g. `pytest -m mobile --device="iPhone 12"`), so no
extra fixtures are needed to apply it.
"""
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage

# Standard Saucedemo credentials
STANDARD_USER = "standard_user"
STANDARD_PASSWORD = "secret_sauce"


@pytest.fixture
def login_page(page):
    """Create a LoginPage fixture."""
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    """Create an InventoryPage fixture."""
    return InventoryPage(page)


@pytest.fixture
def product_page(page):
    """Create a ProductPage fixture."""
    return ProductPage(page)


@pytest.fixture
def cart_page(page):
    """Create a CartPage fixture."""
    return CartPage(page)


@pytest.fixture
def checkout_page(page):
    """Create a CheckoutPage fixture."""
    return CheckoutPage(page)


@pytest.fixture
def checkout_overview_page(page):
    """Create a CheckoutOverviewPage fixture."""
    return CheckoutOverviewPage(page)


@pytest.fixture
def logged_in_user(login_page, inventory_page):
    """
    Fixture that logs in a standard user and navigates to inventory.
    Returns the inventory_page, ready to use.
    """
    login_page.load()
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)
    return inventory_page
