import pytest
from selenium.webdriver.chrome.options import Options
from selene import browser
from utils import attaches


@pytest.fixture(autouse=True)
def browser_management():
    options = Options()
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")

    browser.config.driver_options = options
    browser.config.base_url = 'https://mwi.me/'
    browser.config.timeout = 10

    yield

    if browser.driver:
        attaches.add_screenshot(browser.driver)
        attaches.add_page_source(browser.driver)
        attaches.add_logs(browser.driver)

    browser.quit()