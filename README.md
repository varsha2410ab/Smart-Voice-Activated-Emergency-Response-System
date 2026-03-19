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

## Run the Project
Run the main program:

python smart_emergency_system.py

This will start the system, which continuously listens for emergency commands and sends alerts automatically to designated contacts.

## Output
The system provides real-time notifications and logs when an emergency command is detected. Below are the screenshots illustrating the workflow:
![IMG1](https://github.com/user-attachments/assets/9ba7b82c-1158-46e9-a21d-dfa0061513c1)
<img width="1600" height="531" alt="IMG2" src="https://github.com/user-attachments/asset<img width="1600" height="773" alt="IMG3" src="https://github.com/user-attachments/assets/cee8e288-fbb0-4431-b828-bfa8f1844c6c" />
s/598f6504-bd78-419d-918c-c12bd407b2cf" />


## Technologies Used
- Python  
- Flask  
- Speech Recognition  
- NLP  
- Geolocation APIs

## License
MIT License
