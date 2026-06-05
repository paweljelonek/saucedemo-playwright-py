from playwright.sync_api import Locator, Page

from utils.urls import URL


class CartPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self._cart_items: Locator = page.locator(".cart_item")
        self._cart_badge: Locator = page.locator(".shopping_cart_badge")
        self._continue_shopping_button: Locator = page.locator("[data-test='continue-shopping']")
        self._checkout_button: Locator = page.locator("[data-test='checkout']")

    def is_loaded(self) -> bool:
        return URL.CART in self.page.url

    def get_item_count(self) -> int:
        return self._cart_items.count()

    def get_item_names(self) -> list[str]:
        return self._cart_items.locator(".inventory_item_name").all_inner_texts()

    def get_item_prices(self) -> list[str]:
        return self._cart_items.locator(".inventory_item_price").all_inner_texts()

    def get_item_quantity(self, index: int) -> str:
        return self._cart_items.nth(index).locator(".cart_quantity").inner_text()

    def remove_item_by_index(self, index: int) -> None:
        self._cart_items.nth(index).locator("button").click()

    def continue_shopping(self) -> None:
        self._continue_shopping_button.click()

    def proceed_to_checkout(self) -> None:
        self._checkout_button.click()

    def is_checkout_button_visible(self) -> bool:
        return self._checkout_button.is_visible()

    def get_cart_badge_text(self) -> str:
        return self._cart_badge.inner_text()

    def is_cart_badge_visible(self) -> bool:
        return self._cart_badge.is_visible()
