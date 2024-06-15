from selenium.webdriver.common.by import By


class HeaderLocators:
    BUTTON_ORDER_HEADER = By.XPATH, ('.//div[starts-with(@class, "Header_Nav")]'
                                     '/button[text()="Заказать"]')  # кнопка "Заказать"
    LOGO_YANDEX = By.XPATH, './/a[starts-with(@class, "Header_LogoYandex")]'  # логотип «Яндекс»
    LOGO_SCOOTER = By.XPATH, './/a[starts-with(@class, "Header_LogoScooter")]'  # логотип «Самоката»
