from flask import Flask, request, render_template
import pickle
import os

app = Flask(__name__)

# Load model
model_path = os.path.join("model", "sentiment_model.pkl")
with open(model_path, "rb") as f:
    vectorizer, model = pickle.load(f)

def predict_sentiment(text):
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)[0]
    label_map = {1: "Positive ", 0: "Neutral ", -1: "Negative "}
    return label_map.get(prediction, "Unknown")

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = ""
    user_input = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        if user_input.strip():
            sentiment = predict_sentiment(user_input)
    return render_template("index.html", sentiment=sentiment, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)
