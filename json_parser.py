import requests
import json

from requests import JSONDecodeError

string_as_json_format = '{"answer":"Hello, Loser!"}'

obj = json.loads(string_as_json_format)

key = "loser"
if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} в JSON нет")

payload = {"name":"user"}
response = requests.get("https://playground.learnqa.ru/api/hello",params=payload)
response2 = requests.get("https://playground.learnqa.ru/api/get_text")
try:
    parsed_response_text = response2.json()
    print(parsed_response_text["answer"])
except JSONDecodeError:
    print("Response is not JSON format")