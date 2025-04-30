import os
import subprocess
from cartesia import Cartesia
from config import CARTESIA_API_KEY

client = Cartesia(api_key=CARTESIA_API_KEY)

def synthesize_cartesia(text, filename="output.wav"):
    if not CARTESIA_API_KEY:
        raise ValueError("CARTESIA_API_KEY is not set")

    audio_stream = client.tts.bytes(
        model_id="sonic-2",
        transcript=text,
        voice={
            "mode": "id",
            "id": "694f9389-aac1-45b6-b726-9d9369183238",  # Barbershop Man
        },
        language="en",
        output_format={
            "container": "wav",
            "sample_rate": 44100,
            "encoding": "pcm_f32le",
        },
    )

    with open(filename, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)

    print(f"🎧 Audio saved to: {filename}")

    try:
        subprocess.run(["ffplay", "-autoexit", "-nodisp", filename], check=True)
    except FileNotFoundError:
        print("⚠️  ffplay not found — skipping playback")

    return filename
