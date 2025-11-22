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
            return None, None

        data = response.json()

        # 1️⃣ GET TEMPERATURE
        temp = data["current_weather"]["temperature"]

        # 2️⃣ GET CORRECT RAIN %
        now = data["current_weather"]["time"]       # string timestamp
        hourly_times = data["hourly"]["time"]       # list of timestamps

        try:
            index = hourly_times.index(now)
        except ValueError:
    # fallback: nearest hour
            index = len(data["hourly"]["time"]) // 2


        rain = data["hourly"]["precipitation_probability"][index]

        # 🔥 ALWAYS return exactly TWO values
        return temp, rain

