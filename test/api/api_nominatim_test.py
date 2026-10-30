import allure
import pytest
import time

from api.NominatimOSM import NominatimOSM
from test_data.DataProvider import DataProvider

data = DataProvider()


@allure.epic("api_nominatim_status")
@allure.severity("blocker")
@pytest.mark.order(1)
@pytest.mark.api
class Test_Api_Nominatim_test_status:

    @allure.story("статус сервера")
    @allure.title("статус по json")
    @pytest.mark.usefixtures("api_client")
    def test_status_nominatim_json(self, api_client: NominatimOSM):
        test = api_client.get_status_Nominatim_json()
        allure.attach(f"Ответ {test}", name="Состояние сервера в json формате", attachment_type=allure.attachment_type.JSON)

    @allure.story("статус сервера")
    @allure.title("статус по text")
    @pytest.mark.usefixtures("api_client")
    def test_status_nominatim_text(self, api_client: NominatimOSM):
        test = api_client.get_status_Nominatim_text()
        allure.attach(f"Ответ {test}", name="Состояние сервера в текстовом формате", attachment_type=allure.attachment_type.TEXT)

@allure.epic("api_nominatim_parametrized")
@allure.severity("blocker")
@pytest.mark.order(2)
@pytest.mark.api
class Test_Api_Nominatim_test_parametrize:

    @pytest.mark.parametrize('q, format, polygon, addressdetails, limit, tags, expected',
        [
            (
                    case["q"],
                    case["format"],
                    case["polygon"],
                    case["addressdetails"],
                    case["limit"],
                    case.get("tags", []),
                    case.get("expected", {}),
            )
            for case in data.get_search_cases()
            if isinstance(case, dict)
        ]
    )
    @allure.story("Прямое геокодирование по параметризации (ddt)")
    @allure.title("Получения полного списка стран по параматризации search")
    @pytest.mark.usefixtures("api_client")
    def test_search_ddt(self, api_client: NominatimOSM, q, format, polygon, addressdetails, limit, tags, expected):
        time.sleep(1.5)
        status_code, response = api_client.get_search_parametrize(q, format, polygon, addressdetails, limit)

        with allure.step("Проверка валдиности формата"):
            valid_formats = ["xml", "geojson", "geocodejson", "json", "jsonv2"]
            allure.attach(f"Ответ {response}", name="Поиск параматризации", attachment_type=allure.attachment_type.JSON)
            assert format is not None, f"Формат не может быть None, format: {format}"
            assert format == format.strip(), f"Формат не может быть пустой строкой или состоять только из пробелов. format: {format}"
            assert format.islower(), f"Формат должен быть в нижнем регистре."
            normalized_format = format.lower().strip()
            assert normalized_format in valid_formats, f"Формат должен быть одним из {valid_formats}. Получено: '{format}'"

        with allure.step("Проверка ожидаемого результата статус кода = 200"):
            expected_status = expected.get("status_code", 200)
            assert status_code == expected_status, f"Ожидали status_code={expected_status}, получили {status_code}"

        with allure.step("Проверка ожидаемого результата на имя"):
            expected_name = expected.get("name")
            if expected_name is None:
                return
            if format in ("json", "jsonv2"):
                items = response if isinstance(response, list) else [response]
                actual_names = [item.get("name") for item in items if isinstance(item, dict)]
                expected_name = expected.get("name")
                assert expected_name in actual_names, f"Ожидали name={expected_name}, получили {actual_names}"
            elif format == "xml":
                expected_name = expected.get("name")
                assert expected_name in response, f"Ожидали name={expected_name} в XML-ответе"


    @pytest.mark.parametrize('format, lat, lon, zoom, addressdetails, tags, expected',
        [
            (
                    case["format"],
                    case["lat"],
                    case["lon"],
                    case["zoom"],
                    case["addressdetails"],
                    case.get("tags", []),
                    case.get("expected", {}),
            )
            for case in data.get_reverse_cases()
            if isinstance(case, dict)
        ]
    )
    @allure.story("Обратные геокодирование по параметризации (ddt)")
    @allure.title("Получения полного списка стран по параматризации reverse")
    @pytest.mark.usefixtures("api_client")
    def test_reverse_ddt(self, api_client: NominatimOSM, format, lat, lon, zoom, addressdetails, tags, expected):
        time.sleep(1.5)
        status_code, response = api_client.get_reverse_parametrize(format, lat, lon, zoom, addressdetails)

        allure.attach(f"Ответ {response}", name="Поиск параматризации", attachment_type=allure.attachment_type.JSON)
        allure.attach(f"Ответ {status_code}", name="Код ответа", attachment_type=allure.attachment_type.JSON)

        with allure.step("Проверка валдиности формата"):
            valid_formats = ["xml", "geojson", "geocodejson", "json", "jsonv2"]
            assert format is not None, f"Формат не может быть None, format: {format}"
            assert format == format.strip(), f"Формат не может быть пустой строкой или состоять только из пробелов. format: {format}"
            assert format.islower(), f"Формат должен быть в нижнем регистре."
            normalized_format = format.lower().strip()
            assert normalized_format in valid_formats, f"Формат должен быть одним из {valid_formats}. Получено: '{format}'"
        with allure.step("Проверка широты"):
            assert lat == lat.strip(), f"Широта не должна быть пустой. LAT: {lat}"
            assert lat != "0", f"Широта не должна быть равна 0. LAT: {lat}"
            assert lat != " ", f"Долгота не должна содержать пробел. LON: {lat}"
        with allure.step("Проверка долготы"):
            assert lon == lon.strip(), f"Долгота не должна быть пустой. LON: {lon}"
            assert lon != "0", f"Долгота не должна быть равна 0. LON: {lon}"
            assert lon != " ", f"Долгота не должна содержать пробел. LON: {lon}"

        with allure.step("Проверка ожидаемого результата статус кода = 200"):
            expected_status = expected.get("status_code", 200)
            assert status_code == expected_status, f"Ожидали status_code={expected_status}, получили {status_code}"

        with allure.step("Проверка ожидаемого результата на имя"):
            expected_name = expected.get("name")
            if expected_name is None:
                return
            if format in ("json", "jsonv2"):
                items = response if isinstance(response, list) else [response]
                actual_names = [item.get("name") for item in items if isinstance(item, dict)]
                expected_name = expected.get("name")
                assert expected_name in actual_names, f"Ожидали name={expected_name}, получили {actual_names}"
            elif format == "xml":
                expected_name = expected.get("name")
                assert expected_name in response, f"Ожидали name={expected_name} в XML-ответе"