from playwright.sync_api import Locator, Page

from utils.urls import URL


class CheckoutPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self._first_name_input: Locator = page.locator("[data-test='firstName']")
        self._last_name_input: Locator = page.locator("[data-test='lastName']")
        self._postal_code_input: Locator = page.locator("[data-test='postalCode']")
        self._continue_button: Locator = page.locator("[data-test='continue']")
        self._cancel_button: Locator = page.locator("[data-test='cancel']")
        self._error_container: Locator = page.locator("[data-test='error']")

    def is_loaded(self) -> bool:
        return URL.CHECKOUT_STEP_ONE in self.page.url

    def is_first_name_visible(self) -> bool:
        return self._first_name_input.is_visible()

    def is_last_name_visible(self) -> bool:
        return self._last_name_input.is_visible()

    def is_postal_code_visible(self) -> bool:
        return self._postal_code_input.is_visible()

    def is_continue_visible(self) -> bool:
        return self._continue_button.is_visible()

    def is_cancel_visible(self) -> bool:
        return self._cancel_button.is_visible()

    def fill_first_name(self, value: str) -> None:
        self._first_name_input.fill(value)

    def fill_last_name(self, value: str) -> None:
        self._last_name_input.fill(value)

    def fill_postal_code(self, value: str) -> None:
        self._postal_code_input.fill(value)

    def click_continue(self) -> None:
        self._continue_button.click()

    def click_cancel(self) -> None:
        self._cancel_button.click()

    def get_error_message(self) -> str:
        return self._error_container.inner_text()
