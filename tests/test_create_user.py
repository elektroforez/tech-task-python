import http

import allure


@allure.title("create_user")
def test_create_user(user_client, payload):
    create_response = user_client.create_user(payload)
    assert create_response.status_code == http.HTTPStatus.OK
    assert "error_code" not in create_response.json()

    user_login = create_response.json()["login"]
    user_client.headers["User-Token"] = create_response.json()["User-Token"]

    get_response = user_client.get_user(user_login)
    assert get_response.status_code == http.HTTPStatus.OK
    assert "error_code" not in get_response.json()
    # the server normalizes all values to lowercase
    assert get_response.json()["login"] == payload["user"]["login"].lower()
    assert get_response.json()["account_details"]["email"] == payload["user"]["email"].lower()

@allure.title("update_user")
def test_update_user(user_client, update_user_payload, created_user):
    login = update_user_payload["user"]["login"]
    email = update_user_payload["user"]["email"]
    user_client.headers["User-Token"] = created_user["User-Token"]
    update_response = user_client.update_user(created_user["login"], update_user_payload)
    assert update_response.status_code == http.HTTPStatus.OK
    assert "error_code" not in update_response.json()

    get_response = user_client.get_user(login)
    assert get_response.status_code == http.HTTPStatus.OK
    assert "error_code" not in get_response.json()
    # the server normalizes all values to lowercase
    assert get_response.json()["login"] == login.lower()
    assert get_response.json()["account_details"]["email"] == email.lower()