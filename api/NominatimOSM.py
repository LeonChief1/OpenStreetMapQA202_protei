import requests
import allure
import pytest


class NominatimOSM:

    @allure.step("URL: {base_url}")
    def __init__(self, base_url: str, api_context: dict = None) -> None:
        self.base_url = base_url
        self.api_context = api_context

    @allure.step("Запрос статуса сервера в формате json")
    def get_status_Nominatim_json(self, headers: dict = None) -> dict:

        """Функция получения статуса сервера Nominatim в формате json"""

        path = "{nominatim}status?format=json".format(nominatim=self.base_url)
        resp = requests.get(path, headers=headers)
        if self.api_context is not None:
            self.api_context["response"] = resp

        allure.attach(f"Ответ {resp}", name="Код ответа", attachment_type=allure.attachment_type.TEXT)

        return resp.json()

    @allure.step("Запрос статуса сервера в формате text")
    def get_status_Nominatim_text(self, headers: dict = None) -> str:

        """Функция получения статуса сервера Nominatim в формате text"""

        path = "{nominatim}status?format=text".format(nominatim=self.base_url)
        resp = requests.get(path, headers=headers)
        if self.api_context is not None:
            self.api_context["response"] = resp
        allure.attach(f"Ответ {resp}", name="Код ответа", attachment_type=allure.attachment_type.TEXT)

        return resp.text

    @allure.step("Поиск в параметризации по параметрам: {q}, {format}, {polygon}, {addressdetails}, {limit}")
    def get_search_parametrize(self, q: str, format: str, polygon: int, addressdetails: int, limit: int, headers: dict = None) -> dict:

        """Функция поиска по параметризации и получения ответа в json/xml"""

        params = {
            'q': q,
            'format': format,
            'polygon': polygon,
            'addressdetails': addressdetails,
            'limit': limit
        }

        path = "{nominatim}search?".format(nominatim=self.base_url)
        resp = requests.get(path, headers=headers, params=params)
        if self.api_context is not None:
            self.api_context["response"] = resp
        allure.attach(f"Ответ {resp}", name="Код ответа", attachment_type=allure.attachment_type.TEXT)

        if format == 'xml':
            return resp.text
        else:
            return resp.json()

    @allure.step("Реверс с параметризациией по парамтерам: {format}, {lat}, {lon}, {zoom}. {addressdetails}")
    def get_reverse_parametrize(self, format: str, lat: int, lon: int, zoom: int, addressdetails: int, headers: dict = None) -> dict:

        """Функция реверса по параметризации и получения ответа в json/xml"""

        params = {
            'format': format,
            'lat': lat,
            'lon': lon,
            "zoom": zoom,
            'addressdetails': addressdetails
        }

        path = "{nominatim}reverse?".format(nominatim=self.base_url)
        resp = requests.get(path, headers=headers, params=params)
        if self.api_context is not None:
            self.api_context["response"] = resp
        allure.attach(f"Ответ {resp}", name="Код ответа", attachment_type=allure.attachment_type.TEXT)

        if format == 'xml':
            return resp.text
        else:
            return resp.json()