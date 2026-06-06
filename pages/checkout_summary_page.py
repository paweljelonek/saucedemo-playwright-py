from playwright.sync_api import Locator, Page

from utils.urls import URL


class CheckoutSummaryPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self._cart_items: Locator = page.locator(".cart_item")
        self._subtotal_label: Locator = page.locator(".summary_subtotal_label")
        self._tax_label: Locator = page.locator(".summary_tax_label")
        self._total_label: Locator = page.locator(".summary_total_label")
        self._finish_button: Locator = page.locator("[data-test='finish']")
        self._cancel_button: Locator = page.locator("[data-test='cancel']")
        self._cart_badge: Locator = page.locator(".shopping_cart_badge")

    def is_loaded(self) -> bool:
        return URL.CHECKOUT_STEP_TWO in self.page.url

    def get_item_count(self) -> int:
        return self._cart_items.count()

    def get_item_names(self) -> list[str]:
        return self._cart_items.locator(".inventory_item_name").all_inner_texts()

    def get_item_prices(self) -> list[float]:
        texts = self._cart_items.locator(".inventory_item_price").all_inner_texts()
        return [float(t.replace("$", "")) for t in texts]

    def _parse_price(self, text: str) -> float:
        return float(text.split("$")[-1])

    def get_subtotal(self) -> float:
        return self._parse_price(self._subtotal_label.inner_text())

    def get_tax(self) -> float:
        return self._parse_price(self._tax_label.inner_text())

    def get_total(self) -> float:
        return self._parse_price(self._total_label.inner_text())

    def click_finish(self) -> None:
        self._finish_button.click()

    def click_cancel(self) -> None:
        self._cancel_button.click()

    def is_cart_badge_visible(self) -> bool:
        return self._cart_badge.is_visible()
