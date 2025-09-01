# 📰 Fake News Detector  

A simple **machine learning-powered web app** that detects whether a news article or headline is **FAKE** or **REAL**.  
Built using **Python, Flask, Scikit-learn, HTML, CSS, and JavaScript**.  

---

## 🚀 Features
- Paste any news article/headline and get an instant prediction.  
- Shows **FAKE (red)** or **REAL (green)** clearly.  
- Clean, responsive interface with a loading spinner (`⏳ Analyzing…`).  
- Machine learning model trained on a labeled fake news dataset.  
- Uses **TF-IDF Vectorization** + **Logistic Regression** for predictions.  

---

## 📂 Dataset
Due to GitHub file size limits, datasets are hosted externally.  
You can download them here:  

- [Fake.csv](https://drive.google.com/file/d/1eNVikjB5k5ceUVei8UI6PPhN_XyykfpL/view?usp=drive_link)  
- [True.csv](https://drive.google.com/file/d/1DDlkGAf7OUTvu9-2ukT2QQi0E09Tclm1/view?usp=drive_link)  
- [fake_news.csv](https://drive.google.com/file/d/1KAy7S0UyeCJSJ4LbnjRsak1ihyvJcY5F/view?usp=drive_link)  

---

## 📂 Project Structure
FakeNewsDetector/
│── app.py # Flask backend
│── create_model.py # Script to train & save the model
│── fake_news_model.pkl # Saved ML model
│── tfidf_vectorizer.pkl # Saved vectorizer
│── fake_news.csv # Dataset (large file, hosted externally)
│── templates/
│ └── index.html # Frontend HTML
│── static/
│ ├── css/
│ │ └── style.css # Styling
│ └── js/
│ └── main.js # Frontend logic



---

## ⚙️ Installation & Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/Comrade123-123/Fake-News-Detector-Project.git
   cd Fake-News-Detector-Project
2. Install dependencies

pip install -r requirements.txt


##If you don’t have a requirements.txt, install manually:

pip install flask scikit-learn pandas numpy joblib

3. Run the app
   python app.py


4. Open your browser and go to:
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
Deploy online (Heroku, Render, or Railway)
