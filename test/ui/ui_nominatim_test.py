from time import sleep

import pytest

import allure
from pages.MainPage import MainPage


@allure.epic("ui_nominatim_test")
@allure.severity("blocker")
@allure.story("Проверка сайта на поисковик")
@allure.title("проверка на поиск")
@pytest.mark.usefixtures("browser")
@pytest.mark.skip()
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
def ui_nominatim_test_search(browser, country):

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


@allure.epic("ui_nominatim_test")
@allure.severity("blocker")
@allure.story("Проверка сайта на revers")
@allure.title("проверка на reverse")
@pytest.mark.usefixtures("browser")
@pytest.mark.parametrize('lat, lon, zoom', [
    ('-9.911374', '-53.580959', 0),
    ('82.689336', '-31.809395', 1),
    ('-24.743005', '-32.115876', 2),
    ('10.239005', '35.390495', 3),
    ('-37.164761', '45.394554', 4),
    ('82.689336', '-32.115876', 5),
    ('-24.743005', '35.390495', 6),
    ('10.239005', '45.394554', 7),
    ('-37.164761', '-53.580959', 8),
    ('-9.911374', '-31.809395', 9),
    ('-24.743005', '45.394554', 10),
    ('10.239005', '-53.580959', 11),
    ('-37.164761', '-31.809395', 12),
    ('-9.911374', '-32.115876', 13),
    ('82.689336', '35.390495', 14),
    ( '10.239005', '-31.809395', 15),
    ('-37.164761', '-32.115876', 16),
    ('-9.911374', '35.390495', 17),
    ('82.689336', '45.394554', 18),
    ('82.689336', '45.394554', 19),
])
def ui_nominatim_test_reverse(browser, lat, lon, zoom):

    main_page = MainPage(browser)
    main_page.go()
    main_page.go_to_reverse()
    main_page.reverse_input_lat(lat)
    main_page.reverse_input_lon(lon)
    main_page.reverse_input_zoom(zoom)
    main_page.advanced_options()
    main_page.click_reverse_button()
    current_url = main_page.get_current_url()
    screenshot_name = f"lat_{lat}_lon_{lon}_zoom_{zoom}"
    main_page.save_screenshot(screenshot_name)

    with allure.step(f"Проверить, что URL содержит параметр поиска для '{lat, lon, zoom}'"):
        assert "ui/reverse.html" in current_url, f"URL должен содержать 'ui/reverse.html'"
        assert f"lat={lat}" in current_url, f"URL должен содержать 'lat={lat}'"
        assert f"lon={lon}" in current_url, f"URL должен содержать 'lon={lon}'"
        assert f"zoom={int(zoom) - 2}" in current_url, f"URL должен содержать 'zoom={zoom}'"