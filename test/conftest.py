import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from configuration.ConfigProvired import ConfigProvider


@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):

        timeout = ConfigProvider().getint("ui", "timeout")
        browser_name = ConfigProvider().get("ui", "browser_name")

        driver = None

        if browser_name == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.binary_location = "/usr/bin/chromium-gost"
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Chrome(options=chrome_options)
        else:
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()))

        driver.implicitly_wait(timeout)
        driver.maximize_window()
        yield driver

    with allure.step("Закрыть браузер"):
        driver.quit()