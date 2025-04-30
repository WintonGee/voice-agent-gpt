from agent import GPTVoiceAgent
from tts import synthesize_cartesia

agent = GPTVoiceAgent()

while True:
    user_input = input("🧍 You say: ")
    reply, done, data = agent.process_input(user_input)
    print("🤖 Agent replies:", reply)

    synthesize_cartesia(reply)

    if done:
        break

print("\n✅ Final collected data:")
for k, v in data.items():
    print(f" - {k}: {v}")
