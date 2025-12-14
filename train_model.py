from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Step 1: Small labeled dataset
emergency_sentences = [
    "help me", "please help", "emergency", "save me",
    "i am in danger", "someone is attacking me",
    "i need help", "please save me", "kidnap", "attack"
]

normal_sentences = [
    "hello how are you", "what is the time",
    "open the door", "play music", "i am going home",
    "turn on the light", "call my friend",
    "i am tired", "i am sleepy"
]

HINDI_EMERGENCY_KEYWORDS = [
    "bachao", "madad", "madad karo", "bacha lo", 
    "danger hai", "kidnap", "mujhe bachao",
    "mujhe madad chahiye", "mujhe bacha lo", 
    "dhoka", "hamla", "hamla hua", "attack"
]


X = emergency_sentences + normal_sentences
y = [1]*len(emergency_sentences) + [0]*len(normal_sentences)  # 1 = emergency, 0 = normal

# Step 2: Vectorize text using TF-IDF
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Step 3: Train Logistic Regression classifier
model = LogisticRegression()
model.fit(X_vec, y)

# Step 4: Save the model and vectorizer using joblib
joblib.dump(model, 'ml_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Model trained and saved successfully!")
