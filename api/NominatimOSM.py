import requests
import allure
import pytest


class NominatimOSM:

    @allure.step("URL: {base_url}")
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    @allure.step("Запрос статуса сервера в формате json")
    def get_status_Nominatim_json(self, headers: dict = None) -> dict:

        path = "{nominatim}status?format=json".format(nominatim=self.base_url)
        resp = requests.get(path, headers=headers)
        resp.raise_for_status()

        return resp.json()

    @allure.step("Запрос статуса сервера в формате text")
    def get_status_Nominatim_text(self, headers: dict = None) -> str:

        path = "{nominatim}status?format=text".format(nominatim=self.base_url)
        resp = requests.get(path, headers=headers)
        resp.raise_for_status()

        return resp.text

    @allure.step("Поиск в параметризации по параметрам: {q}, {format}, {polygon}, {addressdetails}, {limit}")
    def get_search_parametrize(self, q: str, format: str, polygon: int, addressdetails: int, limit: int, headers: dict = None) -> dict:

        params = {
            'q': q,
            'format': format,
            'polygon': polygon,
            'addressdetails': addressdetails,
            'limit': limit
        }

        path = "{nominatim}search?".format(nominatim=self.base_url)
        resp = requests.get(path, headers=headers, params=params)
        resp.raise_for_status()

        if format == 'xml':
            return resp.text
        else:
            return resp.json()

    @allure.step("Реверс с параметризациией по парамтерам: {format}, {lat}, {lon}, {zoom}. {addressdetails}")
    def get_reverse_parametrize(self, format: str, lat: int, lon: int, zoom: int, addressdetails: int, headers: dict = None) -> dict:

        params = {
            'format': format,
            'lat': lat,
            'lon': lon,
            "zoom": zoom,
            'addressdetails': addressdetails
        }

        path = "{nominatim}reverse?".format(nominatim=self.base_url)
        resp = requests.get(path, headers=headers, params=params)
        resp.raise_for_status()

        if format == 'xml':
            return resp.text
        else:
            return resp.json()