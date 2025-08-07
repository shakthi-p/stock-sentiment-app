import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os

# Load dataset
df = pd.read_csv("dataset/tweet_sentiment.csv")
print("📄 Available columns:", df.columns)

# Use correct column names
df.dropna(subset=["cleaned_tweets", "sentiment"], inplace=True)
X = df["cleaned_tweets"]
y = df["sentiment"]  # Assumed to be -1, 0, or 1

# Vectorize text
vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
X_vec = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_vec, y)

# Save model and vectorizer
os.makedirs("model", exist_ok=True)
with open("model/sentiment_model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print("✅ Model trained and saved to model/sentiment_model.pkl")
