import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
CARTESIA_API_KEY = os.getenv("CARTESIA_API_KEY")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
VALIDATOR_API_KEY = os.getenv("VALIDATOR_API_KEY")  # SmartyStreets
TWILIO_EMAIL_RECIPIENTS = ["jeff@assorthealth.com", "connor@assorthealth.com", "cole@assorthealth.com"]