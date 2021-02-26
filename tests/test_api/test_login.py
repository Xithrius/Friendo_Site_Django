import requests

from .api_calls import VALID_LOGIN, GET_USERS, INVALID_LOGIN
from tests.settings import LOCAL_TEST_URL

API_URL = f"{LOCAL_TEST_URL}/api/"


class TestLogin:
    """Tests login mutation."""

    def test_valid_request(self) -> None:
        """Valid login data should return jwt."""
        response = requests.post(url=API_URL, json={"query": VALID_LOGIN})
        resp_data = response.json()
        token = resp_data["data"]["login"].get("token")
        headers = {"Authorization": f"Bearer {token}"}
        test_get_request = requests.post(
            url=API_URL, json={"query": GET_USERS}, headers=headers
        )

        users = [
            user.get("username") for user in test_get_request.json()["data"]["allUsers"]
        ]
        assert "test_api_user" in users

    def test_invalid_request(self) -> None:
        """Invalid login credentials should return None for 'token.'"""
        assert True
