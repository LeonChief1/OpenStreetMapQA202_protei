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
def api_client(api_context) -> NominatimOSM:
    return NominatimOSM(
        ConfigProvider().get_api_url(),
        api_context
    )

@pytest.fixture
def test_data():
    return DataProvider()

@pytest.fixture
def api_context():
    return {}


def pytest_exception_interact(node, call, report):

    if report.failed and call.when == "call":

        browser = node.funcargs.get("browser")
        if browser:
            try:
                screenshot = browser.get_screenshot_as_png()
                current_url = browser.current_url

                allure.attach(
                    screenshot,
                    name=f"screenshot_{node.name}",
                    attachment_type=allure.attachment_type.PNG
                )

                allure.attach(
                    current_url,
                    name="Current URL",
                    attachment_type=allure.attachment_type.URI_LIST
                )

            except Exception:
                pass

        api_context = node.funcargs.get("api_context")
        if api_context and "response" in api_context:
            try:
                resp = api_context["response"]

                allure.attach(
                    resp.request.url,
                    name="Request URL",
                    attachment_type=allure.attachment_type.URI_LIST
                )

                allure.attach(
                    str(resp.request.headers),
                    name="Request Headers",
                    attachment_type=allure.attachment_type.TEXT
                )

                allure.attach(
                    str(resp.status_code),
                    name="Status Code",
                    attachment_type=allure.attachment_type.TEXT
                )

                allure.attach(
                    resp.text,
                    name="Response Body",
                    attachment_type=allure.attachment_type.TEXT
                )
            except Exception:
                pass