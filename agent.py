import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

class GPTVoiceAgent:
    def __init__(self):
        self.collected = {}
        self.required_fields = ["name", "dob", "insurance", "referral", "complaint", "address", "contact", "appointment"]
    
    def is_complete(self):
        return all(k in self.collected for k in self.required_fields)

    def process_input(self, user_input):
        prompt = f"""
You are a medical intake assistant. Collect:
- Name, DOB
- Insurance (payer + ID)
- Referral (Y/N and doctor name)
- Chief complaint
- Address
- Phone and optional email
- Suggest available doctors + times
Return answers as JSON.
User says: {user_input}
"""
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5
        )
        reply = response['choices'][0]['message']['content']
        # Parse and update internal state here
        # e.g. self.collected["name"] = ...
        return reply, self.is_complete(), self.collected
