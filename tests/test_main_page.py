import allure
import pytest

from conftest import driver
from data import *

from pages.main_page import MainPage


class TestMainPage:
    @allure.title('Проверка ответов на вопросы в разделе FAQ')
    @pytest.mark.parametrize(
        'num, result',
        [
            (0, ANSWER_TEXT_PRICE),
            (1, ANSWER_TEXT_COUNT),
            (2, ANSWER_TEXT_TIME),
            (3, ANSWER_TEXT_DATE),
            (4, ANSWER_TEXT_EXTEND),
            (5, ANSWER_TEXT_CHARGER),
            (6, ANSWER_TEXT_CANCEL),
            (7, ANSWER_TEXT_LOCATION)
        ]
    )
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)

        assert main_page.get_answer_text(num) == result
