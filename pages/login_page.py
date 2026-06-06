from playwright.sync_api import Locator, Page

from utils.urls import URL


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self._username_input: Locator = page.locator("#user-name")
        self._password_input: Locator = page.locator("#password")
        self._login_button: Locator = page.locator("#login-button")
        self._error_container: Locator = page.locator("[data-test='error']")

    def navigate(self) -> None:
        self.page.goto(URL.LOGIN)

    def is_loaded(self) -> bool:
        return URL.LOGIN in self.page.url

    def login(self, username: str, password: str) -> None:
        self._username_input.fill(username)
        self._password_input.fill(password)
        self._login_button.click()

    def get_error_message(self) -> str:
        return self._error_container.inner_text()
