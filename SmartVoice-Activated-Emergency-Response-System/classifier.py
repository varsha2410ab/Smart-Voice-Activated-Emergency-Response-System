import joblib
import os

# Load trained model and vectorizer
model = joblib.load('ml_model.pkl')        # Logistic Regression model
vectorizer = joblib.load('vectorizer.pkl') # TF-IDF vectorizer

def predict_emergency(text):
    text = [text]
    X = vectorizer.transform(text)
    prediction = model.predict(X)[0]
    return prediction   # 1 = emergency, 0 = non-emergency
