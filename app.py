from fastapi import FastAPI
from pydantic import BaseModel
from core.tourism_orchestrator import TourismOrchestrator

app = FastAPI(title="Tourism Multi-Agent System")
agent = TourismOrchestrator()

class Query(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Tourism Multi-Agent API is running!"}

@app.post("/ask")
def ask(query: Query):
    reply = agent.process(query.message)
    return {"reply": reply}

