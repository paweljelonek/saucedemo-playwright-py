from playwright.sync_api import Page

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.sidebar import Sidebar
from utils.urls import URL


class TestNavigation:
    def test_tc32_successful_logout_via_sidebar(self, logged_in_page: Page) -> None:
        sidebar = Sidebar(logged_in_page)
        login_page = LoginPage(logged_in_page)

        sidebar.open()
        sidebar.click_logout()

        assert URL.LOGIN in logged_in_page.url
        assert login_page.is_loaded()

    def test_tc33_no_access_to_inventory_after_logout(self, logged_in_page: Page) -> None:
        sidebar = Sidebar(logged_in_page)
        inventory_page = InventoryPage(logged_in_page)
        login_page = LoginPage(logged_in_page)

        sidebar.open()
        sidebar.click_logout()
        inventory_page.navigate()

        assert login_page.is_loaded()
        assert URL.INVENTORY not in logged_in_page.url

    def test_tc34_sidebar_contains_all_expected_options(self, logged_in_page: Page) -> None:
        sidebar = Sidebar(logged_in_page)

        sidebar.open()

        assert sidebar.is_all_items_visible()
        assert sidebar.is_about_visible()
        assert sidebar.is_logout_visible()
        assert sidebar.is_reset_visible()
        assert sidebar.is_close_button_visible()

    def test_tc35_reset_app_state_clears_cart(self, logged_in_page: Page) -> None:
        inventory_page = InventoryPage(logged_in_page)
        sidebar = Sidebar(logged_in_page)

        inventory_page.add_product_to_cart_by_index(0)
        inventory_page.add_product_to_cart_by_index(1)
        sidebar.open()
        sidebar.click_reset_app_state()
        sidebar.close()

        assert not inventory_page.is_cart_badge_visible()
