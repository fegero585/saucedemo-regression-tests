"""Regression tests: login functionality."""
import pytest

STANDARD_USER = "standard_user"
STANDARD_PASSWORD = "secret_sauce"


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
