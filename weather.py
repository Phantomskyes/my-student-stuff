import requests

API_KEY = "e0e352d22493ede5c840523e4b3c0aa6"

city = input("Enter a city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid="+ API_KEY

weather_data = requests.get(base_url).json()

print(weather_data)