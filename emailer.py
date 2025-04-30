import sendgrid
from sendgrid.helpers.mail import Mail
from config import SENDGRID_API_KEY

def send_appointment_email(data):
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)

    recipients = [
        "wintongee1@gmail.com"
    ]

    content = "<br>".join([f"<strong>{k}:</strong> {v}" for k, v in data.items()])

    message = Mail(
        from_email="agent@assorthealth.com",
        to_emails=recipients,
        subject="🩺 New Patient Intake Submitted",
        html_content=f"""
        <h3>New Appointment Collected:</h3>
        {content}
        """
    )

    try:
        response = sg.send(message)
        print(f"📬 Email sent. Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Email failed: {e}")
