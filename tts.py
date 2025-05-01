import os
from cartesia import Cartesia
from config import CARTESIA_API_KEY

client = Cartesia(api_key=CARTESIA_API_KEY)

def synthesize_cartesia(text: str) -> str:
    filename = f"output.wav"
    filepath = f"static/audio/{filename}"

    audio_bytes = client.tts.bytes(
        model_id="sonic-2",
        transcript=text,
        voice={
            "mode": "id",
            "id": "694f9389-aac1-45b6-b726-9d9369183238",
        },
        language="en",
        output_format={
            "container": "wav",
            "sample_rate": 44100,
            "encoding": "pcm_f32le",
        },
    )

    with open(filepath, "wb") as f:
        f.write(b"".join(audio_bytes))


    # This is the public URL that Twilio needs
    return f"{PUBLIC_URL}/static/audio/{filename}"
