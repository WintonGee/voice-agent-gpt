import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CARTESIA_API_KEY = os.getenv("CARTESIA_API_KEY")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
