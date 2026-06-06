from playwright.sync_api import Locator, Page

from utils.urls import URL


class InventoryPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self._app_logo: Locator = page.locator(".app_logo")
        self._product_items: Locator = page.locator(".inventory_item")
        self._product_names: Locator = page.locator(".inventory_item_name")
        self._product_descriptions: Locator = page.locator(".inventory_item_desc")
        self._product_prices: Locator = page.locator(".inventory_item_price")
        self._add_to_cart_buttons: Locator = page.locator(".inventory_item button")
        self._sort_dropdown: Locator = page.locator(".product_sort_container")
        self._cart_icon: Locator = page.locator(".shopping_cart_link")
        self._cart_badge: Locator = page.locator(".shopping_cart_badge")

    def navigate(self) -> None:
        self.page.goto(URL.INVENTORY)

    def is_loaded(self) -> bool:
        return URL.INVENTORY in self.page.url

    def get_logo_text(self) -> str:
        return self._app_logo.inner_text()

    def get_product_count(self) -> int:
        return self._product_items.count()

    def get_product_names(self) -> list[str]:
        return self._product_names.all_inner_texts()

    def get_product_descriptions(self) -> list[str]:
        return self._product_descriptions.all_inner_texts()

    def get_product_price_texts(self) -> list[str]:
        return self._product_prices.all_inner_texts()

    def get_product_prices(self) -> list[float]:
        return [float(t.replace("$", "")) for t in self.get_product_price_texts()]

    def get_add_to_cart_button_count(self) -> int:
        return self._add_to_cart_buttons.count()

    def get_active_sort_label(self) -> str:
        return self._sort_dropdown.evaluate("el => el.options[el.selectedIndex].text")

    def sort_by_name_asc(self) -> None:
        self._sort_dropdown.select_option("az")

    def sort_by_name_desc(self) -> None:
        self._sort_dropdown.select_option("za")

    def sort_by_price_asc(self) -> None:
        self._sort_dropdown.select_option("lohi")

    def sort_by_price_desc(self) -> None:
        self._sort_dropdown.select_option("hilo")

    def click_first_product_name(self) -> None:
        self._product_names.first.click()

    def click_cart_icon(self) -> None:
        self._cart_icon.click()

    def add_first_product_to_cart(self) -> None:
        self._product_items.first.locator("button").click()

    def add_product_to_cart_by_index(self, index: int) -> None:
        self._product_items.nth(index).locator("button").click()

    def reload(self) -> None:
        self.page.reload()

    def get_cart_badge_text(self) -> str:
        return self._cart_badge.inner_text()

    def is_cart_badge_visible(self) -> bool:
        return self._cart_badge.is_visible()
