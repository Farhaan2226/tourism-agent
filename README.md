
🌍 Tourism Multi-Agent Assistant

Hey Guys! This project is something I built to understand how multiple agents can co-operate to give real-world solutions.
The project basically invloves:

•	Typing a question like:
                   “weather and places to visit in Bangalore”
•	The system figures out what I want
•	It checks the weather
•	It finds nearby tourist spots
•	And it replies in a clean, human-readable format

Everything runs through a FastAPI backend, and the system is fully deployed online.
I have used Streamlit for an interactive UI

LIVE DEMO LINKS:
	Backend (FastAPI – Render):
•	https://tourism-agent.onrender.com

 Swagger Docs:
•	https://tourism-agent.onrender.com/docs

	Streamlit UI (Frontend)
•	https://tourism-agent-jl4bhbwkbizhwtohr6o8tz.streamlit.app/

WHAT THE APP DOES:
You can ask it things like:
•	“weather in Goa”
•	“places to visit in Chennai”
•	“weather and places to visit in Bangalore”
•	“tourist attractions in Dubai”
It will:
1.	Understand whether you want weather, places, or both
2.	Identify the city
3.	Convert the city to coordinates
4.	Fetch real-time weather data
5.	Fetch real tourist attractions around that area
6.	Combine everything into one meaningful answer

BEHIND THE SCENES (MULTI-AGENT ARCHITECTURE):
To keep things modular, I split the logic into small agents:
1. Intent Detector
Figures out what the user wants:
•	weather?
•	tourist places?
•	both?
2. Geocoder
Turns “Bangalore” → (latitude, longitude) using Nominatim API.
3. Weather Agent
Fetches:
•	temperature
•	rain probability
from the Open-Meteo API.
4. Places Agent
Searches tourist attractions near the coordinates using Overpass API.
5. Orchestrator
This is the “brain.”
It decides which agents to call and assembles the final answer in natural human-like text.


RUNNING THE APP LOCALLY:
1. Install requirements :
pip install -r requirements.txt
2. Run FastAPI :
uvicorn main:app --reload
API will be live at:
http://127.0.0.1:8000
3. Run Streamlit :
streamlit run streamlit_app.py

DEPLOYMENT:

The app is deployed using:

FastAPI → Render

Streamlit UI → Streamlit Cloud

Procfile handles production startup.

TECH STACK:

•	FastAPI

•	Streamlit

•	Python

•	Requests

•	Open-Meteo API

•	Nominatim Geocoding


•	Overpass API (OSM)

•	Render(hosting)





