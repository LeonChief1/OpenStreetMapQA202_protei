import allure
import time
import pytest
from pages.base_page import NominatimPage


# @allure.feature("Карта")
# @allure.story("Взаимодействие с картой")
# def test_osm_fullscreen_interaction(driver):
#     page = NominatimPage(driver)
#
#     page.open()
#
#     page.click_advanced_options()
#     page.click_wright_search('canada')
#     page.click_search()
#     page.wait_until_loaded_safe()
#
#     with allure.step("Проверка заголовка"):
#         assert "Nominatim" in driver.title


@allure.epic("ui_nominatim_test")
@allure.severity("blocker")
@allure.story("Проверка сайта на поисковик через pyautogui")
@allure.title("проверка на поиск")
@pytest.mark.usefixtures("browser")
@pytest.mark.parametrize('country', [
    ('New-Yourk'),
    ('Barbados'),
    ('Tuvalu'),
    ('Chile'),
    ('Afghanistan'),
    ('Honduras'),
    ('Test'),
    (' '),
    ('BARBADOS'),
    ('barbados'),
    ('bar#bados'),
    ('barbados1'),
    ('bar2bados'),
    ('A' * 100),
])
def test_ui_nominatim_test_search_pyautogui(browser, country):

    page = NominatimPage(browser)
    page.open()
    page.wait_url()
    page.click_advanced_options()
    page.set_eng_layout()
    page.click_wright_search(country)
    page.click_search()
    current_url = page.get_current_url()
    page.is_no_results_displayed()
    page.check_no_results()

    with allure.step(f"Проверить, что URL содержит параметр поиска для '{country}'"):
        from urllib.parse import unquote
        decoded_url = unquote(current_url)
        assert "ui/search.html" in current_url
        assert f"q={country}" in decoded_url, f"Поисковый запрос '{country}' не найден в URL: {decoded_url}"

    page.set_ru_eng_layout()