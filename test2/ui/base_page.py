import time

import pytest

import info
from base_case import BaseCase
from locators import BasePageLocators
from selenium.webdriver import Chrome


class BasePage(BaseCase):

    @pytest.fixture(autouse=True)
    def __init__(self, browser):
        self.locators = BasePageLocators
        self.browser: Chrome = browser
        self.url = info.url
        super().__init__(browser)

    """Открывает страницу в браузере"""
    @pytest.fixture()
    def open(self):
        self.browser.get(self.url)
        return self

    """Проверяем что страница открыта"""
    @pytest.fixture()
    def is_open(self, timeout):
        locator = self.locators.PIKABU_LOGO_HOME
        for _ in range(timeout):
            if self.is_visible(locator, timeout):
                return True
            time.sleep(0.5)
        return False