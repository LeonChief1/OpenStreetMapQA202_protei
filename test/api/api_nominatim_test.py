import allure
import pytest

from api.NominatimOSM import NominatimOSM

@pytest.mark.skip
def test_status_nominatim_json(api_client: NominatimOSM, test_data):
    headers = {
        "User-Agent": test_data.get_user_agent(),
        "Accept": test_data.get_accept()
    }

    test = api_client.get_status_Nominatim_json(headers)
    print(test)

@pytest.mark.skip
def test_status_nominatim_text(api_client: NominatimOSM, test_data):
    headers = {
        "User-Agent": test_data.get_user_agent(),
        "Accept": test_data.get_accept()
    }

    test = api_client.get_status_Nominatim_text(headers)
    print(test)

@pytest.mark.parametrize('q, formant, polygon, addressdetails, limit', [
        ('Barbados', 'xml', '1', '1', '1'),
        ('Tuvalu', 'json', '0', '1', '1'),
        ('Chile', 'jsonv2', '0', '1', '1'),
        ('Afghanistan', 'geojson', '1', '1', '1'),
        ('Honduras', 'geocodejson', '1', '1', '1'),
    ])
def test_search_ddt(api_client: NominatimOSM, test_data, q, formant, polygon, addressdetails, limit):
    headers = {
        "User-Agent": test_data.get_user_agent(),
        "Accept": test_data.get_accept()
    }
    api_client.get_search_parametrize(q, formant, polygon, addressdetails, limit, headers)


@pytest.mark.parametrize('format, lat, lon, zoom, addressdetails', [
        ('xml', '-9.911374', '-53.580959', '18', '1'),
        ('json', '82.689336', '-31.809395', '50', '1'),
        ('jsonv2', '-24.743005', '-32.115876', '30', '1'),
        ('geojson', '10.239005', '35.390495', '22', '1'),
        ('geocodejson', '-37.164761', '45.394554', '1', '1'),
    ])
def test_reverse_ddt(api_client: NominatimOSM, test_data, format, lat, lon, zoom, addressdetails):
    headers = {
        "User-Agent": test_data.get_user_agent(),
        "Accept": test_data.get_accept()
    }
    api_client.get_reverse_parametrize(format, lat, lon, zoom, addressdetails, headers)