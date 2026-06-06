from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.checkout_data import VALID_CUSTOMER
from utils.urls import URL


class TestCheckoutForm:
    def test_tc24_checkout_opens_form_with_required_fields(self, cart_with_product: Page) -> None:
        cart_page = CartPage(cart_with_product)
        checkout_page = CheckoutPage(cart_with_product)

        cart_page.proceed_to_checkout()

        assert URL.CHECKOUT_STEP_ONE in cart_with_product.url
        assert checkout_page.is_first_name_visible()
        assert checkout_page.is_last_name_visible()
        assert checkout_page.is_postal_code_visible()
        assert checkout_page.is_continue_visible()
        assert checkout_page.is_cancel_visible()

    def test_tc25_checkout_without_first_name_shows_error(self, checkout_form_page: Page) -> None:
        checkout_page = CheckoutPage(checkout_form_page)

        checkout_page.fill_last_name(VALID_CUSTOMER.last_name)
        checkout_page.fill_postal_code(VALID_CUSTOMER.postal_code)
        checkout_page.click_continue()

        assert URL.CHECKOUT_STEP_ONE in checkout_form_page.url
        assert "First Name is required" in checkout_page.get_error_message()

    def test_tc26_checkout_without_last_name_shows_error(self, checkout_form_page: Page) -> None:
        checkout_page = CheckoutPage(checkout_form_page)

        checkout_page.fill_first_name(VALID_CUSTOMER.first_name)
        checkout_page.fill_postal_code(VALID_CUSTOMER.postal_code)
        checkout_page.click_continue()

        assert "Last Name is required" in checkout_page.get_error_message()

    def test_tc27_checkout_without_postal_code_shows_error(self, checkout_form_page: Page) -> None:
        checkout_page = CheckoutPage(checkout_form_page)

        checkout_page.fill_first_name(VALID_CUSTOMER.first_name)
        checkout_page.fill_last_name(VALID_CUSTOMER.last_name)
        checkout_page.click_continue()

        assert "Postal Code is required" in checkout_page.get_error_message()
