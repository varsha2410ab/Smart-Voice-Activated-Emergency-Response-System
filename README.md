# SmartVoice-Activated Emergency Response System

This AI-powered voice-controlled emergency response system listens for distress commands and automatically alerts trusted contacts with your real-time location. The system combines hands-free voice recognition, ML-based classification, GPS tracking, and email/SMS notifications to provide a practical solution for real-world emergencies.

---

## Features
- Continuously listens for emergency phrases via microphone
- Classifies type of emergency using a trained ML model
- Sends email/SMS alerts with real-time location
- Minimal setup; works silently in the background
- Easily extensible with new phrases or alert methods

---

## Project Structure

├── smart_emergency_system.py # Main program
├── train_model.py # Script to train the ML model
├── test_model.py # Script to test the model
├── ml_model.pkl # Saved trained model
├── vectorizer.pkl # Saved text vectorizer
├── venv/ # Virtual environment
├── README.md # This file

---

## How to Run
1. Activate virtual environment:  
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows

2. Run the main program:
python smart_emergency_system.py

## Tech Stack
Python, Flask, Speech Recognition, NLP, Geolocation APIs

## Output
![SmartVoice System Screenshot](screenshot.png)
