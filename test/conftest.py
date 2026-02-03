import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

from configuration.ConfigProvired import ConfigProvider
from api.NominatimOSM import NominatimOSM
from test_data.DataProvider import DataProvider


@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):

        timeout = ConfigProvider().getint("ui", "timeout")
        browser_name = ConfigProvider().get("ui", "browser_name")

        driver = None

        if browser_name == 'chrome':
            chrome_options = Options()
            chrome_options.binary_location = "/usr/bin/chromium-gost"
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            service = Service("/usr/local/bin/chromedriver_127")
            driver = webdriver.Chrome(service=service, options=chrome_options)
        else:
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()))

        driver.implicitly_wait(timeout)
        driver.maximize_window()
        yield driver

    with allure.step("Закрыть браузер"):
        driver.quit()


@pytest.fixture
def api_client() -> NominatimOSM:
    return NominatimOSM(
        ConfigProvider().get_api_url()
    )

@pytest.fixture
def test_data():
    return DataProvider()