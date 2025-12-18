from fastapi import FastAPI
from monitoring.metrics import metrics
from services.copilot import run_copilot
from feedback.store import save_feedback


app = FastAPI(
    title="AI Customer Support Copilot",
    description="Tier-2 AI system with observability",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/metrics")
def get_metrics():
    """
    Exposes live AI system metrics
    """
    snapshot = metrics.snapshot()
    return snapshot if snapshot else {"message": "No metrics recorded yet"}

@app.post("/copilot")
def copilot_endpoint(payload: dict):
    """
    Runs AI copilot on incoming ticket
    """
    ticket_text = payload.get("ticket_text")
    if not ticket_text:
        return {"error": "ticket_text is required"}

    return run_copilot(ticket_text)

@app.post("/feedback")
def submit_feedback(payload: dict):
    required = [
        "ticket_text",
        "predicted_category",
        "corrected_category",
        "predicted_priority",
        "corrected_priority"
    ]

    for field in required:
        if field not in payload:
            return {"error": f"{field} is required"}

    save_feedback(payload)

    return {"status": "feedback saved"}

