import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import os
import joblib

# Load data
data = pd.read_csv("data/raw/tickets.csv", encoding='latin1', on_bad_lines='skip')


X = data["text"]
y = data["category"]

# Build pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("clf", LogisticRegression(max_iter=200))
])

# Train model
model.fit(X, y)

# Ensure the directory exists
os.makedirs("models/classifier", exist_ok=True)

# Save model
joblib.dump(model, "models/classifier/ticket_classifier.pkl")

print("✅ Ticket classification model trained and saved.")
