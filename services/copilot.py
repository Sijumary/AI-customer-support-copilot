from services.sentiment import analyze_sentiment
from services.priority import assign_priority
from services.responder import generate_response
from config.settings import CONFIDENCE_THRESHOLD
import uuid
from config.logging_config import get_logger
import joblib

logger = get_logger("copilot")
# Load trained classifier
model = joblib.load("models/classifier/ticket_classifier.pkl")

def run_copilot(ticket_text: str):
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

    logger.info(
        f"request_id={request_id} | "
        f"category={category} | "
        f"confidence={round(max_confidence, 2)} | "
        f"sentiment={sentiment_result['label']} | "
        f"priority={priority} | "
        f"escalated={escalated}"
    )

    return {
        "request_id": request_id,
        "ticket_text": ticket_text,
        "predicted_category": category,
        "confidence": round(max_confidence, 2),
        "sentiment": sentiment_result,
        "priority": priority,
        "escalated": escalated,
        "suggested_response": response
    }



if __name__ == "__main__":
    test_ticket = "The app crashed twice and my payment failed"
    result = run_copilot(test_ticket)
    print(result)
