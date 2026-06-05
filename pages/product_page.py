from playwright.sync_api import Locator, Page

from utils.urls import URL


class ProductPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self._name: Locator = page.locator(".inventory_details_name")
        self._description: Locator = page.locator(".inventory_details_desc")
        self._price: Locator = page.locator(".inventory_details_price")
        self._image: Locator = page.locator(".inventory_details_img_container img")
        self._add_to_cart_button: Locator = page.locator(".btn_primary.btn_inventory")
        self._remove_button: Locator = page.locator("[data-test='remove']")
        self._back_button: Locator = page.locator("[data-test='back-to-products']")
        self._cart_badge: Locator = page.locator(".shopping_cart_badge")

    def is_loaded(self) -> bool:
        return URL.INVENTORY_ITEM in self.page.url

    def get_name(self) -> str:
        return self._name.inner_text()

    def get_description(self) -> str:
        return self._description.inner_text()

    def get_price(self) -> str:
        return self._price.inner_text()

    def is_image_visible(self) -> bool:
        return self._image.is_visible()

    def is_add_to_cart_visible(self) -> bool:
        return self._add_to_cart_button.is_visible()

    def is_remove_visible(self) -> bool:
        return self._remove_button.is_visible()

    def add_to_cart(self) -> None:
        self._add_to_cart_button.click()

    def remove_from_cart(self) -> None:
        self._remove_button.click()

    def go_back(self) -> None:
        self._back_button.click()

    def get_cart_badge_text(self) -> str:
        return self._cart_badge.inner_text()

    def is_cart_badge_visible(self) -> bool:
        return self._cart_badge.is_visible()
