import requests

class UserClient:
    def __init__(self, base_url: str, headers: dict):
        self.base_url = base_url
        self.headers = headers

    def create_user(self, payload: dict):
        return requests.request("POST", f"{self.base_url}/users", json=payload, headers=self.headers)

    def get_user(self, login: str):
        return requests.request("GET", f"{self.base_url}/users/{login}", headers=self.headers)

    def update_user(self, login: str, payload: dict):
        return requests.request("PUT", f"{self.base_url}/users/{login}", json=payload, headers=self.headers)