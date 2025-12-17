def assign_priority(category: str, sentiment: str) -> str:
    category = category.lower()
    sentiment = sentiment.upper()

    if sentiment == "NEGATIVE":
        if category in ["billing", "payment failed"]:
            return "HIGH"
        if category in ["app crash", "technical"]:
            return "MEDIUM"
        return "MEDIUM"

    if sentiment == "NEUTRAL":
        return "MEDIUM"

    return "LOW"


if __name__ == "__main__":
    print(assign_priority("Billing", "NEGATIVE"))
    print(assign_priority("App Crash", "NEGATIVE"))
    print(assign_priority("Promo Missing", "POSITIVE"))
