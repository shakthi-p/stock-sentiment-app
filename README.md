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

#### Project Structure
stock-sentiment-app/
│
├── dataset/                # CSV dataset for training
│   └── tweet_sentiment.csv
│
├── model/                  # Trained model
│   └── sentiment_model.pkl
│
├── static/                 # Static files (CSS, JS if any)
│
├── templates/              # HTML Templates
│   └── index.html
│
├── app.py                  # Flask application
├── train_model.py          # Script to train model
├── requirements.txt        # Required Python packages

#### How to Run Locally

1. **Clone the repo**
git clone https://github.com/shakthi-p/stock-sentiment-app.git
cd stock-sentiment-app

2. **Create virtual environment (optional but recommended)**
python -m venv venv
venv\Scripts\activate  # For Windows
source venv/bin/activate  # For Mac/Linux

3. **Install dependencies**
pip install -r requirements.txt

4. **Run the app**
python app.py

5. **Open in browser**
   Go to `http://127.0.0.1:5000`
   
#### Screenshot
<img width="1919" height="1040" alt="Positive Tweet" src="https://github.com/user-attachments/assets/5ebdc8f1-4da0-4ef9-9a05-90b090eb60e9" />




