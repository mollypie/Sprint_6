from helpers import generate_user_data, generate_order_data
from pages.header import Header
from pages.main_page import MainPage
from pages.order_page import OrderPage

from conftest import driver


class TestOrderPage:

    def test_create_order_by_button_in_header(self, driver):
        header = Header(driver)
        order_page = OrderPage(driver)

        header.click_to_order_button_in_header()
        assert 'Заказ оформлен' in order_page.create_order(generate_user_data(), generate_order_data())

    def test_create_order_by_button_in_main(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_to_order_button()
        assert 'Заказ оформлен' in order_page.create_order(generate_user_data(), generate_order_data())
