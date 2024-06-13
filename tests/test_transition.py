from pages.header import Header
from pages.transition import Transition

from conftest import driver


class TestTransition:
    def test_transition_to_main_from_order_page(self, driver):
        transition = Transition(driver)
        header = Header(driver)
        header.click_to_order_button_in_header()
        transition.click_to_logo_scooter()

        assert 'Самокат' in transition.get_main_header()

    def test_transition_to_dzen_from_logo(self, driver):
        transition = Transition(driver)
        transition.click_to_logo_yandex()

        assert transition.open_dzen_page() == 'Найти'
