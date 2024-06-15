import pytest

from selenium import webdriver

from pages_url import MAIN_PAGE


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(MAIN_PAGE)

    yield driver

    driver.quit()
