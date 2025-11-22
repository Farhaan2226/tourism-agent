import re

class IntentDetector:

    def detect_intents(self, text: str):
        t = text.lower()
        return {
            "weather": any(w in t for w in ["weather", "temperature", "rain", "hot", "cold"]),
            "places": any(w in t for w in ["visit", "place", "tourist", "attractions"])
        }

    def extract_place(self, text: str):
        # Try "to <place>"
        match = re.search(r"\bto ([A-Za-z\s]+)", text, re.IGNORECASE)
        if match:
            return match.group(1).strip(" .?")

        # Try "in <place>"
        match = re.search(r"\bin ([A-Za-z\s]+)", text, re.IGNORECASE)
        if match:
            return match.group(1).strip(" .?")

        return None
