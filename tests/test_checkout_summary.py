from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_page import CheckoutPage
from pages.checkout_summary_page import CheckoutSummaryPage
from pages.inventory_page import InventoryPage
from utils.checkout_data import VALID_CUSTOMER
from utils.urls import URL


class TestCheckoutSummary:

    def test_tc28_completing_form_opens_order_summary(self, checkout_summary_page: Page) -> None:
        summary_page = CheckoutSummaryPage(checkout_summary_page)

        assert URL.CHECKOUT_STEP_TWO in checkout_summary_page.url
        assert summary_page.get_item_count() >= 1
        assert summary_page.get_subtotal() > 0
        assert summary_page.get_tax() > 0
        assert summary_page.get_total() > 0

    def test_tc29_order_summary_amounts_are_correct(self, logged_in_page: Page) -> None:
        inventory_page = InventoryPage(logged_in_page)
        inventory_page.add_product_to_cart_by_index(0)
        inventory_page.add_product_to_cart_by_index(1)
        inventory_page.click_cart_icon()
        CartPage(logged_in_page).proceed_to_checkout()
        checkout_page = CheckoutPage(logged_in_page)
        checkout_page.fill_first_name(VALID_CUSTOMER.first_name)
        checkout_page.fill_last_name(VALID_CUSTOMER.last_name)
        checkout_page.fill_postal_code(VALID_CUSTOMER.postal_code)
        checkout_page.click_continue()

        summary_page = CheckoutSummaryPage(logged_in_page)
        item_prices = summary_page.get_item_prices()

        assert round(summary_page.get_subtotal(), 2) == round(sum(item_prices), 2)
        assert round(summary_page.get_total(), 2) == round(
            summary_page.get_subtotal() + summary_page.get_tax(), 2
        )

    def test_tc30_cancel_on_summary_returns_to_inventory(self, checkout_summary_page: Page) -> None:
        summary_page = CheckoutSummaryPage(checkout_summary_page)
        inventory_page = InventoryPage(checkout_summary_page)

        summary_page.click_cancel()

        assert inventory_page.is_loaded()
        assert inventory_page.get_cart_badge_text() == "1"

    def test_tc31_finishing_order_shows_confirmation(self, checkout_summary_page: Page) -> None:
        summary_page = CheckoutSummaryPage(checkout_summary_page)
        complete_page = CheckoutCompletePage(checkout_summary_page)

        summary_page.click_finish()

        assert complete_page.is_loaded()
        assert complete_page.get_header_text() == "Thank you for your order!"
        assert complete_page.is_back_home_visible()
        assert not complete_page.is_cart_badge_visible()
