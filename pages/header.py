import allure

from locators.header_locators import HeaderLocators
from locators.main_page_locators import MainPagesLocators
from pages.base_page import BasePage


class Header(BasePage):
    @allure.step('Клик по кнопке "Заказать" в хедере страницы')
    def click_to_order_button_in_header(self):
        self.click_to_element(HeaderLocators.BUTTON_ORDER_HEADER)

    @allure.step('Клик на логотип "Самокат"')
    def click_to_logo_scooter(self):
        self.click_to_element(HeaderLocators.LOGO_SCOOTER)

    @allure.step('Клик на логотип "Яндекс"')
    def click_to_logo_yandex(self):
        self.click_to_element(HeaderLocators.LOGO_YANDEX)

    @allure.step('Получение текста заголовка главной страницы')
    def get_main_header(self):
        return self.get_text_from_element(MainPagesLocators.MAIN_HEADER)
