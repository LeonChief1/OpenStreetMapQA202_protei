import allure
from api.NominatimOSM import NominatimOSM

def test_status_nominatim_json(api_client: NominatimOSM, test_data):
    headers = {
        "User-Agent": test_data.get_user_agent(),
        "Accept": test_data.get_accept()
    }

    test = api_client.get_status_Nominatim_json(headers)
    print(test)


def test_status_nominatim_text(api_client: NominatimOSM, test_data):
    headers = {
        "User-Agent": test_data.get_user_agent(),
        "Accept": test_data.get_accept()
    }

    test = api_client.get_status_Nominatim_text(headers)
    print(test)