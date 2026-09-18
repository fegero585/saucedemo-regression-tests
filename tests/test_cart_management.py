"""Regression tests: cart management."""
import pytest
from playwright.sync_api import expect

BACKPACK = "Sauce Labs Backpack"
BIKE_LIGHT = "Sauce Labs Bike Light"


@pytest.mark.cart
def test_cart_is_empty_on_new_session(logged_in_user):
    """A new login session should have an empty cart."""
    # Badge is either absent or hidden when the cart is empty. The fixture has
    # already waited for the inventory, so this can't pass on an unloaded page.
    expect(logged_in_user.cart_badge).not_to_be_visible()


@pytest.mark.cart
def test_can_view_empty_cart(logged_in_user, cart_page):
    """User can view cart page when empty."""
    cart_page.load()
    assert cart_page.is_empty()


@pytest.mark.cart
def test_continue_shopping_from_cart(logged_in_user, cart_page):
    """User can click 'Continue Shopping' to return to inventory."""
    logged_in_user.add_product_to_cart(BACKPACK)
    logged_in_user.open_cart()
    
    cart_page.continue_shopping()
    # Should be back on inventory page
    assert "inventory" in logged_in_user.page.url


@pytest.mark.cart
def test_cart_persists_after_leaving_page(logged_in_user, cart_page):
    """Cart contents persist when navigating away and back."""
    logged_in_user.add_product_to_cart(BACKPACK)
    logged_in_user.add_product_to_cart(BIKE_LIGHT)
    logged_in_user.open_cart()
    
    cart_page.continue_shopping()
    logged_in_user.open_cart()
    
    cart_page.expect_item_present(BACKPACK)
    cart_page.expect_item_present(BIKE_LIGHT)


@pytest.mark.cart
def test_cart_persists_after_page_reload(logged_in_user, cart_page):
    """Cart contents survive a full page reload."""
    logged_in_user.add_product_to_cart(BACKPACK)
    logged_in_user.page.reload()
    logged_in_user.expect_loaded()

    logged_in_user.expect_cart_count("1")
    logged_in_user.open_cart()
    cart_page.expect_item_present(BACKPACK)
