"""Regression tests: adding products to cart."""
import pytest

BACKPACK = "Sauce Labs Backpack"
BIKE_LIGHT = "Sauce Labs Bike Light"
ONESIE = "Sauce Labs Onesie"


@pytest.mark.smoke
@pytest.mark.cart
def test_add_single_product_to_cart(logged_in_user, cart_page):
    """User can add a single product to cart."""
    logged_in_user.add_product_to_cart(BACKPACK)
    logged_in_user.expect_cart_count("1")
    
    logged_in_user.open_cart()
    cart_page.expect_item_present(BACKPACK)


@pytest.mark.cart
def test_add_multiple_products_to_cart(logged_in_user, cart_page):
    """User can add multiple products to cart."""
    logged_in_user.add_product_to_cart(BACKPACK)
    logged_in_user.add_product_to_cart(BIKE_LIGHT)
    logged_in_user.add_product_to_cart(ONESIE)
    
    logged_in_user.expect_cart_count("3")
    
    logged_in_user.open_cart()
    cart_page.expect_item_present(BACKPACK)
    cart_page.expect_item_present(BIKE_LIGHT)
    cart_page.expect_item_present(ONESIE)


@pytest.mark.cart
def test_cart_count_updates_on_add(logged_in_user):
    """Cart count updates as products are added."""
    logged_in_user.add_product_to_cart(BACKPACK)
    logged_in_user.expect_cart_count("1")
    
    logged_in_user.add_product_to_cart(BIKE_LIGHT)
    logged_in_user.expect_cart_count("2")


@pytest.mark.cart
def test_remove_product_from_cart(logged_in_user, cart_page):
    """User can remove a product from the cart."""
    logged_in_user.add_product_to_cart(BACKPACK)
    logged_in_user.add_product_to_cart(BIKE_LIGHT)
    logged_in_user.open_cart()
    
    cart_page.remove_item(BACKPACK)
    cart_page.expect_item_not_present(BACKPACK)
    cart_page.expect_item_present(BIKE_LIGHT)
