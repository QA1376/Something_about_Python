import pytest
import requests

class TestFirstApi:
    names = [
        ("Egor"),
        ("Egorka"),
        ("")
    ]

    @pytest.mark.parametrize('name',names)
    def test_hello_call(self,name):
        url = "https://playground.learnqa.ru/api/hello"
        # name = "Egor"
        data = {'name':name}

        response = requests.get(url,params=data)

        assert response.status_code == 200, "ne 200"

        response_dict = response.json()
        assert "answer" in response_dict, "pohozhe"
        if len(name) == 0:
            expected_response_text = "Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict["answer"]
        assert expected_response_text == actual_response_text, "chota ne to"

