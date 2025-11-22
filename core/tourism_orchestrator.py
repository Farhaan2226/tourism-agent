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
        """
        Main pipeline:
        - Extract place
        - Geocode place
        - Infer intents
        - Call WeatherAgent / PlacesAgent
        - Combine responses
        - Always return CLEAN result
        """

        try:
            # 1. Extract place
            place = self.intent_detector.extract_place(query)
            if not place:
                return "I couldn't detect the place. Please try again."

            # 2. Geocode the place
            coords = self.geocoder.get_coordinates(place)
            if coords is None:
                return f"I couldn't find '{place}' on the map."

            lat, lon = coords

            # 3. Detect intentions
            intents = self.intent_detector.detect_intents(query)
            responses = []

            # 4. Weather info
            if intents["weather"]:
                weather_text = self.weather_agent.get_weather(lat, lon)
                responses.append(f"In {place}, {weather_text}")

            # 5. Places / attractions
            if intents["places"]:
                places = self.places_agent.get_places(lat, lon)
                if places:
                    formatted = "\n- " + "\n- ".join(places)
                    responses.append(f"Here are some places to visit:{formatted}")
                else:
                    responses.append("I couldn't find attractions nearby.")

            # 6. If no explicit intent → return places only
            if not responses:
                places = self.places_agent.get_places(lat, lon)
                if places:
                    formatted = "\n- " + "\n- ".join(places)
                    return f"Places to visit in {place}:{formatted}"
                else:
                    return f"I couldn't find anything interesting in {place}."

            return " ".join(responses)

        except Exception as e:
            # If ANYTHING fails, we return the error so we can debug Render
            return f"Internal error: {str(e)}"

