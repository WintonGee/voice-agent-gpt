from flask import Flask, request, Response
from agent import GPTVoiceAgent
from stt import transcribe_audio
from tts import synthesize_cartesia
from emailer import send_appointment_email
from config import PUBLIC_URL

app = Flask(__name__)
agent = GPTVoiceAgent()

# ===========
# HELPERS
# ===========

def build_twiml_play_and_record(audio_url: str) -> str:
    return f"""
    <Response>
        <Play>{audio_url}</Play>
        <Record action="/transcribe" maxLength="6" playBeep="true" />
    </Response>
    """

def build_twiml_say_and_record(prompt: str) -> str:
    return f"""
    <Response>
        <Say>{prompt}</Say>
        <Record action="/transcribe" maxLength="6" playBeep="true" />
    </Response>
    """

def build_twiml_final(audio_url: str, goodbye_url: str) -> str:
    return f"""
    <Response>
        <Play>{audio_url}</Play>
        <Play>{goodbye_url}</Play>
        <Hangup/>
    </Response>
    """

def build_twiml_error(message: str) -> str:
    return f"""
    <Response>
        <Say>{message}</Say>
        <Hangup/>
    </Response>
    """

# ===========
# ROUTES
# ===========

@app.route("/", methods=["GET"])
def index():
    return "🧠 Voice Agent Flask is running."

@app.route("/voice", methods=["POST"])
def voice():
    if agent.is_complete():
        return Response("<Response><Say>Thank you. Goodbye.</Say><Hangup/></Response>", mimetype="text/xml")

    current_field = agent.fields_order[agent.current_index]
    prompt = agent.prompts[current_field]

    try:
        audio_path = synthesize_cartesia(prompt)
        audio_url = f"{PUBLIC_URL}{audio_path}"
        twiml = build_twiml_play_and_record(audio_url)
    except Exception:
        twiml = build_twiml_say_and_record(prompt)

    return Response(twiml, mimetype="text/xml")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    recording_url = request.form.get("RecordingUrl")
    if not recording_url:
        return Response(build_twiml_error("No audio found."), mimetype="text/xml")

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

            twiml = build_twiml_final(audio_url, goodbye_url)
        else:
            # ✅ NO redirect — ask next question immediately
            twiml = build_twiml_play_and_record(audio_url)

    except Exception as e:
        print(f"❌ Error in /transcribe: {e}")
        twiml = build_twiml_error("Sorry, something went wrong. Please try again later.")

    return Response(twiml, mimetype="text/xml")

# ===========
# MAIN
# ===========

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
