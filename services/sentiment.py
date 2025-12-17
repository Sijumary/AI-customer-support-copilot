from transformers import pipeline

# Load sentiment model
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text: str) -> dict:
    text = text.lower()

    negative_keywords = ["angry", "frustrated", "refund", "not working", "crash", "failed"]
    positive_keywords = ["thanks", "great", "good", "love"]

    score = 0
    for word in negative_keywords:
        if word in text:
            score -= 1

    for word in positive_keywords:
        if word in text:
            score += 1

    if score < 0:
        label = "NEGATIVE"
    elif score > 0:
        label = "POSITIVE"
    else:
        label = "NEUTRAL"

    return {
        "label": label,
        "score": abs(score)
    }


if __name__ == "__main__":
    print(analyze_sentiment("The app crashed and I want a refund"))
