import requests
import allure
from selenium.webdriver.support.expected_conditions import none_of
from ssh_import_id import user_agent
from test_data.DataProvider import  DataProvider


class NominatimOSM:

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def get_status_Nominatim_json(self, headers: dict = None) -> dict:

        path = "{nominatim}status?format=json".format(nominatim=self.base_url)
        resp = requests.get(path, headers=headers)
        resp.raise_for_status()

        return resp.json()

    def get_status_Nominatim_text(self, headers: dict = None) -> str:

        path = "{nominatim}status?format=text".format(nominatim=self.base_url)
        resp = requests.get(path, headers=headers)
        resp.raise_for_status()

        return resp.text