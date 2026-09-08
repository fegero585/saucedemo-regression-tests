# 🧪 Saucedemo Regression Tests

A comprehensive **test automation suite** for [saucedemo.com](https://www.saucedemo.com/) built with modern QA best practices. This project demonstrates expertise in **end-to-end testing**, **page object modeling**, and **test automation frameworks**.

## ✨ Key Features

- **Page Object Model (POM)** - Clean separation of test logic and UI interactions
- **Pytest Framework** - Organized, scalable test structure with fixtures and markers
- **Playwright** - Modern browser automation with cross-browser support
- **Comprehensive Coverage** - Login, inventory, cart, checkout (with price verification), and mobile emulation
- **Test Markers** - Run tests by category (smoke, login, cart, inventory, checkout, mobile)
- **Mobile Device Emulation** - Run any suite against real device viewports via Playwright's `--device` flag
- **Slow-Motion Testing** - Watch tests execute step-by-step with `--slowmo`
- **CI on Every Push** - GitHub Actions runs the full suite headless on `main`/`develop`

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.14** | Programming language |
| **Pytest** | Test framework & assertions |
| **Playwright** | Browser automation & interactions |
| **pytest-playwright** | Pytest plugin for Playwright integration |
| **python-dotenv** | Environment variable management |

## 📋 Project Overview

This project provides regression tests for the Saucedemo demo e-commerce site, covering key user workflows:

- **🔐 Login** - Valid/invalid credentials, error handling, edge cases
- **📦 Inventory/Products** - Product listing, sorting, filtering
- **🛒 Shopping Cart** - Add/remove items, cart management, persistence
- **💳 Checkout** - Complete purchase flow with subtotal/tax/total price verification
- **📱 Mobile** - Login and cart flows under real device emulation

## 🏗️ Project Structure

```
saucedemo-regression-tests/
├── pages/                          # Page Object Models
│   ├── base_page.py                # Base class - common methods for all pages
│   ├── login_page.py               # Login page interactions & validations
│   ├── inventory_page.py           # Products listing, sorting & add-to-cart
│   ├── product_page.py             # Product detail page interactions
│   ├── cart_page.py                # Shopping cart management
│   ├── checkout_page.py            # Checkout info form (step 1)
│   └── checkout_overview_page.py   # Checkout overview & price totals (step 2)
├── tests/                          # Test Suite
│   ├── conftest.py                 # Pytest fixtures & configuration
│   ├── test_login.py               # Login validation tests
│   ├── test_inventory.py           # Product listing & filtering tests
│   ├── test_add_to_cart.py         # Add to cart functionality tests
│   ├── test_cart_management.py     # Cart operations tests
│   ├── test_checkout.py            # Checkout flow with price verification
│   └── test_mobile.py              # Critical flows under mobile emulation
├── .github/workflows/tests.yml     # CI pipeline (GitHub Actions)
├── requirements.txt                # Python dependencies
├── pytest.ini                      # Pytest configuration & markers
└── README.md                       # Documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Git
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/fegero585/saucedemo-regression-tests.git
   cd saucedemo-regression-tests
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\Activate.ps1
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers** (one-time setup)
   ```bash
   playwright install
   ```

## 🧪 Running Tests

Tests run **headless by default** (fast, CI-friendly).

### Run all tests
```bash
pytest
```

### Run a specific test file
```bash
pytest tests/test_login.py -v
```

### Run tests by marker/category
```bash
pytest -m smoke      # Quick smoke tests (critical paths)
pytest -m login      # Login tests only
pytest -m cart       # Cart tests
pytest -m inventory  # Inventory tests
pytest -m checkout   # Checkout tests
pytest -m mobile     # Mobile-emulation tests
```

### Watch tests run (headed browser)
```bash
pytest --headed

# Slow-motion, for visual validation and debugging
pytest --headed --slowmo=1000
```

### Mobile device emulation
```bash
pytest -m mobile --device="iPhone 12"
pytest -m mobile --device="Pixel 5"
```

### Run tests in parallel
```bash
pytest -n auto
```

### Generate an HTML report
```bash
pytest --html=report.html
```

## 🔐 Test Credentials

The following test accounts are available on Saucedemo:

| Username | Password | Purpose |
|----------|----------|---------|
| `standard_user` | `secret_sauce` | Standard user - all features work |
| `locked_out_user` | `secret_sauce` | Locked account - tests login failure |
| `problem_user` | `secret_sauce` | UI display issues - tests resilience |
| `performance_glitch_user` | `secret_sauce` | Slow loading - tests timeout handling |

## 📊 Test Coverage

| Category | Tests | Notes |
|----------|-------|-------|
| Login | 5 tests | Valid/invalid credentials, empty fields |
| Inventory | 5 tests | Listing, sorting, filtering |
| Add to Cart | 4 tests | Single & multiple items |
| Cart Management | 4 tests | Edit, remove, persist |
| Checkout | 1 test | Full flow with subtotal/tax/total price verification |
| Mobile | 2 tests | Login & add-to-cart under device emulation |
| **Total** | **21 tests** | |

## 🏗️ Architecture Highlights

### Page Object Model (POM)
Each page is represented as a separate class with:
- **Selectors** - Centralized element locators
- **Methods** - User interactions (click, type, navigate)
- **Assertions** - Page-specific validations

```python
# Example: Using LoginPage POM
def test_valid_login(login_page, inventory_page):
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in inventory_page.get_url()
```

### Fixture Pattern
Pytest fixtures provide:
- Fresh browser page per test
- Pre-configured page objects
- Logged-in user fixture for dependent tests

```python
@pytest.fixture
def logged_in_user(login_page, inventory_page):
    login_page.load()
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)
    return inventory_page
