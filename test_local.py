from agent import GPTVoiceAgent
from tts import synthesize_cartesia
from emailer import send_appointment_email

agent = GPTVoiceAgent()

while True:
    user_input = input("🧍 You say: ")
    reply, done, data = agent.process_input(user_input)
    print("🤖 Agent replies:", reply)

    try:
        synthesize_cartesia(reply)
    except Exception as e:
        print(f"❌ TTS failed: {e}")

    if done:
        print("\n✅ Final collected data:")
        for k, v in data.items():
            print(f" - {k}: {v}")

        print("\n📬 Sending confirmation email...")
        try:
            send_appointment_email(data)
        except Exception as e:
            print(f"❌ Email failed: {e}")
        break
