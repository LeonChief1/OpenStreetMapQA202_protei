import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configuration.ConfigProvired import ConfigProvider
from test_data.DataProvider import DataProvider


class MainPage:

    def __init__(self, driver: WebDriver):
        """Конструктор"""
        self.__driver = driver
        self.url = ConfigProvider().get_ui_url()
        self.data = DataProvider().get_user_agent()
        self.data = DataProvider().get_accept()

    @allure.step("Перейти на страницу Nominatim")
    def go(self) -> None:
        '''Функция к переходу на страницу'''
        self.__driver.get(self.url)

    @allure.step("Перейти на страницу reverse Nominatim")
    def go_to_reverse(self) -> None:
        '''Функция к переходу на страницу reverse'''
        self.__driver.find_element(By.CSS_SELECTOR, "a[href='reverse.html']").click()

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        '''Функция получения текущего URL страницы'''
        current_url = self.__driver.current_url

        allure.attach(
            current_url,
            name="страница",
            attachment_type=allure.attachment_type.URI_LIST
        )
        return current_url

    @allure.step("Открыть дополнительные настройки")
    def advanced_options(self) -> None:
        '''Функция открытия дополнительных настроек на странице Nominatim'''
        self.__driver.find_element(By.CSS_SELECTOR, "#searchAdvancedOptions").click()

    @allure.step("Написать слово в поисковике {country}")
    def search_input(self, country) -> None:
        '''Функция написания слова в поисковик поля search на странице Nominatim'''
        self.__driver.find_element(By.CSS_SELECTOR, "#q").send_keys(country)

    @allure.step("Нажать поиск")
    def click_search_button(self) -> None:
        '''Функция нажатия на кнопку поиска'''
        self.__driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-sm").click()
        WebDriverWait(self.__driver, 4).until(EC.url_contains(self.url + "ui/search.html?q="))

    @allure.step("Выполняем скрпиншот {screenshot_name}")
    def save_screenshot(self, screenshot_name):
        '''Функция скриншота в allure'''
        screenshot = self.__driver.get_screenshot_as_png()

        allure.attach(
            screenshot,
            name=screenshot_name,
            attachment_type=allure.attachment_type.PNG
        )

        return screenshot

    @allure.step("Написать щироту {lat}")
    def reverse_input_lat(self, lat) -> None:
        '''Функция написания широты в поисковик поля reverse на странице Nominatim'''
        self.__driver.find_element(By.CSS_SELECTOR, "#reverse-lat").send_keys(lat)

    @allure.step("Написать долготы {lon}")
    def reverse_input_lon(self, lon) -> None:
        '''Функция написания долготы в поисковик поля reverse на странице Nominatim'''
        self.__driver.find_element(By.CSS_SELECTOR, "#reverse-lon").send_keys(lon)

    @allure.step("Выбор зума из котекстного меню {zoom}")
    def reverse_input_zoom(self, zoom) -> None:
        '''Функция выбора из котекстного меню zoom Nominatim reverse'''
        self.__driver.find_element(By.CSS_SELECTOR, "#reverse-zoom").click()
        self.__driver.find_element(By.CSS_SELECTOR, f"#reverse-zoom > option:nth-child({zoom})").click()


    @allure.step("Нажать поиск")
    def click_reverse_button(self) -> None:
        '''Функция нажатия на кнопку поиска'''
        self.__driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-sm.mx-1").click()
        WebDriverWait(self.__driver, 4).until(EC.url_contains(self.url + "ui/reverse.html?lat="))