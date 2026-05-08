import pyautogui
import allure
import os

from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class NominatimPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://nominatim.openstreetmap.org/ui/search.html"
        self.wait = WebDriverWait(self.driver, 0.5)
        self.loader_locator = (By.ID, "loading")

    @allure.step("Открыть страницу Nominatim")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Кликнуть в дополнительные настройки")
    def click_advanced_options(self):
        pyautogui.moveTo(122, 282, duration=0)
        pyautogui.click()

    @allure.step("Кликнуть на поле поиска и очистит/ввести текст")
    def click_wright_search(self, name):
        pyautogui.moveTo(239, 255, duration=0)
        pyautogui.click(clicks=3)
        pyautogui.press('delete')
        pyautogui.write(name, interval=0)

    @allure.step("Кликнуть на кнопку поиска")
    def click_search(self):
        pyautogui.moveTo(567, 250, duration=0)
        pyautogui.click()

    @allure.step("Ожидание открытия страницы")
    def wait_url(self) -> None:
        self.wait.until(EC.url_contains(self.url))

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        '''Функция получения текущего URL страницы'''
        current_url = self.driver.current_url

        allure.attach(
            current_url,
            name="страница",
            attachment_type=allure.attachment_type.URI_LIST
        )
        return current_url

    def set_eng_layout(self):
        os.system("setxkbmap us &> /dev/null")

    def set_ru_eng_layout(self):
        os.system("setxkbmap -layout us,ru -option grp:ctrl_alt_toggle &> /dev/null")

    def is_no_results_displayed(self):
        """Проверяет с коротким таймаутом"""
        try:
            element = WebDriverWait(self.driver, 0.5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.noresults"))
            )
            return "No search results found" in element.text
        except TimeoutException:
            return False

    def check_no_results(self):
        """Проверяет наличие результатов (падает если есть сообщение об ошибке)"""
        if self.is_no_results_displayed():
            raise AssertionError("❌ Тест провален! Найдено сообщение 'No search results found'")
        return True