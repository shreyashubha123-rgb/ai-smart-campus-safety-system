from flask import Flask, request, jsonify
from emergency_detection import detect_emergency
from voice_assistant import process_voice_command
from sos_alert import send_sos_alert

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Smart Campus Safety & Assistance System is Running"

@app.route("/detect", methods=["POST"])
def detect():
    result = detect_emergency()
    return jsonify({"status": result})

@app.route("/voice", methods=["POST"])
def voice():
    data = request.json
    command = data.get("command", "")
    response = process_voice_command(command)
    return jsonify({"response": response})

@app.route("/sos", methods=["POST"])
def sos():
    location = request.json.get("location", "Unknown")
    alert = send_sos_alert(location)
    return jsonify({"alert": alert})

if __name__ == "__main__":
    app.run(debug=True)
