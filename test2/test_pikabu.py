import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.main_page import MainPage


class TestPikabu():
    @pytest.mark.UI
    def test_open(self, browser):
        page = MainPage(browser=browser).is_open()
        assert page.page_is_open(timeout=5) is True


