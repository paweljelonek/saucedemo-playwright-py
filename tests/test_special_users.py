from playwright.sync_api import Page

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.urls import URL
from utils.users import ERROR_USER, PERFORMANCE_GLITCH_USER


class TestSpecialUsers:
    def test_tc36_performance_glitch_user_reaches_inventory(self, page: Page) -> None:
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        login_page.navigate()
        login_page.login(PERFORMANCE_GLITCH_USER.username, PERFORMANCE_GLITCH_USER.password)

        assert URL.INVENTORY in page.url
        assert inventory_page.get_product_count() == 6

    def test_tc37_error_user_reaches_inventory(self, page: Page) -> None:
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        login_page.navigate()
        login_page.login(ERROR_USER.username, ERROR_USER.password)

        assert URL.INVENTORY in page.url
        assert inventory_page.get_product_count() == 6
