from agent import GPTVoiceAgent
from tts import synthesize_cartesia
from emailer import send_appointment_email

agent = GPTVoiceAgent()

while not agent.is_complete():
    user_input = input("🧍 You say: ")
    reply, done, data = agent.process_input(user_input)
    print("🤖 Agent replies:", reply)

    try:
        audio_url = synthesize_cartesia(reply)
        print(f"🎧 Voice output URL: {audio_url}")
    except Exception as e:
        print(f"❌ TTS failed: {e}")

print("\n✅ Data collected:")
print(data)

print("📧 Sending confirmation email...")
send_appointment_email(data)
print("✅ Email sent.")
