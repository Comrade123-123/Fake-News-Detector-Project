import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load your CSV dataset
df = pd.read_csv("fake_news.csv")

# Combine title and text if you have both
df['content'] = df['title'] + " " + df['text']

X = df['content']
y = df['label']

# Split (optional)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert text to numbers
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_train_tfidf = vectorizer.fit_transform(X_train)

# Train model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Save model and vectorizer as .pkl files
joblib.dump(model, "fake_news_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

print("✅ Model and vectorizer saved as .pkl files!")
