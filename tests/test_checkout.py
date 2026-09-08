"""Regression tests: checkout flow with price verification."""
import pytest
import random
import string

BACKPACK = "Sauce Labs Backpack"
BIKE_LIGHT = "Sauce Labs Bike Light"
FLEECE_JACKET = "Sauce Labs Fleece Jacket"


def generate_random_name():
    """Generate a random name (5-10 characters)."""
    length = random.randint(5, 10)
    return "".join(random.choices(string.ascii_letters, k=length))


@pytest.mark.checkout
def test_checkout_with_price_verification(logged_in_user, cart_page, checkout_page, checkout_overview_page):
    """
    Test the complete checkout flow with price verification.
    User logs in, adds three items, goes to checkout, fills in info,
    and verifies that taxes and totals are calculated correctly.
    """
    # STEP 1: Add items to cart and remember their prices
    item_prices = {}
    
    item_prices[BACKPACK] = logged_in_user.get_product_price(BACKPACK)
    logged_in_user.add_product_to_cart(BACKPACK)
    
    item_prices[BIKE_LIGHT] = logged_in_user.get_product_price(BIKE_LIGHT)
    logged_in_user.add_product_to_cart(BIKE_LIGHT)
    
    item_prices[FLEECE_JACKET] = logged_in_user.get_product_price(FLEECE_JACKET)
    logged_in_user.add_product_to_cart(FLEECE_JACKET)
    
    # Verify all items were added to cart
    assert logged_in_user.get_cart_count() == "3"
    
    # STEP 2: Open cart
    logged_in_user.open_cart()
    
    # Verify items are in cart
    cart_page.expect_item_present(BACKPACK)
    cart_page.expect_item_present(BIKE_LIGHT)
    cart_page.expect_item_present(FLEECE_JACKET)
    
    # STEP 3: Click checkout button
    cart_page.checkout()
    
    # STEP 4: Fill in checkout information with random name and given zipcode
    first_name = generate_random_name()
    last_name = generate_random_name()
    postal_code = "14108"
    
    checkout_page.fill_checkout_info(first_name, last_name, postal_code)
    
    # STEP 5: Click continue to proceed to overview
    checkout_page.continue_to_overview()
    
    # STEP 6: Verify prices are correct on overview page
    # Parse prices and convert to float for comparison
    backpack_price = float(item_prices[BACKPACK].replace("$", ""))
    bike_light_price = float(item_prices[BIKE_LIGHT].replace("$", ""))
    jacket_price = float(item_prices[FLEECE_JACKET].replace("$", ""))
    
    expected_subtotal = backpack_price + bike_light_price + jacket_price
    actual_subtotal = checkout_overview_page.get_item_total()
    
    # Verify item total
    assert abs(actual_subtotal - expected_subtotal) < 0.01, \
        f"Expected subtotal ${expected_subtotal:.2f}, got ${actual_subtotal:.2f}"
    
    # Verify tax is calculated
    tax = checkout_overview_page.get_tax()
    assert tax > 0, "Tax should be greater than 0"
    
    # Verify total = subtotal + tax
    total = checkout_overview_page.get_total()
    calculated_total = round(actual_subtotal + tax, 2)
    
    assert abs(total - calculated_total) < 0.01, \
        f"Total should be ${calculated_total:.2f} (${actual_subtotal:.2f} + ${tax:.2f}), got ${total:.2f}"
    
    # All verifications passed
    assert True, "Checkout complete with correct price calculations"
