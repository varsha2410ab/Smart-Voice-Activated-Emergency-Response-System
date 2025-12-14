import joblib
import speech_recognition as sr
import smtplib
from email.message import EmailMessage
import time
import winsound
import tkinter as tk
from tkinter import messagebox

model = joblib.load("ml_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

EMAIL_USER = "varshatiwari.projects@gmail.com"
EMAIL_PASS = "bbnblibxfmtnmfzl"
RECIPIENT = "varshatiwari.projects@gmail.com"

LOCATION = "Jalandhar, Punjab, India"

EMERGENCY_KEYWORDS = [
    "help", "help me", "save me", "emergency", "danger", "police", "fire", "attack",
    "bachao", "madad", "madad karo", "bacha lo", "mujhe bachao", "police bulao", "aag", "khatra"
]

def alert_beep():
    for _ in range(3):
        winsound.Beep(2000, 500)
        time.sleep(0.2)

def alert_popup():
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning("EMERGENCY ALERT", "Emergency detected!\nAlert has been sent.")
    root.destroy()

def send_email_alert(text):
    msg = EmailMessage()
    msg.set_content(
        f"!!! EMERGENCY DETECTED !!!\n\n"
        f"Message: {text}\n"
        f"Location: {LOCATION}"
    )
    msg["Subject"] = "Emergency Alert from SmartVoice System"
    msg["From"] = EMAIL_USER
    msg["To"] = RECIPIENT
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
        print("Alert email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)

def listen_to_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for emergency...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except:
        return ""

def keyword_detected(text):
    for word in EMERGENCY_KEYWORDS:
        if word in text:
            return True
    return False

def check_emergency(text):
    if not keyword_detected(text):
        return False
    vec = vectorizer.transform([text])
    return model.predict(vec)[0] == 1

if __name__ == "__main__":
    print("SmartVoice Emergency System is running. Press Ctrl+C to stop.")
    while True:
        speech_text = listen_to_voice()
        if speech_text.strip() == "":
            continue
        if check_emergency(speech_text):
            print("!!! EMERGENCY DETECTED !!!")
            alert_beep()
            alert_popup()
            send_email_alert(speech_text)
        else:
            print("No emergency detected.")
        time.sleep(1)
