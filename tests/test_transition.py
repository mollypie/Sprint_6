import allure

from pages.header import Header
from pages.main_page import MainPage
from pages.transition import Transition

from conftest import driver


class TestTransition:
    @allure.title('Переход на главную страницу со страницы заказа по клику на лого "Самокат"')
    def test_transition_to_main_from_order_page(self, driver):
        header = Header(driver)
        main_page = MainPage(driver)
        header.click_to_order_button_in_header()
        header.click_to_logo_scooter()

        assert 'Самокат' in main_page.get_main_header()

    @allure.title('Редирект на страницу Дзена по клику на лого "Яндекс"')
    def test_transition_to_dzen_from_logo(self, driver):
        transition = Transition(driver)
        header = Header(driver)
        header.click_to_logo_yandex()

        assert transition.open_dzen_page() == 'Найти'
