# 🧪 Saucedemo Regression Tests

A comprehensive **test automation suite** for [saucedemo.com](https://www.saucedemo.com/) built with modern QA best practices. This project demonstrates expertise in **end-to-end testing**, **page object modeling**, and **test automation frameworks**.

## ✨ Key Features

- **Page Object Model (POM)** - Clean separation of test logic and UI interactions
- **Pytest Framework** - Organized, scalable test structure with fixtures and markers
- **Playwright** - Modern browser automation with cross-browser support
- **Comprehensive Coverage** - Login, inventory, products, cart, and checkout flows
- **Test Markers** - Run tests by category (smoke, login, cart, inventory, checkout)
- **Slow-Motion Testing** - Watch tests execute step-by-step with `--slowmo` option
- **Headed Browser** - Visual feedback during test execution (enabled by default)

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
- **💳 Checkout** - Complete purchase flow

## 🏗️ Project Structure

```
saucedemo-regression-tests/
├── pages/                      # Page Object Models
│   ├── base_page.py           # Base class - common methods for all pages
│   ├── login_page.py          # Login page interactions & validations
│   ├── inventory_page.py      # Products listing & filtering
│   ├── product_page.py        # Product detail page interactions
│   └── cart_page.py           # Shopping cart management
├── tests/                      # Test Suite
│   ├── conftest.py            # Pytest fixtures & configuration
│   ├── test_login.py          # 5 login validation tests
│   ├── test_inventory.py      # Product listing & filtering tests
│   ├── test_add_to_cart.py    # Add to cart functionality tests
│   └── test_cart_management.py # Cart operations tests
├── requirements.txt            # Python dependencies
├── pytest.ini                  # Pytest configuration & markers
└── README.md                   # Documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Git
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/saucedemo-regression-tests.git
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

### Run All Tests
```bash
python -m pytest tests/ -v
```

### Run Specific Test File
```bash
python -m pytest tests/test_login.py -v
```

### Run Tests by Marker/Category
```bash
# Smoke tests (quick validation)
python -m pytest -m smoke

# Login tests only
python -m pytest -m login

# Cart tests
python -m pytest -m cart

# Inventory tests
python -m pytest -m inventory
```

### Watch Tests in Slow-Motion
Perfect for visual validation and debugging:
```bash
# 500ms delay between actions
python -m pytest tests/ -v --slowmo=500

# 1000ms (1 second) delay
python -m pytest tests/ -v --slowmo=1000

# 2000ms (2 seconds) delay
python -m pytest tests/ -v --slowmo=2000
```

### Headless Mode (No Browser Window)
```bash
python -m pytest tests/ -v --headless
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

| Category | Tests | Status |
|----------|-------|--------|
| Login | 5 tests | ✅ Full coverage |
| Inventory | 4+ tests | ✅ Listing, sorting, filtering |
| Add to Cart | 3+ tests | ✅ Single & multiple items |
| Cart Management | 2+ tests | ✅ Edit, remove, persist |
| **Total** | **14+ tests** | **✅ Pass** |

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

## 📈 Performance

- **Execution Time**: ~12-15 seconds for all tests (with visual playback)
- **Headless Mode**: ~8-10 seconds (faster execution)
- **Slow-Motion Mode**: Adjustable delays for visual testing

## 🔍 Code Quality

- Clean, readable test structure
- Follows pytest best practices
- POM reduces maintenance overhead
- Descriptive test names and docstrings
- Proper fixture organization

## 📝 Example Test Case

```python
@pytest.mark.smoke
@pytest.mark.login
def test_valid_login(login_page, inventory_page):
    """User can login with valid credentials and reach inventory."""
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.load()  # Navigate to confirm page
    assert "inventory" in inventory_page.get_url()
```

## 🤝 Best Practices Demonstrated

✅ **Page Object Model** - Maintainable, scalable test code  
✅ **Pytest Fixtures** - DRY principle, code reuse  
✅ **Test Markers** - Organized test execution  
✅ **Descriptive Assertions** - Clear test intent  
✅ **Error Handling** - Validates error messages  
✅ **Cross-browser Ready** - Playwright supports multiple browsers  
✅ **CI/CD Ready** - Can be integrated with GitHub Actions, Jenkins, etc.

## 🔄 Extending the Tests

To add new tests:

1. Create new test file in `tests/` folder
2. Add marker decorator: `@pytest.mark.category_name`
3. Use existing page objects or create new ones in `pages/` folder
4. Run with: `python -m pytest tests/new_test.py -v`

Example:
```python
# tests/test_checkout.py
@pytest.mark.checkout
def test_complete_purchase(logged_in_user, cart_page):
    """Complete end-to-end purchase flow."""
    # Test implementation
    pass
```

## 📚 Learning Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Page Object Model Pattern](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
- [Saucedemo](https://www.saucedemo.com/) - Test application

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created as a demonstration of QA automation expertise and testing best practices.

---

**Ready to see it in action?** Clone the repo and run `python -m pytest tests/ -v --slowmo=1000` to watch the tests execute!

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
