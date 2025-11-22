from agents.weather_agent import WeatherAgent
from agents.places_agent import PlacesAgent
from utils.intent import IntentDetector
from utils.geocode import Geocoder


class TourismOrchestrator:
    def __init__(self):
        self.weather_agent = WeatherAgent()
        self.places_agent = PlacesAgent()
        self.intent_detector = IntentDetector()
        self.geocoder = Geocoder()

    def process(self, query: str) -> str:
        try:
            # 1️⃣ Extract the place
            place = self.intent_detector.extract_place(query)
            if not place:
                return "I couldn't detect the place. Please try again."

            # 2️⃣ Geocode the place
            coords = self.geocoder.get_coordinates(place)
            if coords is None:
                return f"I couldn't find '{place}' on the map."

            lat, lon = coords

            # 3️⃣ Detect user intent
            intents = self.intent_detector.detect_intents(query)

            # Prepare weather and places variables
            temp = None
            rain = None
            places = []

            # 4️⃣ WEATHER INTENT
            if intents["weather"]:
                temp, rain = self.weather_agent.get_weather(lat, lon)
                if temp is None:
                    return f"I found {place.title()}, but I couldn't get the weather data."

            # 5️⃣ PLACES / TOURIST INTENT
            if intents["places"]:
                places = self.places_agent.get_places(lat, lon)

            # 6️⃣ If no intents → default to places list
            if not intents["weather"] and not intents["places"]:
                places = self.places_agent.get_places(lat, lon)
                if not places:
                    return f"In {place.title()} I couldn't find any popular tourist spots."
                return (
                    f"Here are some places you can go in {place.title()}:\n"
                    + "\n".join([p for p in places])
                )

            # 7️⃣ WEATHER ONLY
            if intents["weather"] and not intents["places"]:
                return (
                    f"In {place.title()} it’s currently {temp}°C "
                    f"with a {rain}% chance of rain."
                )

            # 8️⃣ PLACES ONLY
            if intents["places"] and not intents["weather"]:
                if not places:
                    return f"I couldn't find any tourist places in {place.title()}."
                return (
                    f"And these are the places you can go in {place.title()}:\n"
                    + "\n".join([p for p in places])
                )

            # 9️⃣ BOTH WEATHER + PLACES
            if temp is not None and places:
                places_text = "\n".join(places)
                return (
                    f"In {place.title()} it’s currently {temp}°C "
                    f"with a {rain}% chance of rain. "
                    f"And these are the places you can go:\n"
                    f"\n{places_text}\n"
                )

            # Fallback
            return "I couldn't generate a response. Please try again."

        except Exception as e:
            return f"Internal error: {str(e)}"

