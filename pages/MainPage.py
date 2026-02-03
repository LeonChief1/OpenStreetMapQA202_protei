import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configuration.ConfigProvired import ConfigProvider
from test_data.DataProvider import DataProvider


class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.url = ConfigProvider().get_ui_url()
        self.data = DataProvider().get_user_agent()
        self.data = DataProvider().get_accept()

    @allure.step("Перейти на страницу Nominatim")
    def go(self):
        self.__driver.get(self.url)

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.__driver.current_url

    @allure.step("Открыть дополнительные настройки")
    def advanced_options(self):
        self.__driver.find_element(By.CSS_SELECTOR, "#searchAdvancedOptions").click()

    @allure.step("Написать слово в поисковике {country}")
    def search_input(self, country):
        self.__driver.find_element(By.CSS_SELECTOR, "#q").send_keys(country)

    @allure.step("Нажать поиск")
    def click_search_button(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-sm").click()
        WebDriverWait(self.__driver, 4).until(EC.url_contains(self.url + "ui/search.html?q="))
