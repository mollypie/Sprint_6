from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class Header(BasePage):

    def click_to_order_button_in_header(self):
        self.click_to_element(HeaderLocators.BUTTON_ORDER_HEADER)

    def click_to_track_button_in_header(self):
        self.click_to_element(HeaderLocators.BUTTON_ORDER_HEADER)