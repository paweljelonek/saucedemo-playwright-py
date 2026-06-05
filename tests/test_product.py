import pytest
from playwright.sync_api import Page

from pages.inventory_page import InventoryPage
from pages.product_page import ProductPage
from utils.urls import URL


@pytest.fixture
def product_detail_page(logged_in_page: Page) -> Page:
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.click_first_product_name()
    return logged_in_page


class TestProduct:
    def test_tc14_product_name_opens_details_page(self, product_detail_page: Page) -> None:
        product_page = ProductPage(product_detail_page)

        assert URL.INVENTORY_ITEM in product_detail_page.url
        assert product_page.get_name()
        assert product_page.get_description()
        assert product_page.get_price()
        assert product_page.is_image_visible()
        assert product_page.is_add_to_cart_visible()

    def test_tc15_adding_product_from_details_updates_cart_badge(self, product_detail_page: Page) -> None:
        product_page = ProductPage(product_detail_page)

        product_page.add_to_cart()

        assert product_page.is_remove_visible()
        assert product_page.get_cart_badge_text() == "1"

    def test_tc16_removing_product_from_details_clears_cart_badge(self, product_detail_page: Page) -> None:
        product_page = ProductPage(product_detail_page)

        product_page.add_to_cart()
        product_page.remove_from_cart()

        assert product_page.is_add_to_cart_visible()
        assert not product_page.is_cart_badge_visible()

    def test_tc17_back_button_returns_to_inventory(self, product_detail_page: Page) -> None:
        product_page = ProductPage(product_detail_page)
        inventory_page = InventoryPage(product_detail_page)

        product_page.go_back()

        assert inventory_page.is_loaded()
        assert inventory_page.get_product_count() == 6
