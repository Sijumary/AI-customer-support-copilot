from fastapi import FastAPI
from pydantic import BaseModel
from services.copilot import run_copilot

app = FastAPI(title="AI Customer Support Copilot")

class Ticket(BaseModel):
    text: str

@app.post("/analyze-ticket")
def analyze_ticket(ticket: Ticket):
    return run_copilot(ticket.text)
