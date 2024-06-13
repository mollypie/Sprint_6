import pytest

from selenium import webdriver
from pages import *


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get('https://qa-scooter.praktikum-services.ru/')

    yield driver

    driver.quit()
