📞 AI Voice Agent – Assort Health Take Home
An AI-powered phone intake system for medical appointments using OpenAI GPT-4, Deepgram, Cartesia, and Twilio, hosted via Google Cloud Run ☁️.

🧠 Features
✅ Real-time voice intake
✅ GPT-4 agent handles logic
✅ Deepgram for speech-to-text
✅ Cartesia for lifelike voice replies
✅ Smart address validation (SmartyStreets)
✅ Sends email confirmations via SendGrid
✅ Deployed as Docker container to GCP
✅ Callable via Twilio number

🧪 Demo Requirements
✅ What this agent does:
Collects:

Patient name and date of birth

Insurance details (payer + ID)

Referral (Y/N and physician)

Chief complaint

Address (with validation)

Contact info (phone/email)

Appointment choice from generated list

Refuses to complete call until all fields gathered

Sends confirmation email to:

jeff@assorthealth.com

connor@assorthealth.com

cole@assorthealth.com

🔧 Setup

1. Clone
   bash
   Copy
   Edit
   git clone https://github.com/YOUR_USERNAME/voice-agent-gpt.git
   cd voice-agent-gpt
2. Configure Environment
   Create a .env file based on the .env.example:

env
Copy
Edit
OPENAI_API_KEY=sk-...
DEEPGRAM_API_KEY=...
CARTESIA_API_KEY=...
SENDGRID_API_KEY=...
VALIDATOR_API_KEY=...
🐍 Local Dev
Create virtualenv + install deps:
bash
Copy
Edit
make venv
Run locally:
bash
Copy
Edit
make run
☁️ Cloud Run Deployment
Build container:
bash
Copy
Edit
make docker-build
Deploy to GCP:
bash
Copy
Edit
make deploy
☎️ Twilio Setup
Buy number at Twilio Console

Under "Voice & Fax" settings:

Webhook: https://<your-cloud-run-url>/voice

Method: POST

Now calling your number triggers the agent!

📦 Project Structure
txt
Copy
Edit
voice-agent-gpt/
├── app.py # Flask app entrypoint
├── agent.py # GPT-4 dialog logic
├── stt.py # Deepgram handler (optional live)
├── tts.py # Cartesia TTS
├── emailer.py # SendGrid integration
├── validator.py # Address validator
├── config.py # Env var management
├── Dockerfile # Cloud Run deploy config
├── Makefile # Automations (build, deploy, run)
├── requirements.txt # Python dependencies
├── README.md # This file
└── .env.example # Sample env
📽 Loom Video
🎥 Record a quick 3–5 minute Loom walking through:

Architecture + tech used

GPT integration

TTS/STT choices

Live demo (call recording encouraged)

Deployment method (Cloud Run)

✅ Deliverables Checklist

Item Status
📦 GitHub repo (private) ✅
📽 Loom explanation 🔄
☎️ Hosted call number ✅
