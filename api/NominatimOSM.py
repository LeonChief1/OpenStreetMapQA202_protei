import requests
import allure
import pytest


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


    def get_search_parametrize(self, q, format, polygon, addressdetails, limit, headers: dict = None) -> dict:

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


    def get_reverse_parametrize(self, format, lat, lon, zoom, addressdetails, headers: dict = None) -> dict:

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