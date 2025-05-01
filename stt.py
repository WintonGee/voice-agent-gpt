import assemblyai as aai
import requests
import time
from config import ASSEMBLYAI_API_KEY, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

aai.settings.api_key = ASSEMBLYAI_API_KEY
config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.best)

def transcribe_audio(audio_url: str) -> str:
    print(f"🧠 Transcribing audio: {audio_url}")

    # Retry up to 5 times with backoff
    for attempt in range(5):
        response = requests.get(audio_url, auth=(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN))
        
        if response.status_code == 200:
            print("✅ Twilio recording downloaded.")
            break
        elif response.status_code == 404:
            print(f"⏳ Recording not ready (404), retrying ({attempt+1}/5)...")
            time.sleep(2 + attempt)  # backoff
        else:
            raise RuntimeError(f"❌ Unexpected download error: {response.status_code}")

    else:
        raise RuntimeError(f"❌ Failed to download Twilio recording after retries.")

    with open("recording.wav", "wb") as f:
        f.write(response.content)

    transcript = aai.Transcriber(config=config).transcribe("recording.wav")

    if transcript.status == "error":
        raise RuntimeError(f"❌ Transcription failed: {transcript.error}")

    print("✅ Transcription complete.")
    return transcript.text
