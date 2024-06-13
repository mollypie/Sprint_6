from selenium.webdriver.common.by import By


class OrderPagesLocators:
    INPUT_NAME = By.XPATH, './/input[@placeholder="* Имя"]'  # поле Имя
    INPUT_LAST_NAME = By.XPATH, './/input[@placeholder="* Фамилия"]'  # поле Фамилия
    INPUT_ADDRESS = By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]'  # поле Адрес
    INPUT_PHONE_NUMBER = By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]'  # поле Телефон

    INPUT_STATION = By.XPATH, './/div[starts-with(@class, "select-search")]'  # поле Станция метро
    METRO_STATION = By.XPATH, './/li[starts-with(@class, "select-search__row") and @data-index={}]'  # выбор метро

    INPUT_DATE = By.XPATH, './/input[@placeholder="* Когда привезти самокат"]'  # поле даты заказа

    INPUT_RENTAL_PERIOD = By.XPATH, './/div[@class="Dropdown-placeholder"]'  # поле срока аренды
    DROPDOWN_RENTAL_PERIOD = By.XPATH, './/div[text()="двое суток"]'  # выбор срока аренды

    CHECKBOX_BLACK = By.XPATH, ('.//input[starts-with(@class, "Checkbox_Input") '
                                'and @id="black"]')  # выбор чёрного цвета самоката
    CHECKBOX_GREY = By.XPATH, ('.//input[starts-with(@class, "Checkbox_Input") '
                               'and @id="grey"]')  # выбор серого цвета самоката

    INPUT_COMMENT = By.XPATH, './/input[@placeholder="Комментарий для курьера"]'  # поле Комментарий для курьера

    BUTTON_NEXT = By.XPATH, ('.//div[starts-with(@class, "Order_NextButton")]'
                             '/button[text()="Далее"]')  # кнопка "Далее"
    BUTTON_ORDER = By.XPATH, ('.//div[starts-with(@class, "Order_Buttons")]'
                              '/button[text()="Заказать"]')  # кнопка "Заказать"
    BUTTON_APPROVE_ORDER = By.XPATH, ('.//div[starts-with(@class, "Order_Modal")]'
                                      '/div[starts-with(@class, "Order_Buttons")]'
                                      '/button[text()="Да"]')  # кнопка "Да"

    HEADER_ORDER_INFORMATION = By.XPATH, ('.//div[starts-with(@class, "Order_Modal")]'
                                          '/div[starts-with(@class, "Order_ModalHeader")]')  # заголовок модального окна о созданном заказе
