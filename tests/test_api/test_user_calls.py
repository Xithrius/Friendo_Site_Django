import requests

from .api_calls import GET_USERS
from tests.settings import LOCAL_TEST_URL, INVALID_TOKEN

API_URL = f"{LOCAL_TEST_URL}/api/"


class TestUserCalls:
    def test_no_token(self):
        response = requests.post(url=API_URL, json=GET_USERS)
        assert response.status_code != 200

    def test_invalid_token(self):
        headers = {"Authorization": f"Bearer {INVALID_TOKEN}"}
        response = requests.post(url=API_URL, json=GET_USERS, headers=headers)
        assert response.status_code != 200
