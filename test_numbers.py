import requests

import phone_numbers_re
from generate_numbers import generate_phone_number

TEST_URL = "https://stage.auth-api.infinitecreator.com"

numbers = phone_numbers_re.phone_numbers


def user_sign_in(payload):
    return requests.post(TEST_URL + f"/sign_in", json=payload)


# Check elliman users
def test_check_sign_in():
    def elliman_payload():
        return {
            "phone_number": f"{i}",
            "app_type": "elliman"
        }

    for i in numbers:
        print(i)
        payload = elliman_payload()
        response = user_sign_in(payload)
        assert response.status_code == 202


# Check test IC random number to log in
def test_check_gen_sign_in():
    def ic_payload():
        return {
            "phone_number": f"{generate_phone_number()}",
            "app_type": "ic"
        }

    payload = ic_payload()
    response = user_sign_in(payload)
    assert response.status_code == 202
    