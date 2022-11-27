import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument('--no-sandbox')  # avoid ci crash
chrome_options.add_argument('--disable-gpu')  # avoid ci crash
chrome_options.add_argument('--disable-dev-shm-usage')  # avoid ci crash (can add more shm-size in runner instead)


@pytest.fixture()
def browser():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    browser.maximize_window()
    yield browser
    browser.quit()


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "UI: mark test to run only UI tests"
    )
    config.addinivalue_line(
        "markers", "skip: mark test to skip"
    )
