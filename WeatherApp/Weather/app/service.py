import os
import requests
from dotenv import load_dotenv

load_dotenv()


class WeatherService:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    API_KEY = os.getenv("OPENWEATHER_API_KEY")

    @classmethod
    def get_weather(cls, city_name):
        try:
            params = {
                'q': city_name,
                'appid': cls.API_KEY,
                'units': 'metric',
                'lang': 'ru'
            }
            response = requests.get(cls.BASE_URL, params=params)
            response.raise_for_status()
            return cls.parse_weather_data(response.json())
        except requests.exceptions.RequestException as e:
            return {'error': f"Ошибка API: {str(e)}"}

    @classmethod
    def parse_weather_data(cls, data):
        weather = data.get('weather', [{}])[0]
        main = data.get('main', {})
        wind = data.get('wind', {})

        return {
            'city': data.get('name', 'Неизвестный город'),
            'temperature': main.get('temp', 0),
            'feels_like': main.get('feels_like', 0),
            'description': weather.get('description', 'нет данных'),
            'humidity': main.get('humidity', 0),
            'pressure': main.get('pressure', 0),
            'wind_speed': wind.get('speed', 0),
            'icon': weather.get('icon', ''),
            'timestamp': data.get('dt', 0)
        }