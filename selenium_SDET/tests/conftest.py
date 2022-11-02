import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options

from selenium.webdriver.common.by import By


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('options')
    options.add_argument('--start_maximized')
    return options

@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://vk.com/id540631030'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()

