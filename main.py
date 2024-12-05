import requests

payload = {"name":"user"}
response = requests.get("https://playground.learnqa.ru/api/hello",params=payload)

print(response.text)

response2 = requests.delete("https://playground.learnqa.ru/api/check_type")

print(response2.text)


print(2**)