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
        place = self.intent_detector.extract_place(query)

        if not place:
            return "I couldn't detect the place. Please try again."

        coords = self.geocoder.get_coordinates(place)
        if coords is None:
            return f"I don't know if '{place}' exists."

        lat, lon = coords

        intents = self.intent_detector.detect_intents(query)
        responses = []

        if intents["weather"]:
            responses.append(
                f"In {place}, {self.weather_agent.get_weather(lat, lon)}"
            )

        if intents["places"]:
            places = self.places_agent.get_places(lat, lon)
            if places:
                formatted = "\n- " + "\n- ".join(places)
                responses.append(f"Here are some places to visit:{formatted}")
            else:
                responses.append("I couldn't find attractions nearby.")

        if not responses:
            # default behavior: give places
            places = self.places_agent.get_places(lat, lon)
            formatted = "\n- " + "\n- ".join(places)
            return f"Places to visit in {place}:{formatted}"

        return " ".join(responses)
