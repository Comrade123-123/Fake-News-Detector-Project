from flask import Flask, request, render_template, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        news = data.get("news", "").strip()

        if not news:
            return jsonify({"error": "No news text provided"}), 400

        X = vectorizer.transform([news])
        raw_pred = model.predict(X)[0]

        # Normalize labels
        result = "FAKE" if str(raw_pred).lower() in ("0", "fake") else "REAL"

        print("DEBUG:", news[:50], "->", raw_pred, "=>", result)  # 👈 log in console

        return jsonify({"prediction": result})
    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
