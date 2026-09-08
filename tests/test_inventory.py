"""Regression tests: inventory/products page."""
import pytest

BACKPACK = "Sauce Labs Backpack"
BIKE_LIGHT = "Sauce Labs Bike Light"


@pytest.mark.smoke
@pytest.mark.inventory
def test_products_are_displayed(logged_in_user):
    """User can see products on the inventory page."""
    products = logged_in_user.page.locator("div.inventory_item")
    assert products.count() > 0


@pytest.mark.inventory
def test_can_open_product_details(logged_in_user, product_page):
    """User can click on a product to view details."""
    logged_in_user.click_product(BACKPACK)
    title = product_page.get_product_title()
    assert BACKPACK in title


@pytest.mark.inventory
def test_products_have_prices(logged_in_user):
    """All products should have prices displayed."""
    price = logged_in_user.get_product_price(BACKPACK)
    assert "$" in price


@pytest.mark.inventory
def test_sort_by_name_a_to_z(logged_in_user):
    """Sorting A to Z puts product names in ascending alphabetical order."""
    logged_in_user.sort_by("az")
    names = logged_in_user.get_product_names()
    assert names == sorted(names)


@pytest.mark.inventory
def test_sort_by_name_z_to_a(logged_in_user):
    """Sorting Z to A puts product names in descending alphabetical order."""
    logged_in_user.sort_by("za")
    names = logged_in_user.get_product_names()
    assert names == sorted(names, reverse=True)


@pytest.mark.inventory
def test_sort_by_price_low_to_high(logged_in_user):
    """Sorting price low to high puts prices in ascending order."""
    logged_in_user.sort_by("lohi")
    prices = logged_in_user.get_product_prices()
    assert prices == sorted(prices)


@pytest.mark.inventory
def test_sort_by_price_high_to_low(logged_in_user):
    """Sorting price high to low puts prices in descending order."""
    logged_in_user.sort_by("hilo")
    prices = logged_in_user.get_product_prices()
    assert prices == sorted(prices, reverse=True)
