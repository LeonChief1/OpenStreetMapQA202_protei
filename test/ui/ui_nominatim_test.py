import time
from time import sleep

import allure
from pages.MainPage import MainPage


@allure.epic("ui_nominatim_test")
@allure.severity("blocker")
@allure.feature("nominatim")
@allure.story("Проверка сайта на поисковик")
@allure.title("проверка на поиск")
def ui_nominatim_test(browser, test_data: dict):

    main_page = MainPage(browser)
    main_page.go()
    main_page.advanced_options()
    main_page.search_input("New-Yourk")
    main_page.click_search_button()
    current_url = main_page.get_current_url()
    with allure.step("Проверить, что URL " + current_url + "заканчивается на ui/search.html?q=New-Yourk"):
        assert current_url.endswith("ui/search.html?q=New-Yourk")
