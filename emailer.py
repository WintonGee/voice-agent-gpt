from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config import SENDGRID_API_KEY

def send_appointment_email(data):
    # 👇 Must match verified sender from SendGrid
    from_email = "wintongee1@gmail.com"
    to_emails = [
        "wintongee@gmail.com",  # Change to Assort emails when verified
    ]

    html_content = "<h3>New Appointment Collected:</h3><br>" + \
        "<br>".join([f"<strong>{k}:</strong> {v}" for k, v in data.items()])

    message = Mail(
        from_email=from_email,
        to_emails=to_emails,
        subject="🩺 New Patient Intake Submitted",
        html_content=html_content
    )

    # Print the email and data that will be sent
    print("📬 Sending email with the following data:")
    print(f"From: {from_email}")
    print(f"To: {to_emails}")
    print(f"Subject: {message.subject}")
    print(f"HTML Content: {html_content}")

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"📬 Email sent! Status: {response.status_code}")
        return response.status_code == 202
    except Exception as e:
        print(f"❌ Email failed: {e}")
        return False
