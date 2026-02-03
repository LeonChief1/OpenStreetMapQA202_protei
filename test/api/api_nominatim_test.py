import allure
import pytest

from api.NominatimOSM import NominatimOSM


@allure.epic("openstreetmap")
@allure.severity("blocker")
class Test_Api_Nominatim_test_status:

    @allure.feature("nominatim")
    @allure.story("статус сервера")
    @allure.title("статус по json")
    def test_status_nominatim_json(self, api_client: NominatimOSM, test_data):
        headers = {
            "User-Agent": test_data.get_user_agent(),
            "Accept": test_data.get_accept()
        }

        test = api_client.get_status_Nominatim_json(headers)
        allure.attach(f"Ответ {test}", name="Состояние сервера в json формате", attachment_type=allure.attachment_type.JSON)

    @allure.feature("nominatim")
    @allure.story("статус сервера")
    @allure.title("статус по text")
    def test_status_nominatim_text(self, api_client: NominatimOSM, test_data):
        headers = {
            "User-Agent": test_data.get_user_agent(),
            "Accept": test_data.get_accept()
        }

        test = api_client.get_status_Nominatim_text(headers)
        allure.attach(f"Ответ {test}", name="Состояние сервера в текстовом формате", attachment_type=allure.attachment_type.TEXT)

@allure.epic("openstreetmap")
@allure.severity("blocker")
class Test_Api_Nominatim_test_parametrize:

    @pytest.mark.parametrize('q, format, polygon, addressdetails, limit', [
            ('Barbados', 'xml', '1', '1', '1'),
            ('Tuvalu', 'json', '0', '1', '1'),
            ('Chile', 'jsonv2', '0', '1', '1'),
            ('Afghanistan', 'geojson', '1', '1', '1'),
            ('Honduras', 'geocodejson', '1', '1', '1'),
        ])
    @allure.feature("nominatim")
    @allure.story("Прямое геокодирование по параметризации (ddt)")
    @allure.title("Получения полного списка стран по параматризации search")
    def test_search_ddt(self, api_client: NominatimOSM, test_data, q, format, polygon, addressdetails, limit):
        headers = {
            "User-Agent": test_data.get_user_agent(),
            "Accept": test_data.get_accept()
        }
        ddt = api_client.get_search_parametrize(q, format, polygon, addressdetails, limit, headers)
        allure.attach(f"Ответ {ddt}", name="Поиск параматризации", attachment_type=allure.attachment_type.JSON)


    @pytest.mark.parametrize('format, lat, lon, zoom, addressdetails', [
            ('xml', '-9.911374', '-53.580959', '18', '1'),
            ('json', '82.689336', '-31.809395', '50', '1'),
            ('jsonv2', '-24.743005', '-32.115876', '30', '1'),
            ('geojson', '10.239005', '35.390495', '22', '1'),
            ('geocodejson', '-37.164761', '45.394554', '1', '1'),
        ])
    @allure.feature("nominatim")
    @allure.story("Обратные геокодирование по параметризации (ddt)")
    @allure.title("Получения полного списка стран по параматризации reverse")
    def test_reverse_ddt(self, api_client: NominatimOSM, test_data, format, lat, lon, zoom, addressdetails):
        headers = {
            "User-Agent": test_data.get_user_agent(),
            "Accept": test_data.get_accept()
        }
        ddt = api_client.get_reverse_parametrize(format, lat, lon, zoom, addressdetails, headers)
        allure.attach(f"Ответ {ddt}", name="Поиск параматризации", attachment_type=allure.attachment_type.JSON)