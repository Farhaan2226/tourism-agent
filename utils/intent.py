import re

class IntentDetector:

    def detect_intents(self, text: str):
        t = text.lower()
        return {
            "weather": any(w in t for w in ["weather", "temperature", "rain", "hot", "cold"]),
            "places": any(w in t for w in ["visit", "place", "tourist", "attractions"])
        }

    def extract_place(self, text: str):
        text = text.lower()

        # Match "in bangalore"
        match = re.search(r"\bin ([a-zA-Z\s]+)", text)
        if match:
            place = match.group(1).strip()
            tokens = place.split()
            stopwords = {"to", "visit", "in", "the", "go", "best", "places"}
            cleaned = [t for t in tokens if t not in stopwords]
            if len(cleaned) == 1:
                return cleaned[0]
            return " ".join(cleaned[-2:])

        # Match "to bangalore"
        match = re.search(r"\bto ([a-zA-Z\s]+)", text)
        if match:
            place = match.group(1).strip()
            tokens = place.split()
            stopwords = {"to", "visit", "in", "the", "go", "best", "places"}
            cleaned = [t for t in tokens if t not in stopwords]
            if len(cleaned) == 1:
                return cleaned[0]
            return " ".join(cleaned[-2:])

        return None
