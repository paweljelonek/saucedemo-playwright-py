import pytest
from playwright.sync_api import Page

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
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
