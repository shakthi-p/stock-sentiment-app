### Stock Sentiment App
A simple Flask-based web app that predicts **stock market sentiment** (Positive, Neutral, or Negative) based on tweets using a machine learning model trained on labeled tweet data.

#### Features
- Sentiment analysis of tweets related to stock market.
- Trained using Naive Bayes and CountVectorizer.
- Built using Python, Flask, HTML, and Bootstrap.
- Predicts sentiment live using a saved `.pkl` model.

#### ML Model
- `train_model.py` trains the model.
- Saves the model as `model/sentiment_model.pkl`.

**Project Structure:**

1 `dataset/` – Contains the training dataset
  >`tweet_sentiment.csv` – The CSV file with labeled tweet data
2 `model/` – Contains the trained machine learning model
  >`sentiment_model.pkl` – Saved model file
3`static/` – Folder for static files (e.g., CSS, JavaScript)
4 `templates/` – Contains HTML templates
   >`index.html` – Main page of the app
5 `app.py` – Flask web application script
6 `train_model.py` – Script to train the sentiment analysis model
7`requirements.txt` – List of Python dependencies

#### How to Run Locally

1. **Clone the repo**
git clone https://github.com/shakthi-p/stock-sentiment-app.git

cd stock-sentiment-app

3. **Create virtual environment (optional but recommended)**
python -m venv venv

venv\Scripts\activate  # For Windows


5. **Install dependencies**
pip install -r requirements.txt

6. **Run the app**
python app.py

7. **Open in browser**
   Go to `http://127.0.0.1:5000`
   
#### Screenshot
<img width="1919" height="1040" alt="Positive Tweet" src="https://github.com/user-attachments/assets/5ebdc8f1-4da0-4ef9-9a05-90b090eb60e9" />




