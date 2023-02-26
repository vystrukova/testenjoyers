import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    browser = webdriver.Chrome(chrome_options=options, service=Service(ChromeDriverManager().install()))

    browser.maximize_window()
    yield browser
    browser.quit()