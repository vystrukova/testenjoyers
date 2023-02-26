import pytest
from base_case import BaseCase
from ui.base_page import BasePage


class TestPikabu(BaseCase):

    @pytest.mark.UI
    def test_open(self, browser):
        page = BasePage(browser=browser).open()
        assert page.page_is_open(timeout=5) is True


