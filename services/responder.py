def generate_response(category, sentiment, priority):
    if priority == "HIGH":
        opening = "We sincerely apologize for the inconvenience."
    elif sentiment == "NEGATIVE":
        opening = "Thank you for bringing this to our attention."
    else:
        opening = "Thanks for reaching out!"

    body_map = {
        "Payment Failed": "Our team is actively investigating the payment issue.",
        "App Crash": "We are aware of the app stability issue and are working on a fix.",
        "Billing": "We are reviewing your billing concern carefully.",
        "Promo Missing": "We are checking the promo application on your account."
    }

    body = body_map.get(category, "Our support team is reviewing your request.")

    closing = "We appreciate your patience and will update you shortly."

    return f"{opening} {body} {closing}"


if __name__ == "__main__":
    print(generate_response("Payment Failed", "NEGATIVE", "HIGH"))
