import requests
from config import CARTESIA_API_KEY

def synthesize_cartesia(text):
    response = requests.post("https://api.cartesia.ai/v1/tts", json={
        "text": text,
        "voice": "emily"  # Replace with your chosen voice ID
    }, headers={"Authorization": f"Bearer {CARTESIA_API_KEY}"})

    if response.ok:
        return response.json().get("audio_url")
    else:
        raise requests.exceptions.RequestException(f"Cartesia failed: {response.text}")
