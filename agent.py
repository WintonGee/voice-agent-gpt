import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

class GPTVoiceAgent:
    def __init__(self):
        self.collected = {}
        self.required_fields = [
            "name", "dob", "insurance", "referral",
            "complaint", "address", "contact", "appointment"
        ]

    def is_complete(self):
        return all(k in self.collected for k in self.required_fields)

    def process_input(self, user_input):
        prompt = f"""
You are a helpful medical intake assistant. Ask questions to gather the following:

- Patient's name
- Date of birth
- Insurance info (payer + ID)
- Referral and referring physician (if applicable)
- Chief complaint
- Address (must be complete)
- Contact (phone number, optional email)
- Then offer a fake appointment (doctor + time)

Here’s what we have so far: {self.collected}

User says: "{user_input}"

Reply conversationally AND provide JSON like this:

{{
  "name": "...",
  "dob": "...",
  "insurance": "...",
  "referral": "...",
  "complaint": "...",
  "address": "...",
  "contact": "...",
  "appointment": "..."
}}
"""
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6
        )

        reply = response['choices'][0]['message']['content']

        # Naive JSON extraction (mock - for real use, use json mode/function calling)
        # You should replace this with proper JSON parsing
        if "Sarah Smith" in user_input:
            self.collected["name"] = "Sarah Smith"
        if "May 2" in user_input or "born" in user_input:
            self.collected["dob"] = "1985-05-02"
        # Extend similar checks...

        return reply, self.is_complete(), self.collected
