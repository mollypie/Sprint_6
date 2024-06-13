import allure

from locators.transition_locators import TransitionLocators
from pages.base_page import BasePage


class Transition(BasePage):
    @allure.step('Переход в открывшуюся страницу')
    def switch_to_open_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получение подтверждения нахождения на новой странице')
    def open_dzen_page(self):
        self.switch_to_open_window()

        return self.get_text_from_element(TransitionLocators.BUTTON_SEARCH)
