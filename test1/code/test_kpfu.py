import pytest
import info
from base import BaseCase
from selenium.webdriver.common.by import By
import locators


class TestKpfu(BaseCase):
    @pytest.mark.UI
    def test_login(self):
        self.browser.get("https://kpfu.ru/")
        self.login()
        self.wait(2)
        assert self.browser.find_element(by=By.XPATH, value=locators.LOGO_NAME)

    @pytest.mark.UI
    def test_logout(self):
        self.browser.get("https://kpfu.ru/")
        self.login()
        self.wait(2)
        assert self.browser.find_element(by=By.XPATH, value=locators.LOGO_NAME)
        self.logout()
        self.wait(2)
        assert self.browser.current_url == 'https://kpfu.ru/'

    @pytest.mark.UI
    def test_change_status(self):
        status = self.generate_value(0, 100, False)
        self.browser.get("https://kpfu.ru/")
        self.login()
        self.wait(2)
        assert self.browser.find_element(by=By.XPATH, value=locators.LOGO_NAME)

        self.click_when_loaded(locators.PORTFOLIO_BUTTON)
        self.click_when_loaded(locators.PORTFOLIO_EDIT_BUTTON)
        self.click_when_loaded(locators.STATUS_INPUT)
        self.clear_field(locators.STATUS_INPUT)
        self.send_keys(locators.STATUS_INPUT, status)
        self.click(locators.STATUS_SAVE_BUTTON)
        self.browser.refresh()
        self.wait(2)
        assert status == self.attribute_text_value(locators.STATUS_INFO)

    @pytest.mark.UI
    @pytest.mark.parametrize("username, passwrd",
                             [(info.login, info.password,),
                              (info.login_false, info.password_false,)])
    def test_change_login(self, username, passwrd):
        self.browser.get("https://kpfu.ru/")
        self.wait(3)
        self.click_when_loaded(locators.LOGIN_PAGE_BUTTON)
        self.send_keys(locators.LOGIN_FIELD, username)
        self.send_keys(locators.PASSWORD_FIELD, passwrd)
        self.click(locators.LOGIN_BUTTON)
        self.wait(2)
        assert self.browser.find_element(by=By.XPATH, value=locators.LOGO_NAME)




