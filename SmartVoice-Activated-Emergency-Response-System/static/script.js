const startBtn = document.getElementById('startBtn');
const stopBtn = document.getElementById('stopBtn');
const manualBtn = document.getElementById('manualBtn');
const statusEl = document.getElementById('status');
const lastEl = document.getElementById('last');
const resultEl = document.getElementById('result');
const recipientInput = document.getElementById('recipient');

let recognition;
let listening = false;

function updateStatus(s) {
    statusEl.textContent = 'Status: ' + s;
}

function postAlert(transcript, coords) {
    // set RECIPIENT input into server env via a quick request (for demo only we send it in body so backend can print warning)
    const payload = { transcript, coords, recipient: recipientInput.value };
    resultEl.textContent = 'Sending alert...';
    fetch('/alert', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify(payload)
    }).then(r => r.json())
      .then(j => {
         if(j.status === 'ok') {
             resultEl.textContent = 'Alert sent! Location: ' + (j.location || 'unknown');
         } else {
             resultEl.textContent = 'Error: ' + (j.message || 'unknown');
         }
      }).catch(e => {
         resultEl.textContent = 'Error sending alert: ' + e;
      });
}

function getLocationThenSend(transcript) {
    if (!navigator.geolocation) {
        postAlert(transcript, null);
        return;
    }
    navigator.geolocation.getCurrentPosition(function(pos) {
        const coords = { lat: pos.coords.latitude, lon: pos.coords.longitude };
        postAlert(transcript, coords);
    }, function(err) {
        // if user denies or fails, still send without coords
        postAlert(transcript, null);
    }, {enableHighAccuracy:true, timeout:8000});
}

// Set up Web Speech API
if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
    updateStatus('Web Speech API not supported in this browser. Use Chrome desktop for best results.');
} else {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    recognition = new SpeechRecognition();
    recognition.lang = 'en-IN';
    recognition.interimResults = false;
    recognition.continuous = true;

    recognition.onstart = function() {
        listening = true;
        updateStatus('Listening...');
        startBtn.disabled = true;
        stopBtn.disabled = false;
    };

    recognition.onend = function() {
        listening = false;
        updateStatus('Stopped');
        startBtn.disabled = false;
        stopBtn.disabled = true;
    };

    recognition.onerror = function(e) {
        updateStatus('Error: ' + e.error);
    };

    recognition.onresult = function(event) {
        const transcript = Array.from(event.results)
            .slice(event.resultIndex)
            .map(r => r[0].transcript)
            .join('\n').toLowerCase();
        lastEl.textContent = 'Last transcript: ' + transcript;
        // trigger words: help, emergency
        if (transcript.includes('help') || transcript.includes('emergency')) {
            updateStatus('Trigger detected: ' + transcript);
            getLocationThenSend(transcript);
        }
    };
}

startBtn.addEventListener('click', () => {
    // save recipient email by sending to server environment via fetch? For demo, we just inform user to set env vars.
    updateStatus('Requesting microphone access...');
    try {
        recognition.start();
    } catch (e) {
        updateStatus('Could not start recognition: ' + e);
    }
});

stopBtn.addEventListener('click', () => {
    if (recognition && listening) recognition.stop();
});

manualBtn.addEventListener('click', () => {
    const text = prompt('Enter short message to send with alert (e.g. I need help):', 'I need help');
    if (!text) return;
    getLocationThenSend(text);
});
