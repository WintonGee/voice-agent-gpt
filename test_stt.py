from stt import transcribe_audio

# You can use a sample file from AssemblyAI or a Twilio RecordingUrl
# Replace this with a real Twilio-recorded file if needed
sample_audio_url = "https://storage.googleapis.com/aai-web-samples/5_common_sports_injuries.mp3"

print("🎧 Testing transcription...")
try:
    text = transcribe_audio(sample_audio_url)
    print("🗣️ Transcript:")
    print(text)
except Exception as e:
    print(f"❌ Transcription failed: {e}")
