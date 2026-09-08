"""Regression tests: critical flows under mobile device emulation.

These tests use the same fixtures as the desktop suite. Emulation is applied
via pytest-playwright's built-in --device flag, e.g.:

    pytest -m mobile --device="iPhone 12"
    pytest -m mobile --device="Pixel 5"
"""
import pytest

BACKPACK = "Sauce Labs Backpack"


@pytest.mark.mobile
@pytest.mark.smoke
def test_login_on_mobile(login_page, inventory_page):
    """User can log in and reach inventory on a mobile viewport."""
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in inventory_page.get_url()


@pytest.mark.mobile
def test_add_to_cart_on_mobile(logged_in_user):
    """User can add a product to the cart on a mobile viewport."""
    logged_in_user.add_product_to_cart(BACKPACK)
    logged_in_user.expect_cart_count("1")
