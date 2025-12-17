from services.sentiment import analyze_sentiment
from services.priority import assign_priority
from services.responder import generate_response

import joblib

# Load trained classifier
model = joblib.load("models/classifier/ticket_classifier.pkl")

def run_copilot(ticket_text: str):
    # 1. Predict issue category
    category = model.predict([ticket_text])[0]

    # 2. Sentiment analysis
    sentiment_result = analyze_sentiment(ticket_text)

    # 3. Priority assignment
    priority = assign_priority(category, sentiment_result["label"])

    # 4. Generate suggested response
    response = generate_response(
        category,
        sentiment_result["label"],
        priority
    )

    return {
        "ticket_text": ticket_text,
        "predicted_category": category,
        "sentiment": sentiment_result,
        "priority": priority,
        "suggested_response": response
    }


if __name__ == "__main__":
    test_ticket = "The app crashed twice and my payment failed"
    result = run_copilot(test_ticket)
    print(result)
