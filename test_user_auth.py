import pytest
import requests

class TestUserAuth:
    def test_auth_user(self):
        data = {
        'email':'vinkotov@example.com',
        'password':'1234'
    }

        resource1 = requests.post("https://playground.learnqa.ru/api/user/login",data = data)
        assert "auth_sid" in resource1.cookies, "net SIDa"