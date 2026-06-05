import re

from playwright.sync_api import Page

from pages.inventory_page import InventoryPage


class TestInventory:

    def test_tc08_product_list_displayed_after_login(self, logged_in_page: Page) -> None:
        inventory_page = InventoryPage(logged_in_page)

        assert inventory_page.get_product_count() == 6
        assert all(name for name in inventory_page.get_product_names())
        assert all(desc for desc in inventory_page.get_product_descriptions())
        assert all(re.match(r"^\$\d+\.\d{2}$", price) for price in inventory_page.get_product_price_texts())
        assert inventory_page.get_add_to_cart_button_count() == 6

    def test_tc09_sort_products_a_to_z_default(self, logged_in_page: Page) -> None:
        inventory_page = InventoryPage(logged_in_page)

        names = inventory_page.get_product_names()

        assert inventory_page.get_active_sort_label() == "Name (A to Z)"
        assert names == sorted(names)

    def test_tc10_sort_products_z_to_a(self, logged_in_page: Page) -> None:
        inventory_page = InventoryPage(logged_in_page)

        inventory_page.sort_by_name_desc()
        names = inventory_page.get_product_names()

        assert names == sorted(names, reverse=True)

    def test_tc11_sort_products_by_price_ascending(self, logged_in_page: Page) -> None:
        inventory_page = InventoryPage(logged_in_page)

        inventory_page.sort_by_price_asc()
        prices = inventory_page.get_product_prices()

        assert prices == sorted(prices)

    def test_tc12_sort_products_by_price_descending(self, logged_in_page: Page) -> None:
        inventory_page = InventoryPage(logged_in_page)

        inventory_page.sort_by_price_desc()
        prices = inventory_page.get_product_prices()

        assert prices == sorted(prices, reverse=True)

    def test_tc13_cart_badge_updates_after_adding_product(self, logged_in_page: Page) -> None:
        inventory_page = InventoryPage(logged_in_page)

        assert not inventory_page.is_cart_badge_visible()

        inventory_page.add_first_product_to_cart()

        assert inventory_page.is_cart_badge_visible()
        assert inventory_page.get_cart_badge_text() == "1"
