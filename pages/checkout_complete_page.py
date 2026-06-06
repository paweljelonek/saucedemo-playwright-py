from playwright.sync_api import Locator, Page

from utils.urls import URL


class CheckoutCompletePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self._header: Locator = page.locator(".complete-header")
        self._back_home_button: Locator = page.locator("[data-test='back-to-products']")
        self._cart_badge: Locator = page.locator(".shopping_cart_badge")

    def is_loaded(self) -> bool:
        return URL.CHECKOUT_COMPLETE in self.page.url

    def get_header_text(self) -> str:
        return self._header.inner_text()

    def is_back_home_visible(self) -> bool:
        return self._back_home_button.is_visible()

    def is_cart_badge_visible(self) -> bool:
        return self._cart_badge.is_visible()
