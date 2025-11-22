import requests

class PlacesAgent:
    def get_places(self, lat, lon):
        query = f"""
        [out:json];
        node["tourism"](around:5000,{lat},{lon});
        out;
        """
        url = "https://overpass-api.de/api/interpreter"

        try:
            headers = {"User-Agent": "tourism-agent-app/1.0"}
            response = requests.post(url, data=query, headers=headers, timeout=15)

            response.raise_for_status()
        except:
            return []

        data = response.json()
        places = []

        for element in data.get("elements", []):
            name = element.get("tags", {}).get("name")
            if name:
                places.append(name)
            if len(places) == 5:
                break

        return places
