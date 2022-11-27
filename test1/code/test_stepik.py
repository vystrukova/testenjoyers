import pytest
import info
from base import BaseCase
from selenium.webdriver.common.by import By
import locators


class TestStepik(BaseCase):
    @pytest.mark.UI
    def test_login(self):
        self.browser.get("https://stepik.org/catalog")
        self.login_stepik()
        self.wait(2)
        assert self.browser.current_url == 'https://stepik.org/catalog?auth=login'

    @pytest.mark.UI
    def test_email_checker(self):
        email = self.generate_email_value(5, 15, True)
        self.browser.get("https://stepik.org/catalog")
        self.login_stepik()
        self.wait(2)
        assert self.browser.find_element(by=By.XPATH, value=locators.STEPIK_IMAGE_BUTTON)

        self.browser.get('https://stepik.org/edit-profile/email')
        self.wait(2)
        self.click_when_loaded(locators.STEPIK_NEW_EMAIL)
        self.send_keys(locators.STEPIK_NEW_EMAIL, email)
        self.click(locators.STEPIK_BUTTON_ADD_EMAIL)
        assert self.check_visibility(locators.STEPIK_BUTTON_NEW_EMAIL)
        self.click(locators.STEPIK_BUTTON_DELETE_EMAIL)
        self.wait(2)
        #лишний assert
        assert self.check_visibility(locators.STEPIK_BUTTON_NEW_EMAIL)

    @pytest.mark.UI
    @pytest.mark.parametrize("range_start, range_finish, email_only",
                             [(5, 15, True),
                              (5, 15, False)])
    def test_email_parametrize(self, range_start, range_finish, email_only):
        email = self.generate_email_value(range_start, range_finish, email_only)
        self.browser.get("https://stepik.org/catalog")
        self.login_stepik()
        self.wait(2)
        assert self.browser.find_element(by=By.XPATH, value=locators.STEPIK_IMAGE_BUTTON)

        self.browser.get('https://stepik.org/edit-profile/email')
        self.wait(2)
        self.click_when_loaded(locators.STEPIK_NEW_EMAIL)
        self.send_keys(locators.STEPIK_NEW_EMAIL, email)
        self.click(locators.STEPIK_BUTTON_ADD_EMAIL)
        assert self.check_visibility(locators.STEPIK_BUTTON_NEW_EMAIL)
        self.click(locators.STEPIK_BUTTON_DELETE_EMAIL)
        self.wait(1)
        # лишний assert
        assert self.check_visibility(locators.STEPIK_BUTTON_NEW_EMAIL)




