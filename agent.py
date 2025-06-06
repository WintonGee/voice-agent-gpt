import openai
from config import OPENAI_API_KEY
from validator import validate_us_address  # ✅ New import

openai.api_key = OPENAI_API_KEY

class GPTVoiceAgent:
    def __init__(self):
        self.collected = {}
        self.fields_order = [
            "name", "dob", "insurance", "referral",
            "complaint", "address", "contact", "appointment"
        ]
        self.prompts = {
            "name": "What is your full name?",
            "dob": "What is your date of birth?",
            "insurance": "Can you provide your insurance provider and ID?",
            "referral": "Do you have a referral? If so, from which doctor?",
            "complaint": "What is the reason for your visit today?",
            "address": "Can you tell me your complete address?",
            "contact": "What’s your phone number and (optionally) email?",
            "appointment": "Here are some available slots: Dr. Jane - Monday 10AM, Dr. Smith - Tuesday 3PM. Which would you prefer?"
        }
        self.current_index = 0  # track which field we're on

    def is_complete(self):
        return self.current_index >= len(self.fields_order)

    def process_input(self, user_input):
        field = self.fields_order[self.current_index]

        # GPT field extraction
        prompt = f"""Extract the user's {field} from this message: "{user_input}".
Only return the raw value. If it's not provided, return "None".
"""
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )
        answer = response['choices'][0]['message']['content'].strip()

        if answer.lower() != "none":
            # ✅ Address validation hook
            if field == "address" and not validate_us_address(answer):
                print("❌ Invalid address format. Asking again.")
                return "Hmm, that doesn't seem like a valid address. Can you say it again, including the ZIP code?", False, self.collected

            self.collected[field] = answer
            print(f"✅ Collected {field}: {answer}")
            self.current_index += 1
        else:
            print(f"❌ Could not extract {field}. Re-asking.")

        if self.is_complete():
            return "Thanks! All information is collected.", True, self.collected

        next_field = self.fields_order[self.current_index]
        return self.prompts[next_field], False, self.collected
