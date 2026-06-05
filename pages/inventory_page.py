from playwright.sync_api import Page, Locator


class InventoryPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self._app_logo: Locator = page.locator(".app_logo")
        self._product_items: Locator = page.locator(".inventory_item")

    def is_loaded(self) -> bool:
        return "/inventory.html" in self.page.url

    def get_logo_text(self) -> str:
        return self._app_logo.inner_text()

    def get_product_count(self) -> int:
        return self._product_items.count()
