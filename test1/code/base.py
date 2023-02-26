import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import info
import pytest
import locators
import random


class BaseCase:
    browser = None

    @pytest.fixture(autouse=True, scope="function")
    def setup(self, browser):
        self.browser = browser

    def login(self):
        """Авторизуется в KPFU"""
        self.wait(3)
        self.click_when_loaded(locators.LOGIN_PAGE_BUTTON)
        self.send_keys(locators.LOGIN_FIELD, info.login)
        self.send_keys(locators.PASSWORD_FIELD, info.password)
        self.click(locators.LOGIN_BUTTON)

    def login_stepik(self):
        """Авторизуется в Stepik"""
        self.wait(3)
        self.click_when_loaded(locators.STEPIK_LOGIN_PAGE_BUTON)
        self.send_keys(locators.STEPIK_LOGIN_FIELD, info.login_stepik)
        self.send_keys(locators.STEPIK_PASSWORD_FIELD, info.password_stepik)
        self.click(locators.STEPIK_LOGIN_BUTTON)

    def logout(self):
        self.click_when_loaded(locators.LOGOUT_BUTTON)
        self.wait(2)

    def click(self, locator, timeout=3):
        self.mouse_over(locator, timeout)
        WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable((By.XPATH, locator))).click()

    def click_long(self, locator, timeout=5):
        """Ждет появления элемента в DOM, а затем его кликабельности"""
        WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located((By.XPATH, locator)))
        WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable((By.XPATH, locator))).click()

    def click_when_loaded(self, locator, timeout_for_click=5, timeout_for_wait=3, retries_spinner=2,
                          retries_no_spinner=4):
        if self.page_is_loaded(timeout_for_wait, retries_spinner, retries_no_spinner):
            WebDriverWait(self.browser, timeout_for_click).until(
                EC.presence_of_element_located((By.XPATH, locator)))
            WebDriverWait(self.browser, timeout_for_click).until(
                EC.element_to_be_clickable((By.XPATH, locator))).click()
        else:
            raise selenium.common.exceptions.TimeoutException

    def send_keys(self, locator, text, timeout=2):
        WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable((By.XPATH, locator))).send_keys(text)

    def wait(self, time):
        self.browser.implicitly_wait(time)

    def clear_field(self, locator, timeout=2):
        """Делает выбранное поле пустым"""
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        element.clear()

    def attribute_value(self, locator, attribute_name, timeout=2):
        """Возвращает значение выбранного атрибута у указанного элемента"""
        element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))
        return element.get_attribute(attribute_name)

    def attribute_text_value(self, locator, timeout=2):
        """Возвращает ТЕКСТ элемента"""
        element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))
        return element.text

    def check_visibility(self, locator, timeout=2):
        """Проверяет видимость указанного элемента.
           Возвращает True, если элемент видно и False, если элемент не видно."""
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except selenium.common.exceptions.TimeoutException:
            return False

    def generate_value(self, range_start, range_finish, numbers_only):
        data = "АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ абвгдеёжзиклмнопрстуфхцчшщъыьэюя"
        length = random.randint(range_start, range_finish)  # Generates random input`s length
        value = ""

        if numbers_only:  # Switches generator to numbers only mode
            data = "1234567890"

        for i in range(length):
            value += random.choice(data)

        return value.strip()  # обрезает пробелы в начале и в конце

    def generate_email_value(self, range_start, range_finish, email_only):
        """Generate email"""
        data = "abcdefghijklmnopqrstuvwxyz"
        length = random.randint(range_start, range_finish)
        value = ""

        for i in range(length):
            value += random.choice(data)

        if email_only:
            value = value + '@gmail.com'

        return value.strip()


    def mouse_over(self, locator, timeout=2):
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        ActionChains(self.browser).move_to_element(element).perform()

    def page_is_loaded(self, timeout, range1, range2):
        """Ждет завершения загрузки страницы"""
        for i in range(range1):
            print(f"APPEARED {i}")
            try:
                WebDriverWait(self.browser, timeout).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, '.spinner')))
                for j in range(range2):
                    print(f"DISAPPEARED {j}")
                    try:
                        WebDriverWait(self.browser, timeout).until(
                            EC.invisibility_of_element_located((By.CSS_SELECTOR, '.spinner')))
                        return True
                    except:
                        if j == range2 - 1:
                            return False
                        pass
            except:
                if i == range1 - 1:
                    return True
                pass
