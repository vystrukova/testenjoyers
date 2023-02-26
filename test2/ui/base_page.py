import pytest
import selenium
import selenium.common.exceptions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver
from selenium.common.exceptions import TimeoutException

from locators import BasePageLocators


class BasePage:

    def __init__(self, browser):
        self.base_locators = BasePageLocators
        self.browser = browser

    def mouse_over(self, locator, timeout=1):
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        ActionChains(self.browser).move_to_element(element).perform()

    def click(self, locator, timeout):
        self.mouse_over(locator, timeout)
        WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(locator)).click()
        return self

    def click_when_loaded(self, locator, timeout_for_click=2, timeout_for_wait=3,
                          retries_spinner=2, retries_no_spinner=4):
        if self.page_is_loaded(timeout_for_wait, retries_spinner, retries_no_spinner):
            WebDriverWait(self.browser, timeout_for_click).until(EC.presence_of_element_located(locator))
            WebDriverWait(self.browser, timeout_for_click).until(EC.element_to_be_clickable(locator)).click()
        else:
            raise TimeoutException

    def key_down(self):
        ActionChains(driver).key_down(Keys.DOWN)
        ActionChains(driver).key_down(Keys.ENTER)

    def send_keys(self, locator, text, timeout=5):
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout):
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        return element.text

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.browser, timeout=timeout)

    def is_visible(self, locator, timeout):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def is_attribute_value(self, text, locator, timeout):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
            WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element(locator, text))
            return True
        except:
            return False

    def page_is_loaded(self, timeout, retries_to_appear, retries_to_disappear):
        for i in range(retries_to_appear):
            try:
                WebDriverWait(self.browser, timeout).until(
                    EC.visibility_of_element_located(self.base_locators.SPINNER))
                for j in range(retries_to_disappear):
                    try:
                        WebDriverWait(self.browser, timeout).until(
                            EC.invisibility_of_element_located(self.base_locators.SPINNER))
                        return True
                    except:
                        if j == retries_to_disappear - 1:
                            return False
                        pass
            except:
                if i == retries_to_appear - 1:
                    return True
                pass


