import requests
from bs4 import BeautifulSoup

def get_weather_info(country):
    api_key = "7bad8f4389f206e10eb9d3bd3edd0d36"

    # Make a request to the OpenWeather API
    url = f"https://api.openweathermap.org/data/2.5/weather?q={country}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    # Extract weather information from the response
    print(data)
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    return f'The temperature in {country} is {temperature} and the weather is {description}.'


