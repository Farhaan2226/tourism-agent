import requests

class Geocoder:
    def get_coordinates(self, place: str):
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": place,
            "format": "json",
            "limit": 1,
            "addressdetails": 1,
            "email": "farhanmd2004@gmail.com"   
        }

        headers = {
            "User-Agent": "tourism-agent/1.0 (farhanmd2004@gmail.com)"
        }

        try:
            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
        except Exception as e:
            return None

        data = response.json()
        if not data:
            return None

        return float(data[0]["lat"]), float(data[0]["lon"])
