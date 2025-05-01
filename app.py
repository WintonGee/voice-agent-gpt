from flask import Flask, request, Response
from agent import GPTVoiceAgent
from stt import transcribe_audio
from tts import synthesize_cartesia
from emailer import send_appointment_email
from config import PUBLIC_URL  # <— for serving full audio URLs

app = Flask(__name__)

# AI agent instance
agent = GPTVoiceAgent()

@app.route("/", methods=["GET"])
def index():
    return "🧠 Voice Agent Flask is running."

@app.route("/voice", methods=["POST"])
def voice():
    # Entry point when a call hits your Twilio number
    if agent.is_complete():
        return Response("<Response><Say>Thank you. Goodbye.</Say><Hangup/></Response>", mimetype="text/xml")

    current_field = agent.fields_order[agent.current_index]
    prompt = agent.prompts[current_field]

    try:
        # Generate voice from prompt and return public URL
        audio_path = synthesize_cartesia(prompt)  # returns relative path like "/static/audio/output.wav"
        audio_url = f"{PUBLIC_URL}{audio_path}"

        twiml = f"""
        <Response>
            <Play>{audio_url}</Play>
            <Record action="/transcribe" maxLength="6" playBeep="true" />
        </Response>
        """
    except Exception:
        twiml = f"""
        <Response>
            <Say>{prompt}</Say>
            <Record action="/transcribe" maxLength="6" playBeep="true" />
        </Response>
        """

    return Response(twiml, mimetype="text/xml")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    recording_url = request.form.get("RecordingUrl")

    if not recording_url:
        return Response("<Response><Say>Error: No audio found.</Say><Redirect>/voice</Redirect></Response>", mimetype="text/xml")

    print(f"🎙️ Received recording: {recording_url}")

    try:
        text = transcribe_audio(recording_url)
        print(f"🗣️ Transcribed text: {text}")

        reply, done, data = agent.process_input(text)
        print(f"🤖 Agent reply: {reply}")

        audio_path = synthesize_cartesia(reply)
        audio_url = f"{PUBLIC_URL}{audio_path}"

        if done:
            print("✅ All info collected. Sending email...")
            send_appointment_email(data)

            goodbye_path = synthesize_cartesia("Your appointment is confirmed. Goodbye.")
            goodbye_url = f"{PUBLIC_URL}{goodbye_path}"

            twiml = f"""
            <Response>
                <Play>{audio_url}</Play>
                <Play>{goodbye_url}</Play>
                <Hangup/>
            </Response>
            """
        else:
            twiml = f"""
            <Response>
                <Play>{audio_url}</Play>
                <Redirect>/voice</Redirect>
            </Response>
            """

    except Exception as e:
        print(f"❌ Error in /transcribe: {e}")
        twiml = f"""
        <Response>
            <Say>Sorry, something went wrong. Please try again later.</Say>
            <Hangup/>
        </Response>
        """

    return Response(twiml, mimetype="text/xml")

if __name__ == "__main__":
    app.run(port=8080)
