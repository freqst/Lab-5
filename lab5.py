import json
import requests

print("Задание 1.")
city_name = 'Stockholm'
key = 'f1277be5f0e36cae255a132f0117952b'
response = requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}')
result = json.loads(response.text)
print(f'The weather for Stockholm:')
print(f' Temperature: {result.get("main")["temp"]}°F')
print(f' Humidity: {result.get("main")["humidity"]}%')
print(f' Pressure: {result.get("main")["pressure"]} hPa')
print(f' Visibility: {result["visibility"]} km')
print(f' Wind speed: {result.get("wind")["speed"]} m/s')
print(f' Clouds all: {result.get("clouds")["all"]}%')



print(f'')
print("Задание 2.")
r = requests.get("https://rickandmortyapi.com/api/character/?status=alive&gender=female").json()
for i in r.get('results'):
    i.pop("episode")
    print(f'Name: {i.get("name")}')
    print(f'Status: {i.get("status")}')
    print(f'Species: {i.get("species")}')
    print(f'Origin: {i.get("origin")["name"]}')
    print(f'')