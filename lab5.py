import json
import requests


city_name = 'Stockholm'
key = 'f1277be5f0e36cae255a132f0117952b'
response = requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}')
result = json.loads(response.text)
print(result)


r = requests.get("https://rickandmortyapi.com/api/character/?status=alive&gender=female").json()
r.pop("info")
k = r.get("results")
for i in k:
    print(i)