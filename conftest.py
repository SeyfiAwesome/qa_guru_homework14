import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser

from utils import attaches


@pytest.fixture(scope="function", autouse=True)
def browser_management():

    options = Options()
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--window-size=1920,1080")

    if os.getenv("REMOTE"):
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "128.0")
        options.set_capability(
            "selenoid:options",
            {
                "enableVNC": True
            }
        )

        driver = webdriver.Remote(
            command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
            options=options
        )

    else:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)

    browser.config.driver = driver
    browser.config.base_url = "https://mwi.me/"
    browser.config.timeout = 10

    yield

    attaches.add_screenshot(browser.driver)
    attaches.add_page_source(browser.driver)
    attaches.add_logs(browser.driver)

    browser.quit()