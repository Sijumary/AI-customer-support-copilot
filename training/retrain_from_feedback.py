import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load original data
base = pd.read_csv("data/raw/tickets.csv")

# Load feedback
feedback = pd.read_csv("data/feedback/corrections.csv")

# Prepare feedback data
feedback_df = feedback[["ticket_text", "corrected_category"]]
feedback_df.columns = ["text", "category"]

# Combine
combined = pd.concat([base[["text", "category"]], feedback_df])

X = combined["text"]
y = combined["category"]

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=5000)),
    ("clf", LogisticRegression(max_iter=300))
])

pipeline.fit(X, y)

joblib.dump(pipeline, "models/classifier/ticket_classifier.pkl")

print("Model retrained with feedback")
