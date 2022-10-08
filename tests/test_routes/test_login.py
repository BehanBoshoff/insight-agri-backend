import json

from fastapi.security import OAuth2PasswordRequestForm
from urllib3 import encode_multipart_formdata


def test_login_for_access_token(client):
    data = {
        "username": "testuser",
        "email": "testuser@nofoobar.com",
        "password": "test@dmin",
        "is_active": True,
        "is_superuser": True,
        "pic": "",
        "fullname": "Test User",
        "firstname": "Test",
        "lastname": "User",
        "occupation": "Engineer",
        "company_name": "InsightAgri",
        "phone": "",
        "communication": True,
    }
    response = client.post("/users/", json.dumps(data))

    assert response.status_code == 200
    assert response.json()["email"] == "testuser@nofoobar.com"
    assert response.json()["is_active"] is True

    login_data = {
        "username": "testuser@nofoobar.com",
        "password": "test@dmin",
    }
    response = client.post("/auth/login/token", data=login_data)

    assert response.status_code == 200
    assert response.json()["authToken"]
    assert response.json()["refreshToken"]
    assert response.json()["expires_in"]


def test_get_current_user_from_token(client):
    data = {
        "username": "testuser2",
        "email": "testuser2@nofoobar.com",
        "password": "test@dmin",
        "is_active": True,
        "is_superuser": True,
        "pic": "",
        "fullname": "Test User",
        "firstname": "Test",
        "lastname": "User",
        "occupation": "Engineer",
        "company_name": "InsightAgri",
        "phone": "",
        "communication": True,
    }
    response = client.post("/users/", json.dumps(data))
    assert response.status_code == 200

    login_data = {
        "username": data["email"],
        "password": data["password"],
    }
    login_response = client.post("/auth/login/token", data=login_data)

    assert login_response.status_code == 200
    assert login_response.json()["authToken"]

    client.headers = {"Authorization": f"Bearer {login_response.json()['authToken']}"}
    me_response = client.get("/auth/login/me")

    assert me_response.status_code == 200
    assert me_response.json()["email"] == data["email"]
