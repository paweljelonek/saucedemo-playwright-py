from playwright.sync_api import Locator, Page


class Sidebar:
    def __init__(self, page: Page) -> None:
        self.page = page
        self._open_button: Locator = page.locator("#react-burger-menu-btn")
        self._close_button: Locator = page.locator("#react-burger-cross-btn")
        self._all_items_link: Locator = page.locator("#inventory_sidebar_link")
        self._about_link: Locator = page.locator("#about_sidebar_link")
        self._logout_link: Locator = page.locator("#logout_sidebar_link")
        self._reset_link: Locator = page.locator("#reset_sidebar_link")

    def open(self) -> None:
        self._open_button.click()

    def close(self) -> None:
        self._close_button.click()

    def click_logout(self) -> None:
        self._logout_link.click()

    def click_all_items(self) -> None:
        self._all_items_link.click()

    def click_reset_app_state(self) -> None:
        self._reset_link.click()

    def is_all_items_visible(self) -> bool:
        return self._all_items_link.is_visible()

    def is_about_visible(self) -> bool:
        return self._about_link.is_visible()

    def is_logout_visible(self) -> bool:
        return self._logout_link.is_visible()

    def is_reset_visible(self) -> bool:
        return self._reset_link.is_visible()

    def is_close_button_visible(self) -> bool:
        return self._close_button.is_visible()
