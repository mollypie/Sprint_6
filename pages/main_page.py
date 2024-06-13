from pages.base_page import BasePage
from locators.main_page_locators import MainPagesLocators


class MainPage(BasePage):

    def click_to_order_button(self):
        self.scroll_to_element(MainPagesLocators.BUTTON_ORDER_MAIN)
        self.click_to_element(MainPagesLocators.BUTTON_ORDER_MAIN)

    # @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        new_question_locator = self.format_locators(MainPagesLocators.ACCORDION_QUESTION, num)
        self.scroll_to_element(MainPagesLocators.LAST_ELEMENT_OF_PAGE)
        self.click_to_element(new_question_locator)

    # @allure.step('Получение текста ответа')
    def get_text_answer(self, num):
        new_answer_locator = self.format_locators(MainPagesLocators.ACCORDION_ANSWER, num)
        return self.get_text_from_element(new_answer_locator)

    # @allure.step('Проверка результата')
    def get_answer_text(self, num):
        self.click_to_question(num)
        return self.get_text_answer(num)
