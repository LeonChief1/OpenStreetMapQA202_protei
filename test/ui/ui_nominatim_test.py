from time import sleep

import pytest

import allure
from pages.MainPage import MainPage


@allure.epic("ui_nominatim_test")
@allure.severity("blocker")
@allure.feature("nominatim")
@allure.story("Проверка сайта на поисковик")
@allure.title("проверка на поиск")
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
def ui_nominatim_test(browser, country):

    main_page = MainPage(browser)
    main_page.go()
    main_page.advanced_options()
    main_page.search_input(country)
    main_page.click_search_button()
    current_url = main_page.get_current_url()
    main_page.save_screenshot(country)

    with allure.step(f"Проверить, что URL содержит параметр поиска для '{country}'"):
        assert "ui/search.html" in current_url, f"URL должен содержать 'ui/search.html'"
        assert f"q={country}" in current_url, f"URL должен содержать 'q={country}'"