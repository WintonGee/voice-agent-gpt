import requests
from config import CARTESIA_API_KEY

def synthesize_cartesia(text):
    response = requests.post("https://api.cartesia.ai/v1/tts", json={
        "text": text,
        "voice": "emily"  # pick voice from Cartesia dashboard
    }, headers={"Authorization": f"Bearer {CARTESIA_API_KEY}"})
    
    result = response.json()
    return result["audio_url"]
