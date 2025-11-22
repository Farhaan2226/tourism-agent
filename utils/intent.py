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

        # 1️⃣ Match patterns like "in goa", "in mumbai"
        match = re.search(r"\bin ([a-zA-Z\s]+)", text)
        if match:
            place = match.group(1).strip()
            # take only last word(s) by removing verbs like "visit"
            # e.g. "visit in goa" → "goa"
            tokens = place.split()
            # keep the last token OR last 2 tokens (for "new york")
            if len(tokens) == 1:
                return tokens[0]
            else:
                return " ".join(tokens[-2:])  # handles "new york", "los angeles"

        # 2️⃣ Match "to goa"
        match = re.search(r"\bto ([a-zA-Z\s]+)", text)
        if match:
            place = match.group(1).strip()
            tokens = place.split()
            if len(tokens) == 1:
                return tokens[0]
            else:
                return " ".join(tokens[-2:])

        return None

