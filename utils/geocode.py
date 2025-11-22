import requests

class Geocoder:
    def get_coordinates(self, place: str):
        url = "https://nominatim.openstreetmap.org/search"

        headers = {
            "User-Agent": "tourism-agent/1.0 (farhanmd2004@gmail.com)"
        }

        # 1️⃣ FIRST TRY — exact query
        params = {
            "q": place,
            "format": "json",
            "limit": 1,
            "addressdetails": 1,
            "email": "farhanmd2004@gmail.com"
        }

        try:
            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            if data:
                return float(data[0]["lat"]), float(data[0]["lon"])
        except:
            pass

        # 2️⃣ SECOND TRY — add ", India" (this FIXES Goa)
        params["q"] = f"{place}, India"

        try:
            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            if data:
                return float(data[0]["lat"]), float(data[0]["lon"])
        except:
            pass

        # 3️⃣ FAILED BOTH → return None
        return None
