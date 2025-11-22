import requests

class WeatherAgent:
    def get_weather(self, lat, lon):
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True,
            "hourly": "precipitation_probability"
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
        except:
            return "I couldn't fetch the weather right now."

        data = response.json()
        temp = data["current_weather"]["temperature"]
        rain = data["hourly"]["precipitation_probability"][0]

        return f"it's currently {temp}°C with a {rain}% chance of rain."
