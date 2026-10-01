"""Regression tests: critical flows under mobile device emulation.

Every test in this module runs emulating DEFAULT_DEVICE (viewport, touch,
user agent), so a plain `pytest` - including CI - exercises the mobile
layout. pytest-playwright's --device flag still wins when given:

    pytest -m mobile --device="Pixel 5"
"""
import pytest
from playwright.sync_api import expect
from pages.inventory_page import INVENTORY_URL

BACKPACK = "Sauce Labs Backpack"
DEFAULT_DEVICE = "iPhone 12"
MAX_MOBILE_WIDTH = 500   # anything wider means emulation wasn't applied
MIN_TAP_TARGET = 24      # px; WCAG 2.2 SC 2.5.8 minimum target size


@pytest.fixture
def browser_context_args(browser_context_args, playwright, device):
    """Emulate DEFAULT_DEVICE unless --device was passed on the command line."""
    if device:
        return browser_context_args
    descriptor = dict(playwright.devices[DEFAULT_DEVICE])
    # Picks the browser engine, not a context option; we keep the run's --browser.
    descriptor.pop("default_browser_type", None)
    return {**browser_context_args, **descriptor}


@pytest.fixture(autouse=True)
def require_mobile_viewport(page):
    """Fail fast if the page isn't actually at a mobile width."""
    width = page.viewport_size["width"]
    assert width <= MAX_MOBILE_WIDTH, f"expected a mobile viewport, got {width}px wide"


@pytest.mark.mobile
@pytest.mark.smoke
def test_login_on_mobile(login_page, inventory_page):
    """User can log in on a mobile viewport and the inventory fits the screen."""
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    expect(inventory_page.page).to_have_url(INVENTORY_URL)
    inventory_page.expect_loaded()
    assert not inventory_page.has_horizontal_scroll(), "inventory scrolls horizontally on mobile"


@pytest.mark.mobile
def test_add_to_cart_on_mobile(logged_in_user):
    """'Add to cart' is a usable tap target on a mobile viewport."""
    button = logged_in_user.add_to_cart_button(BACKPACK)
    box = button.bounding_box()
    viewport_width = logged_in_user.page.viewport_size["width"]
    assert box["x"] >= 0 and box["x"] + box["width"] <= viewport_width, \
        f"button {box} extends past the {viewport_width}px viewport"
    assert box["width"] >= MIN_TAP_TARGET and box["height"] >= MIN_TAP_TARGET, \
        f"button {box} is smaller than {MIN_TAP_TARGET}px"

    # tap() (not click()) sends a touch event, and fails if another element
    # would receive it - i.e. the button is obscured.
    button.tap()
    logged_in_user.expect_cart_count("1")
