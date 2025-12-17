from services.sentiment import analyze_sentiment
from services.priority import assign_priority
from services.responder import generate_response
from config.settings import CONFIDENCE_THRESHOLD
import uuid
from config.logging_config import get_logger
import joblib
import time
from monitoring.metrics import metrics


logger = get_logger("copilot")
# Load trained classifier
model = joblib.load("models/classifier/ticket_classifier.pkl")

def run_copilot(ticket_text: str):
    start_time = time.time()

    request_id = str(uuid.uuid4())

    probs = model.predict_proba([ticket_text])[0]
    max_confidence = max(probs)
    category = model.classes_[probs.argmax()]

    sentiment_result = analyze_sentiment(ticket_text)
    priority = assign_priority(category, sentiment_result["label"])

    escalated = max_confidence < CONFIDENCE_THRESHOLD

    if escalated:
        response = "This ticket has been escalated to a support specialist for further review."
    else:
        response = generate_response(
            category,
            sentiment_result["label"],
            priority
        )

    latency = time.time() - start_time

    # 🔥 Record metrics
    metrics.record(
        latency=latency,
        confidence=max_confidence,
        priority=priority,
        escalated=escalated
    )

    logger.info(
        f"request_id={request_id} | "
        f"category={category} | "
        f"confidence={round(max_confidence, 2)} | "
        f"priority={priority} | "
        f"escalated={escalated} | "
        f"latency_ms={round(latency * 1000, 2)}"
    )

    return {
        "request_id": request_id,
        "predicted_category": category,
        "confidence": round(max_confidence, 2),
        "sentiment": sentiment_result,
        "priority": priority,
        "escalated": escalated,
        "latency_ms": round(latency * 1000, 2),
        "suggested_response": response
    }




if __name__ == "__main__":
    test_ticket = "The app crashed twice and my payment failed"
    result = run_copilot(test_ticket)
    print(result)


from monitoring.metrics import metrics
print("METRICS SNAPSHOT:", metrics.snapshot())