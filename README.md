# Fake-News-Detector-Project
A simple machine learning-powered web app that detects whether a news article or headline is FAKE or REAL.
Built using Python, Flask, Scikit-learn, HTML, CSS, and JavaScript.

🚀 Features

Paste any news article/headline and get an instant prediction.
Shows FAKE (red) or REAL (green) clearly.
Clean, responsive interface with a loading spinner (⏳ Analyzing…).
Machine learning model trained on a labeled fake news dataset.
Uses TF-IDF Vectorization + Logistic Regression for predictions.

📂 Project Structure
FakeNewsDetector/
│── app.py                 # Flask backend
│── create_model.py         # Script to train & save the model
│── fake_news_model.pkl     # Saved ML model
│── tfidf_vectorizer.pkl    # Saved vectorizer
│── fake_news.csv           # Dataset (if included)
│── templates/
│   └── index.html          # Frontend HTML
│── static/
    ├── css/
    │   └── style.css       # Styling
    └── js/
        └── main.js         # Frontend logic

        

⚙️ Installation & Setup

1) Clone this repository
git clone https://github.com/your-username/FakeNewsDetector.git
cd FakeNewsDetector

2) Install dependencies
pip install -r requirements.txt
(If you don’t have a requirements.txt, install manually:)
pip install flask scikit-learn pandas numpy joblib


3) Run the app
python app.py


4) Open your browser and go to:
👉 http://127.0.0.1:5000



🎯 How It Works

User enters a news headline or article.
Text is preprocessed with TF-IDF vectorization.
The trained Logistic Regression model predicts if it’s fake or real.
Result is shown instantly in the UI.

📊 Future Improvements

Add confidence scores (e.g., Fake with 82% certainty).
Train using more advanced models (Naive Bayes, Random Forest, BERT).
Support multiple languages.
Deploy online (Heroku, Render, or Railway).
