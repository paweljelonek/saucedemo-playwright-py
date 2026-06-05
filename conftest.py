import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from utils.users import STANDARD_USER


@pytest.fixture(scope="session")
def base_url() -> str:
    return "https://www.saucedemo.com"


@pytest.fixture
def logged_in_page(page: Page) -> Page:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(STANDARD_USER.username, STANDARD_USER.password)
    return page
