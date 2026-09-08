"""Regression tests: cart management."""
import pytest

BACKPACK = "Sauce Labs Backpack"
BIKE_LIGHT = "Sauce Labs Bike Light"


@pytest.mark.cart
def test_cart_is_empty_on_new_session(login_page, inventory_page):
    """A new login session should have an empty cart."""
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    # Cart badge should not be visible if empty
    cart_badge = inventory_page.page.locator(".shopping_cart_badge")
    # Either the badge doesn't exist or is not visible
    badge_count = cart_badge.count()
    assert badge_count == 0 or not cart_badge.is_visible()


@pytest.mark.cart
def test_can_view_empty_cart(login_page, cart_page):
    """User can view cart page when empty."""
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
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
