# SmartVoice-Activated Emergency Response System

## One-liner
AI-powered **voice-controlled emergency alert system** that detects distress, classifies the emergency, and instantly alerts trusted contacts with your real-time location.

## Features
- Continuously listens for emergency phrases via microphone  
- Classifies type of emergency using a trained ML model  
- Sends email/SMS alerts with real-time location  
- Minimal setup, works silently in the background  
- Can be extended with new phrases or alert methods  

## Project Structure
smart_emergency_system.py # Main program
train_model.py # Script to train the ML model
test_model.py # Script to test the model
ml_model.pkl # Saved trained model
vectorizer.pkl # Saved text vectorizer
venv/ # Virtual environment
README.md # This file

## License
MIT License
