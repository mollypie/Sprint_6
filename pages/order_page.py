from helpers import generate_number_metro_station
from pages.base_page import BasePage
from locators.order_page_locators import OrderPagesLocators


class OrderPage(BasePage):

    def prepare_user_data(self, user_data):
        self.add_text_to_element(OrderPagesLocators.INPUT_NAME, user_data['name'])
        self.add_text_to_element(OrderPagesLocators.INPUT_LAST_NAME, user_data['last_name'])
        self.add_text_to_element(OrderPagesLocators.INPUT_ADDRESS, user_data['address'])
        self.add_text_to_element(OrderPagesLocators.INPUT_PHONE_NUMBER, user_data['phone_number'])

        self.click_to_element(OrderPagesLocators.INPUT_STATION)
        metro = self.format_locators(OrderPagesLocators.METRO_STATION, generate_number_metro_station())
        self.scroll_to_element(metro)
        self.click_to_element(metro)

        self.click_to_element(OrderPagesLocators.BUTTON_NEXT)

    def prepare_order_data(self, order_data):
        self.add_text_to_element(OrderPagesLocators.INPUT_DATE, order_data['date'])
        self.click_to_element(order_data['color'])
        self.add_text_to_element(OrderPagesLocators.INPUT_COMMENT, order_data['comment'])
        self.click_to_element(OrderPagesLocators.INPUT_RENTAL_PERIOD)
        self.click_to_element(OrderPagesLocators.DROPDOWN_RENTAL_PERIOD)

        self.click_to_element(OrderPagesLocators.BUTTON_ORDER)
        self.click_to_element(OrderPagesLocators.BUTTON_APPROVE_ORDER)

    def check_order(self):
        return self.get_text_from_element(OrderPagesLocators.HEADER_ORDER_INFORMATION)

    def create_order(self, user_date, order_date):
        self.prepare_user_data(user_date)
        self.prepare_order_data(order_date)
        return self.check_order()
