# SmartVoice-Activated Emergency Response System (Demo)

## What this demo does
- Uses browser Speech Recognition (Web Speech API) to listen for trigger words: **"help"** or **"emergency"**.
- Uses browser Geolocation API to get coordinates (if the user allows).
- Sends a POST request to the Flask backend `/alert` endpoint.
- Backend sends an email to your emergency contact (configured via environment variables).

> This design avoids needing microphone drivers or Python `speech_recognition` libraries and works entirely in the browser + simple Flask server.

## Files
- `app.py` - Flask backend which accepts `/alert` and sends email.
- `templates/index.html` - frontend UI; starts/stops listening and sends alerts.
- `static/script.js` - frontend logic (Web Speech API + Geolocation).
- `requirements.txt` - minimal dependency list.

## Setup (Linux / Windows using Git Bash / WSL / Mac)
1. Create a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Configure environment variables (IMPORTANT):
   - `EMAIL_USER` = your SMTP email (Gmail address recommended)
   - `EMAIL_PASS` = SMTP password (for Gmail, create an App Password)
   - `RECIPIENT` = emergency recipient email (who will receive alerts)

   Example (Linux / Mac):
   ```bash
   export EMAIL_USER='youremail@gmail.com'
   export EMAIL_PASS='yourapppassword'
   export RECIPIENT='friend@example.com'
   ```
   Windows (PowerShell):
   ```powershell
   $env:EMAIL_USER='youremail@gmail.com'
   $env:EMAIL_PASS='yourapppassword'
   $env:RECIPIENT='friend@example.com'
   ```

3. Run the app:
   ```bash
   python app.py
   ```
   Open `http://127.0.0.1:5000` in Chrome (desktop recommended). Allow microphone and location access.

## Notes & Troubleshooting
- Use Chrome desktop for best Web Speech API support.
- If the email does not send, check credentials and allow less secure apps or use Gmail App Passwords.
- This is a minimal demo suitable for a project submission. You can extend it to:
  - Send SMS via Twilio
  - Add authentication
  - Store logs into a database
  - Use push notifications

## Quick demo for submission
- Run server, open page, click "Start Listening", say "help" clearly, take screenshots of the page and the received email, and include them in your report.

Good luck! If you want, I can also generate a short PPT and a report you can copy-paste into your submission.
