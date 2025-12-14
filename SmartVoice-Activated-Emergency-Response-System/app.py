from classifier import predict_emergency
from flask import Flask, request, render_template, jsonify
import os
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# Load email credentials from environment variables for safety
EMAIL_USER = os.environ.get('EMAIL_USER')  # your gmail address
EMAIL_PASS = os.environ.get('EMAIL_PASS')  # app password or smtp password
RECIPIENT = os.environ.get('RECIPIENT')    # emergency contact email

if not EMAIL_USER or not EMAIL_PASS or not RECIPIENT:
    print("WARNING: EMAIL_USER, EMAIL_PASS or RECIPIENT environment variables not set. See README.md for setup.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alert', methods=['POST'])
def alert():
    data = request.get_json()
    if not data:
        return jsonify({'status':'error','message':'No JSON received'}), 400

    transcript = data.get('transcript', '[no transcript]')
    coords = data.get('coords')  # expected {lat: ..., lon: ...} or None
    
    # ---- SUPERVISED LEARNING PREDICTION ADDED HERE ----
    prediction = predict_emergency(transcript)

    if prediction == 1:
        emergency_status = "Emergency Detected"
    else:
        emergency_status = "No Emergency"
    # ----------------------------------------------------

    location_link = 'Location not provided'
    if coords and 'lat' in coords and 'lon' in coords:
        location_link = f"https://www.google.com/maps/search/?api=1&query={coords['lat']},{coords['lon']}"

    # Build email ONLY if emergency detected
    if prediction == 1:
        subject = 'EMERGENCY ALERT - SmartVoice System'
        body = (
            f"An emergency voice trigger was detected.\n\n"
            f"Transcript: {transcript}\n"
            f"ML Prediction: {emergency_status}\n\n"
            f"Location: {location_link}\n\n"
            "This message was sent by SmartVoice-Activated Emergency Response System."
        )

        try:
            send_email(subject, body)

        except Exception as e:
            return jsonify({'status':'error','message': str(e)}), 500

    # Always return ML prediction to frontend
    return jsonify({
        'status': 'ok',
        'prediction': emergency_status,
        'location': location_link
    })


def send_email(subject, body):
    if not EMAIL_USER or not EMAIL_PASS or not RECIPIENT:
        raise RuntimeError('Email credentials or recipient not configured in environment variables.')

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_USER
    msg['To'] = RECIPIENT
    msg.set_content(body)

    # Gmail SMTP
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(msg)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
