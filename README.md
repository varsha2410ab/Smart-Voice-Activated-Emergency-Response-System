# SmartVoice-Activated Emergency Response System

![Project Preview](https://github.com/user-attachments/assets/9ba7b82c-1158-46e9-a21d-dfa0061513c1)

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

Emergency Detected Pop-up:
![IMG1](https://github.com/user-attachments/assets/9ba7b82c-1158-46e9-a21d-dfa0061513c1)

Terminal Output:
<img width="1600" height="531" alt="IMG2" src="https://github.com/user-attachments/assets/b3d2b125-3acf-4663-8f78-59cd18c20bcc" />

Email Alert:
<img width="1600" height="773" alt="IMG3" src="https://github.com/user-attachments/assets/647f4fc1-5892-4d2b-b6db-ce965b023b5f" />


## Technologies Used
- Python  
- Flask  
- Speech Recognition  
- NLP  
- Geolocation APIs

## License
MIT License
