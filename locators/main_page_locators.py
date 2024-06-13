from selenium.webdriver.common.by import By


class MainPagesLocators:
    ACCORDION_QUESTION = By.ID, 'accordion__heading-{}'  # вопрос
    ACCORDION_ANSWER = By.ID, 'accordion__panel-{}'  # ответ
    LAST_ELEMENT_OF_PAGE = By.ID, 'accordion__heading-7'  # последний элемент на странице

    MAIN_HEADER = By.XPATH, './/div[starts-with(@class, "Home_Header")]'  # заголовок главной страницы

    BUTTON_ORDER_MAIN = By.XPATH, ('.//div[starts-with(@class, "Home_FinishButton")]'
                                   '/button[text()="Заказать"]')  # кнопка "Заказать"
