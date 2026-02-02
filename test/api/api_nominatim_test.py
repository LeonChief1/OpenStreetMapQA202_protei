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


