import requests

class Geocoder:
    def get_coordinates(self, place: str):
        url = "https://nominatim.openstreetmap.org/search"
        params = {"q": place, "format": "json", "limit": 1}

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
        except:
            return None

        data = response.json()
        if not data:
            return None

        return float(data[0]["lat"]), float(data[0]["lon"])
