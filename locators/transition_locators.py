from selenium.webdriver.common.by import By


class TransitionLocators:
    LOGO_DZEN = By.XPATH, './/div[starts-with(@class, "desktop-base-header__logoContainer-pu")'  # лого Дзен
    BUTTON_SEARCH = By.XPATH, './/button[@class="dzen-search-arrow-common__button"]'  # кнопка "Поиск" в поисковой строке
