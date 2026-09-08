# Saucedemo Regression Tests

A comprehensive test automation suite for [saucedemo.com](https://www.saucedemo.com/) using Playwright and pytest.

## 📋 Project Overview

This project provides regression tests for the Saucedemo demo e-commerce site. It covers key user workflows including:
- **Login** - Valid/invalid credentials, error handling
- **Inventory/Products** - Product listing, sorting, filtering
- **Shopping Cart** - Add/remove items, cart management
- **Checkout** - Complete purchase flow

## 🏗️ Project Structure

```
saucedemo-regression-tests/
├── pages/                      # Page Object Models
│   ├── base_page.py           # Base class for all pages
│   ├── login_page.py          # Login page interactions
│   ├── inventory_page.py      # Products listing page
│   ├── product_page.py        # Individual product detail page
│   └── cart_page.py           # Shopping cart page
├── tests/                      # Test files
│   ├── conftest.py            # Pytest fixtures and configuration
│   ├── test_login.py          # Login tests
│   ├── test_inventory.py      # Product page tests
│   ├── test_add_to_cart.py    # Add to cart tests
│   └── test_cart_management.py # Cart management tests
├── requirements.txt            # Python dependencies
├── pytest.ini                  # Pytest configuration
└── README.md                   # This file
```

## 🔐 Test Credentials

The following credentials are available on Saucedemo for testing:

| Username | Password | Notes |
|----------|----------|-------|
| standard_user | secret_sauce | Standard user account |
| locked_out_user | secret_sauce | Account locked after login |
| problem_user | secret_sauce | User with UI issues |
| performance_glitch_user | secret_sauce | Slow loading user |

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/fegero585/saucedemo-regression-tests.git
   cd saucedemo-regression-tests
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**
   ```bash
   playwright install
   ```

## 🚀 Running Tests

### Run all tests
```bash
pytest
```

### Run with headed browser (see the browser)
```bash
pytest --headed
```

### Run specific test file
```bash
pytest tests/test_login.py
```

### Run tests with specific marker
```bash
pytest -m smoke
pytest -m login
pytest -m cart
```

### Run tests in parallel
```bash
pytest -n auto
```

### Generate HTML report
```bash
pytest --html=report.html
```

## 📝 Test Categories

Tests are organized using pytest markers:

- **@pytest.mark.smoke** - Quick smoke tests (critical paths)
- **@pytest.mark.login** - Login functionality tests
- **@pytest.mark.inventory** - Product listing tests
- **@pytest.mark.cart** - Shopping cart tests

## 🏗️ Page Object Model

This project uses the **Page Object Model** pattern:

- **base_page.py** - Common functionality (navigation, title, URL)
- **Specific pages** - Inherit from BasePage and encapsulate page-specific selectors and methods

Example usage:
```python
def test_login(login_page):
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    login_page.expect_error_not_present()
```

## 🔧 Key Classes

### LoginPage
- `load()` - Navigate to login
- `login(username, password)` - Perform login
- `expect_error_message(text)` - Assert error appears
- `expect_error_not_present()` - Assert no errors

### InventoryPage
- `load()` - Navigate to products page
- `add_product_to_cart(product_name)` - Add item to cart
- `click_product(product_name)` - View product details
- `sort_by(sort_option)` - Sort products
- `expect_cart_count(count)` - Verify cart badge

### CartPage
- `load()` - Navigate to cart
- `expect_item_present(product_name)` - Item in cart
- `remove_item(product_name)` - Remove from cart
- `checkout()` - Start checkout
- `is_empty()` - Check if cart is empty

## 🐛 Debugging

### Run a single test with more verbosity
```bash
pytest tests/test_login.py::test_valid_login -v -s
```

### Run with Playwright debugging
```bash
PWDEBUG=1 pytest tests/test_login.py
```

### View Playwright traces
```bash
pytest --tracing on
playwright show-trace trace.zip
```

## 📊 Test Coverage

Current test coverage includes:
- ✅ Login (valid/invalid credentials, empty fields)
- ✅ Product listing and sorting
- ✅ Add to cart functionality
- ✅ Cart management
- ⏳ Checkout flow (coming soon)
- ⏳ User account management (coming soon)

## 🚧 Future Enhancements

- [ ] Checkout and payment tests
- [ ] Sorting and filtering edge cases
- [ ] Performance testing
- [ ] API layer tests
- [ ] Visual regression testing
- [ ] CI/CD pipeline

## 📝 Contributing

1. Create a feature branch
2. Write tests following the existing patterns
3. Ensure all tests pass: `pytest`
4. Commit and push
5. Create a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**fegero585**
- GitHub: [@fegero585](https://github.com/fegero585)

## 🔗 Resources

- [Saucedemo Site](https://www.saucedemo.com/)
- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Page Object Model Pattern](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)

---

**Last Updated:** January 2025
