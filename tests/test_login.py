from playwright.sync_api import Page

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.urls import URL
from utils.users import (
    INVALID_CREDENTIALS_USER,
    LOCKED_OUT_USER,
    PROBLEM_USER,
    STANDARD_USER,
)


class TestLogin:

    def test_tc01_successful_login_with_standard_user(self, page: Page) -> None:
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        login_page.navigate()
        login_page.login(STANDARD_USER.username, STANDARD_USER.password)

        assert URL.INVENTORY in page.url
        assert inventory_page.get_logo_text() == "Swag Labs"
        assert inventory_page.get_product_count() >= 1

    def test_tc02_login_with_locked_out_user(self, page: Page) -> None:
        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login(LOCKED_OUT_USER.username, LOCKED_OUT_USER.password)

        assert URL.INVENTORY not in page.url
        assert "Sorry, this user has been locked out" in login_page.get_error_message()

    def test_tc03_login_with_wrong_password(self, page: Page) -> None:
        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login(INVALID_CREDENTIALS_USER.username, INVALID_CREDENTIALS_USER.password)

        assert URL.INVENTORY not in page.url
        assert "Username and password do not match" in login_page.get_error_message()

    def test_tc04_login_with_empty_fields(self, page: Page) -> None:
        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login("", "")

        assert "Username is required" in login_page.get_error_message()

    def test_tc05_login_with_empty_password(self, page: Page) -> None:
        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login(STANDARD_USER.username, "")

        assert "Password is required" in login_page.get_error_message()

    def test_tc06_login_with_empty_username(self, page: Page) -> None:
        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login("", STANDARD_USER.password)

        assert "Username is required" in login_page.get_error_message()

    def test_tc07_login_with_problem_user(self, page: Page) -> None:
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        login_page.navigate()
        login_page.login(PROBLEM_USER.username, PROBLEM_USER.password)

        assert URL.INVENTORY in page.url
        assert inventory_page.get_product_count() >= 1