```

### Price Verification Example
`test_checkout.py` captures each item's price at add-to-cart time, then
asserts the checkout overview's subtotal, tax, and total all reconcile:

```python
expected_subtotal = backpack_price + bike_light_price + jacket_price
actual_subtotal = checkout_overview_page.get_item_total()
assert abs(actual_subtotal - expected_subtotal) < 0.01
```

## 🔧 Key Classes

### LoginPage
- `load()` - Navigate to login
- `login(username, password)` - Perform login
- `expect_error_message(text)` - Assert error appears
- `expect_error_not_present()` - Assert no errors

### InventoryPage
- `load()` - Navigate to products page
- `get_product_price(product_name)` - Read a product's price
- `add_product_to_cart(product_name)` / `remove_product_from_cart(product_name)`
- `click_product(product_name)` - View product details
- `sort_by(sort_option)` - Sort products (`az`, `za`, `lohi`, `hilo`)
- `get_cart_count()` / `expect_cart_count(count)` - Verify cart badge
- `open_cart()` - Navigate to the cart

### CartPage
- `load()` - Navigate to cart
- `expect_item_present(product_name)` / `expect_item_not_present(product_name)`
- `remove_item(product_name)` - Remove from cart
- `checkout()` - Start checkout
- `is_empty()` - Check if cart is empty

### CheckoutPage / CheckoutOverviewPage
- `fill_checkout_info(first_name, last_name, postal_code)` - Fill step 1 form
- `continue_to_overview()` / `cancel_checkout()`
- `get_item_total()` / `get_tax()` / `get_total()` - Read step 2 totals as floats
- `finish_checkout()` - Complete the order

## 🐛 Debugging

### Run a single test with more verbosity
```bash
pytest tests/test_login.py::test_valid_login -v -s
```

### Run with Playwright's debugger
```bash
PWDEBUG=1 pytest tests/test_login.py
```

### View Playwright traces
```bash
pytest --tracing on
playwright show-trace trace.zip
```

## ⚙️ Continuous Integration

Every push and pull request to `main`/`develop` triggers [.github/workflows/tests.yml](.github/workflows/tests.yml), which installs dependencies, installs Playwright's browsers, and runs the full suite headless on Ubuntu.

## 🚧 Future Enhancements

- [ ] API layer tests
- [ ] Visual regression testing
- [ ] Cross-browser matrix in CI (Firefox, WebKit)
- [ ] Test data fixtures via `python-dotenv` for environment-specific config

## 🤝 Best Practices Demonstrated

✅ **Page Object Model** - Maintainable, scalable test code
✅ **Pytest Fixtures** - DRY principle, code reuse
✅ **Test Markers** - Organized test execution
✅ **Descriptive Assertions** - Clear test intent
✅ **Error Handling** - Validates error messages
✅ **Mobile Emulation** - Device viewport coverage, not just desktop
✅ **CI/CD** - Automated test runs via GitHub Actions

## 📝 Contributing

1. Create a feature branch
2. Write tests following the existing patterns
3. Ensure all tests pass: `pytest`
4. Commit and push
5. Create a Pull Request

## 📚 Learning Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Page Object Model Pattern](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
- [Saucedemo](https://www.saucedemo.com/) - Test application

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**fegero585**
- GitHub: [@fegero585](https://github.com/fegero585)

---

**Ready to see it in action?** Clone the repo and run `pytest --headed --slowmo=1000` to watch the tests execute!
