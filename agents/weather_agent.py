import requests
from datetime import datetime

class WeatherAgent:
    def get_weather(self, lat, lon):
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True,
            "hourly": "precipitation_probability",
            "timezone": "auto"
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
        except:
            return "I couldn't fetch the weather right now."

        data = response.json()

        # current temperature
        temp = data["current_weather"]["temperature"]

        # Find correct hour index
        now = data["current_weather"]["time"]       # e.g. 2025-11-22T12:00
        hourly_times = data["hourly"]["time"]

        try:
            hour_index = hourly_times.index(now)
        except ValueError:
            hour_index = 0  # fallback

        # real rain probability
        rain = data["hourly"]["precipitation_probability"][hour_index]

        return f"it's currently {temp}°C with a {rain}% chance of rain."
