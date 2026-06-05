from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from utils.urls import URL


class TestCart:
    def test_tc18_adding_one_product_shows_it_in_cart(self, logged_in_page: Page) -> None:
        inventory_page = InventoryPage(logged_in_page)
        cart_page = CartPage(logged_in_page)

        inventory_page.add_first_product_to_cart()
        inventory_page.click_cart_icon()

        assert URL.CART in logged_in_page.url
        assert cart_page.get_item_count() == 1
        assert cart_page.get_item_names()
        assert cart_page.get_item_prices()
        assert cart_page.get_item_quantity(0) == "1"

    def test_tc19_adding_3_products_shows_all_in_cart(self, logged_in_page: Page) -> None:
        inventory_page = InventoryPage(logged_in_page)
        cart_page = CartPage(logged_in_page)

        inventory_page.add_product_to_cart_by_index(0)
        inventory_page.add_product_to_cart_by_index(1)
        inventory_page.add_product_to_cart_by_index(2)
        inventory_page.click_cart_icon()

        assert cart_page.get_cart_badge_text() == "3"
        assert cart_page.get_item_count() == 3

    def test_tc20_removing_product_from_cart_leaves_one_item(self, logged_in_page: Page) -> None:
        inventory_page = InventoryPage(logged_in_page)
        cart_page = CartPage(logged_in_page)

        inventory_page.add_product_to_cart_by_index(0)
        inventory_page.add_product_to_cart_by_index(1)
        inventory_page.click_cart_icon()

        first_product_name = cart_page.get_item_names()[1]
        cart_page.remove_item_by_index(0)

        assert cart_page.get_item_count() == 1
        assert cart_page.get_cart_badge_text() == "1"
        assert first_product_name in cart_page.get_item_names()

    def test_tc21_removing_only_product_leaves_cart_empty(self, logged_in_page: Page) -> None:
        inventory_page = InventoryPage(logged_in_page)
        cart_page = CartPage(logged_in_page)

        inventory_page.add_first_product_to_cart()
        inventory_page.click_cart_icon()
        cart_page.remove_item_by_index(0)

        assert cart_page.get_item_count() == 0
        assert not cart_page.is_cart_badge_visible()
        assert cart_page.is_checkout_button_visible()

    def test_tc22_continue_shopping_returns_to_inventory(self, logged_in_page: Page) -> None:
        inventory_page = InventoryPage(logged_in_page)
        cart_page = CartPage(logged_in_page)

        inventory_page.add_first_product_to_cart()
        inventory_page.click_cart_icon()
        cart_page.continue_shopping()

        assert inventory_page.is_loaded()
        assert inventory_page.get_cart_badge_text() == "1"

    def test_tc23_cart_content_survives_page_reload(self, logged_in_page: Page) -> None:
        inventory_page = InventoryPage(logged_in_page)
        cart_page = CartPage(logged_in_page)

        inventory_page.add_first_product_to_cart()
        inventory_page.reload()

        assert inventory_page.get_cart_badge_text() == "1"

        inventory_page.click_cart_icon()
        assert cart_page.get_item_count() == 1
