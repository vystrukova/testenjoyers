import time

import pytest
from selenium.webdriver import Chrome
from locators import BasePageLocators
from locators import LoginPageLocators
from locators import MainPageLocators
from base_page import BasePage
import main_page
import info


class LoginPage(BasePage):

    def __init__(self, browser):
        self.locators = LoginPageLocators
        self.browser: Chrome = browser
        self.url = info.url
        super().__init__(browser)

    """Открывает страницу в браузере"""
    def open(self):
        self.browser.get(self.url)
        return self

    """Проверяем что страница открыта"""
    def page_is_open(self, timeout):
        locator = self.locators.PIKABU_FORM_LOGIN_BUTTON
        for _ in range(timeout):
            if self.is_visible(locator, timeout):
                return True
            time.sleep(0.5)
        return False