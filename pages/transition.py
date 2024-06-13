from locators.header_locators import HeaderLocators
from locators.main_page_locators import MainPagesLocators
from locators.transition_locators import TransitionLocators
from pages.base_page import BasePage


class Transition(BasePage):

    def click_to_logo_scooter(self):
        self.click_to_element(HeaderLocators.LOGO_SCOOTER)

    def click_to_logo_yandex(self):
        self.click_to_element(HeaderLocators.LOGO_YANDEX)

    def get_main_header(self):
        return self.get_text_from_element(MainPagesLocators.MAIN_HEADER)

    def switch_to_open_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def open_dzen_page(self):
        self.switch_to_open_window()

        return self.get_text_from_element(TransitionLocators.BUTTON_SEARCH)
