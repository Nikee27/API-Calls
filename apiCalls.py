import requests

def get_weather(city):
    api_key = "08ed1a05b5efd14fdc18ff8bc833143e"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'q':city, 'appid':api_key, 'units':'metric'}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"city: {data['name']}")
        print(f"temp: {data['main']['temp']} C")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("city not found, please try again.")

city = input("Enter a city:")        
get_weather(city)