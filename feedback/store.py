import csv
import os
from datetime import datetime

FEEDBACK_FILE = "data/feedback/corrections.csv"

HEADERS = [
    "timestamp",
    "ticket_text",
    "predicted_category",
    "corrected_category",
    "predicted_priority",
    "corrected_priority"
]

def save_feedback(feedback: dict):
    os.makedirs(os.path.dirname(FEEDBACK_FILE), exist_ok=True)
    file_exists = os.path.isfile(FEEDBACK_FILE)

    with open(FEEDBACK_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "timestamp": datetime.utcnow().isoformat(),
            "ticket_text": feedback["ticket_text"],
            "predicted_category": feedback["predicted_category"],
            "corrected_category": feedback["corrected_category"],
            "predicted_priority": feedback["predicted_priority"],
            "corrected_priority": feedback["corrected_priority"]
        })
