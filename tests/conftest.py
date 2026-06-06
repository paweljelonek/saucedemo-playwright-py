import pytest
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.checkout_data import VALID_CUSTOMER
from utils.users import STANDARD_USER


@pytest.fixture
def logged_in_page(page: Page) -> Page:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(STANDARD_USER.username, STANDARD_USER.password)
    return page


@pytest.fixture
def cart_with_product(logged_in_page: Page) -> Page:
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_first_product_to_cart()
    inventory_page.click_cart_icon()
    return logged_in_page


@pytest.fixture
def checkout_form_page(cart_with_product: Page) -> Page:
    cart_page = CartPage(cart_with_product)
    cart_page.proceed_to_checkout()
    return cart_with_product


@pytest.fixture
def checkout_summary_page(checkout_form_page: Page) -> Page:
    checkout_page = CheckoutPage(checkout_form_page)
    checkout_page.fill_first_name(VALID_CUSTOMER.first_name)
    checkout_page.fill_last_name(VALID_CUSTOMER.last_name)
    checkout_page.fill_postal_code(VALID_CUSTOMER.postal_code)
    checkout_page.click_continue()
    return checkout_form_page
