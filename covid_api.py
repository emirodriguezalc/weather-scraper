import requests

def get_covid_info(country):
    url = f'https://api.covid19api.com/live/country/{country}/status/confirmed'
    response = requests.get(url)
    data = response.json()
    latest_data = data[-1]
    confirmed = latest_data['Confirmed']
    deaths = latest_data['Deaths']
    recovered = latest_data['Recovered']
    return f'The number of confirmed COVID-19 cases in {country} is {confirmed}, with {deaths} deaths and {recovered} recoveries.'

