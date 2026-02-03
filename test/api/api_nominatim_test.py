import allure
import pytest

from api.NominatimOSM import NominatimOSM


@allure.epic("api_nominatim_status")
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

@allure.epic("api_nominatim_parametrized")
@allure.severity("blocker")
class Test_Api_Nominatim_test_parametrize:

    @pytest.mark.parametrize('q, format, polygon, addressdetails, limit', [
        # Валидные проверки
        ('Barbados', 'geojson', '0', '0', '0'),
        ('Barbados', 'geocodejson', '1', '1', '1'),
        ('Tuvalu', 'json', '1', '0', '1'),
        ('Tuvalu', 'jsonv2', '0', '1', '0'),
        ('Tuvalu', 'geojson', '1', '0', '1'),
        ('Tuvalu', 'geocodejson', '0', '1', '0'),
        ('Tuvalu', 'xml', '0', '1', '0'),
        ('Chile', 'jsonv2', '1', '1', '1'),
        ('Chile', 'geojson', '0', '0', '0'),
        ('Chile', 'geocodejson', '1', '1', '1'),
        ('Chile', 'xml', '1', '1', '1'),
        ('Chile', 'json', '0', '0', '0'),
        ('Afghanistan', 'geojson', '1', '0', '1'),
        ('Afghanistan', 'geocodejson', '0', '1', '0'),
        ('Afghanistan', 'xml', '0', '1', '0'),
        ('Afghanistan', 'json', '1', '0', '1'),
        ('Afghanistan', 'jsonv2', '0', '1', '0'),
        ('Honduras', 'geocodejson', '1', '1', '1'),
        ('Honduras', 'xml', '0', '0', '0'),
        ('Honduras', 'json', '0', '0', '0'),
        ('Honduras', 'jsonv2', '1', '1', '1'),
        ('Honduras', 'geojson', '0', '0', '0'),
        ('Barbados', 'xml', '1', '0', '1'),
        ('Barbados', 'xml', '0', '1', '0'),
        ('Barbados', 'json', '1', '0', '1'),
        ('Barbados', 'jsonv2', '0', '1', '0'),
        ('Barbados', 'geojson', '1', '0', '1'),
        ('Barbados', 'geocodejson', '0', '1', '0'),
        # Проверки пустых значений
        ('', 'json', '0', '0', '0'),
        ('Barbados', '', '1', '1', '1'),
        ('Test', 'json', '', '1', '1'),
        ('Test', 'json', '1', '', '1'),
        ('Test', 'json', '1', '1', ''),
        ('', '', '', '', ''),
        # Проверки с некорректными значениями
        ('None', 'json', '0', '0', '0'),
        ('null', 'json', '1', '1', '1'),
        ('Barbados', 'invalid_format', '0', '0', '0'),
        # Проверки граничных значений для limit
        ('Test', 'json', '0', '0', '0'),
        ('Test', 'json', '0', '0', '1'),
        ('Test', 'json', '0', '0', '50'),
        ('Test', 'json', '0', '0', '999'),
        # Проверки с пробелами
        ('  Barbados  ', 'json', '1', '0', '1'),
        ('Test', '  json  ', '0', '1', '0'),
        # Проверки со специальными символами
        ('Test&City', 'json', '1', '1', '1'),
        ('Test-City', 'json', '0', '0', '0'),
        ('Test_City', 'json', '1', '0', '1'),
        # Проверки нестандартных значений булевых параметров
        ('Test', 'json', 'true', 'false', '10'),
        ('Test', 'json', 'TRUE', 'FALSE', '5'),
        ('Test', 'json', '2', '3', '10'),
        # Проверки с очень длинными строками
        ('A' * 100, 'json', '1', '0', '1'),
        ('Test', 'json' * 10, '0', '1', '0'),
        # Проверки кодировки
        ('Кириллица', 'json', '1', '1', '1'),  # Кириллица в запросе
        ('München', 'json', '0', '0', '0'),  # Unicode символы
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
        ('xml', '82.689336', '-31.809395', '50', '0'),
        ('xml', '-24.743005', '-32.115876', '30', '1'),
        ('xml', '10.239005', '35.390495', '22', '0'),
        ('xml', '-37.164761', '45.394554', '1', '1'),
        ('json', '82.689336', '-32.115876', '22', '1'),
        ('json', '-24.743005', '35.390495', '1', '1'),
        ('json', '10.239005', '45.394554', '18', '0'),
        ('json', '-37.164761', '-53.580959', '50', '1'),
        ('json', '-9.911374', '-31.809395', '30', '0'),
        ('jsonv2', '-24.743005', '45.394554', '50', '0'),
        ('jsonv2', '10.239005', '-53.580959', '30', '1'),
        ('jsonv2', '-37.164761', '-31.809395', '22', '1'),
        ('jsonv2', '-9.911374', '-32.115876', '1', '0'),
        ('jsonv2', '82.689336', '35.390495', '18', '1'),
        ('geojson', '10.239005', '-31.809395', '1', '1'),
        ('geojson', '-37.164761', '-32.115876', '18', '0'),
        ('geojson', '-9.911374', '35.390495', '50', '1'),
        ('geojson', '82.689336', '45.394554', '30', '1'),
        ('geojson', '-24.743005', '-53.580959', '22', '0'),
        ('geocodejson', '-37.164761', '35.390495', '30', '0'),
        ('geocodejson', '-9.911374', '45.394554', '22', '1'),
        ('geocodejson', '82.689336', '-53.580959', '1', '0'),
        ('geocodejson', '-24.743005', '-31.809395', '18', '1'),
        ('geocodejson', '10.239005', '-32.115876', '50', '1'),

        # Дополнительные проверки с пустыми значениями
        ('', '10.239005', '35.390495', '22', '1'),  # пустой формат
        ('xml', '', '-53.580959', '18', '1'),  # пустая широта
        ('json', '82.689336', '', '22', '1'),  # пустая долгота
        ('jsonv2', '-24.743005', '45.394554', '', '0'),  # пустой zoom
        ('geojson', '10.239005', '-31.809395', '1', ''),  # пустой addressdetails
        ('geocodejson', '', '', '50', '1'),  # пустые координаты
        ('', '', '', '', ''),  # все поля пустые
        ('xml', '0', '0', '18', '1'),  # нулевые координаты
        ('json', '-90.000000', '-180.000000', '50', '1'),  # крайние значения координат
        ('jsonv2', '90.000000', '180.000000', '1', '0'),  # крайние значения координат
        ('geojson', '91.000000', '35.390495', '22', '1'),  # широта за пределами допустимого
        ('geocodejson', '10.239005', '181.000000', '18', '1'),  # долгота за пределами допустимого
        ('xml', '-9.911374', '-53.580959', '-1', '1'),  # отрицательный zoom
        ('json', '82.689336', '-31.809395', '100', '1'),  # слишком большой zoom
        ('jsonv2', '-24.743005', '-32.115876', '30', '2'),  # недопустимое значение addressdetails
        ('invalid_format', '10.239005', '35.390495', '22', '1'),  # невалидный формат
        ('XML', '10.239005', '35.390495', '22', '1'),  # формат в верхнем регистре
        ('Json', '10.239005', '35.390495', '22', '1'),  # формат с заглавной буквы
        ('xml', '10.239.005', '35.390495', '22', '1'),  # невалидный формат числа
        ('json', '82,689336', '-31.809395', '22', '1'),  # запятая вместо точки
        ('jsonv2', '-24.743005', '45.394554', 'abc', '0'),  # нечисловое значение zoom
        ('geojson', '10.239005', '-31.809395', '1', 'true'),  # строковое значение addressdetails
        ('Кириллица', '-24.743005', '35.390495', '1', '1'),  # Кириллица в формате
        ('München', '-24.743005', '35.390495', '0', '0'),  # Unicode в формате
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