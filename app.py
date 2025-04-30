from flask import Flask, request, jsonify
from agent import GPTVoiceAgent
from tts import synthesize_cartesia
from emailer import send_appointment_email
import os

app = Flask(__name__)
agent = GPTVoiceAgent()

@app.route("/voice", methods=["POST"])
def voice_webhook():
    data = request.form
    caller = data.get("From")
    speech = data.get("SpeechResult")

    reply, done, collected = agent.process_input(speech)

    if done:
        send_appointment_email(collected)

    audio_url = synthesize_cartesia(reply)
    return f"""
    <Response>
        <Play>{audio_url}</Play>
        <Pause length="1"/>
        <Redirect>/voice</Redirect>
    </Response>
    """

@app.route("/")
def index():
    return "Voice Agent is live."
