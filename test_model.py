import joblib

# Load the trained model and vectorizer
model = joblib.load("SmartVoice-Activated-Emergency-Response-System/ml_model.pkl")
vectorizer = joblib.load("SmartVoice-Activated-Emergency-Response-System/vectorizer.pkl")

# Example input
sample_text = "I am in danger, please help!"

# Transform the input using the vectorizer
sample_vec = vectorizer.transform([sample_text])

# Predict
prediction = model.predict(sample_vec)
print("Predicted Emergency:", prediction[0])  # 1 = emergency, 0 = normal
