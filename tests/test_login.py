"""Regression tests: login functionality."""
import pytest
from pages.login_page import LOGIN_URL

STANDARD_USER = "standard_user"
STANDARD_PASSWORD = "secret_sauce"
LOCKED_OUT_USER = "locked_out_user"


@pytest.mark.smoke
@pytest.mark.login
def test_valid_login(login_page, inventory_page):
    """User can login with valid credentials and reach inventory."""
    login_page.load()
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)
    inventory_page.load()  # Navigate to confirm page
    assert "inventory" in inventory_page.get_url()


@pytest.mark.login
def test_invalid_password(login_page):
    """Login fails with invalid password."""
    login_page.load()
    login_page.login(STANDARD_USER, "wrong_password")
    login_page.expect_error_message("Username and password do not match")


@pytest.mark.login
def test_invalid_username(login_page):
    """Login fails with invalid username."""
    login_page.load()
    login_page.login("invalid_user", STANDARD_PASSWORD)
    login_page.expect_error_message("Username and password do not match")


@pytest.mark.login
def test_empty_username(login_page):
    """Login fails with empty username."""
    login_page.load()
    login_page.login("", STANDARD_PASSWORD)
    login_page.expect_error_message("Username is required")


@pytest.mark.login
def test_empty_password(login_page):
    """Login fails with empty password."""
    login_page.load()
    login_page.login(STANDARD_USER, "")
    login_page.expect_error_message("Password is required")


@pytest.mark.login
def test_locked_out_user_cannot_login(login_page):
    """A locked-out user is rejected and stays on the login page."""
    login_page.load()
    login_page.login(LOCKED_OUT_USER, STANDARD_PASSWORD)
    login_page.expect_error_message("this user has been locked out")
    assert "inventory" not in login_page.get_url()


@pytest.mark.login
@pytest.mark.parametrize(
    "path",
    ["inventory.html", "cart.html", "checkout-step-one.html", "checkout-complete.html"],
)
def test_protected_pages_require_login(login_page, path):
    """Opening a protected page while logged out shows the login form and an error."""
    login_page.goto(LOGIN_URL + path)
    login_page.expect_error_message(f"You can only access '/{path}' when you are logged in")
    login_page.expect_on_login_page()


@pytest.mark.login
def test_logout_ends_session(logged_in_user, login_page):
    """Logging out returns to a cleared login form and blocks Back navigation."""
    logged_in_user.logout()
    login_page.expect_on_login_page()
    login_page.expect_form_cleared()

    logged_in_user.page.go_back()
    login_page.expect_error_message("You can only access '/inventory.html' when you are logged in")
