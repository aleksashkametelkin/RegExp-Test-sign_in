import requests

import phone_numbers_re

TEST_URL = "https://stage.auth-api.infinitecreator.com"

numbers = phone_numbers_re.phone_numbers


def user_sign_in(payload):
    return requests.post(TEST_URL + f"/sign_in", json=payload)


def test_check_sign_in():
    def user_payload():
        return {
            "phone_number": f"{i}",
            "app_type": "elliman"
        }

    for i in numbers:
        payload = user_payload()
        response = user_sign_in(payload)
        assert response.status_code == 202
        print(response.status_code)
