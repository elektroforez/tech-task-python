import http
import os
import pytest
import uuid
from clients.api_user_client import UserClient
from settings import BASE_URL
from faker import Faker

fake = Faker()

TOKEN = os.getenv("TOKEN")

@pytest.fixture
def headers():
    return {
        "Content-Type": "application/json",
        "Authorization": f'Token token="{TOKEN}"'
    }

@pytest.fixture
def user_client(headers):
    return UserClient(BASE_URL, headers)

@pytest.fixture
def payload():
    unique = uuid.uuid4().hex[:8]
    return {
            "user": {
                "login": f"user_{unique}",
                "email": fake.email(),
                "password": fake.password(length=12)
            }
        }

@pytest.fixture
def created_user(user_client, payload):
    response = user_client.create_user(payload)
    assert response.status_code == http.HTTPStatus.OK
    return response.json()

@pytest.fixture
def update_user_payload():
    unique = uuid.uuid4().hex[:8]
    return {
        "user": {
            "login": f"user_{unique}",
            "email": fake.email(),
        }
    }