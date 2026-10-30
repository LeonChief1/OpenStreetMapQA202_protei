import requests
import allure


class NominatimOSM:

    @allure.step("URL: {base_url}")
    def __init__(self, base_url: str, api_context: dict = None, headers: dict = None) -> None:
        self.base_url = base_url
        self.api_context = api_context
        self.default_headers = headers

    @allure.step("Запрос статуса сервера в формате json")
    def get_status_Nominatim_json(self) -> dict:

        """Функция получения статуса сервера Nominatim в формате json"""

        path = "{nominatim}status?format=json".format(nominatim=self.base_url)
        head = self.default_headers
        resp = requests.get(path, headers=head, timeout=(5, 30))
        if self.api_context is not None:
            self.api_context["response"] = resp

        allure.attach(f"Ответ {resp}", name="Код ответа", attachment_type=allure.attachment_type.TEXT)

        return resp.json()

    @allure.step("Запрос статуса сервера в формате text")
    def get_status_Nominatim_text(self) -> str:

        """Функция получения статуса сервера Nominatim в формате text"""

        path = "{nominatim}status?format=text".format(nominatim=self.base_url)
        head = self.default_headers
        resp = requests.get(path, headers=head, timeout=(5, 30))
        if self.api_context is not None:
            self.api_context["response"] = resp
        allure.attach(f"Ответ {resp}", name="Код ответа", attachment_type=allure.attachment_type.TEXT)

        return resp.text

    @allure.step("Поиск в параметризации по параметрам: {q}, {format}, {polygon}, {addressdetails}, {limit}")
    def get_search_parametrize(self, q: str, format: str, polygon: int, addressdetails: int, limit: int) -> dict:

        """Функция поиска по параметризации и получения ответа в json/xml"""

        params = {
            'q': q,
            'format': format,
            'polygon': polygon,
            'addressdetails': addressdetails,
            'limit': limit
        }

        path = "{nominatim}search?".format(nominatim=self.base_url)
        head = self.default_headers
        resp = requests.get(path, headers=head,params=params, timeout=(5, 30))
        if self.api_context is not None:
            self.api_context["response"] = resp
        allure.attach(f"Ответ {resp}", name="Код ответа", attachment_type=allure.attachment_type.TEXT)

        if resp.status_code != 200:
            return resp.status_code, {"error": True, "status_code": resp.status_code, "message": resp.text}

        if format.lower().strip() in ('json', 'jsonv2', 'geojson', 'geocodejson'):
            try:
                return resp.status_code, resp.json()
            except requests.exceptions.JSONDecodeError:
                return resp.status_code, resp.text

        return resp.status_code, resp.text

    @allure.step("Реверс с параметризациией по парамтерам: {format}, {lat}, {lon}, {zoom}. {addressdetails}")
    def get_reverse_parametrize(self, format: str, lat: int, lon: int, zoom: int, addressdetails: int) -> dict:

        """Функция реверса по параметризации и получения ответа в json/xml"""

        params = {
            'format': format,
            'lat': lat,
            'lon': lon,
            "zoom": zoom,
            'addressdetails': addressdetails,
        }

        path = "{nominatim}reverse?".format(nominatim=self.base_url)
        head = self.default_headers
        resp = requests.get(path, headers=head,params=params, timeout=(5, 30))
        if self.api_context is not None:
            self.api_context["response"] = resp
        allure.attach(f"Ответ {resp}", name="Код ответа", attachment_type=allure.attachment_type.TEXT)

        if resp.status_code != 200:
            return resp.status_code, {"error": True, "status_code": resp.status_code, "message": resp.text}

        if format.lower().strip() in ('json', 'jsonv2', 'geojson', 'geocodejson'):
            try:
                return resp.status_code, resp.json()
            except requests.exceptions.JSONDecodeError:
                return resp.status_code, resp.text

        return resp.status_code, resp.text