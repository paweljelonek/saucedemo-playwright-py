from playwright.sync_api import Page, Locator


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input: Locator = page.locator("#user-name")
        self.password_input: Locator = page.locator("#password")
        self.login_button: Locator = page.locator("#login-button")
        self.error_container: Locator = page.locator("[data-test='error']")

    def navigate(self) -> None:
        self.page.goto("/")

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str:
        return self.error_container.inner_text()
