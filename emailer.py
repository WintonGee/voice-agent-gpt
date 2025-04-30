import sendgrid
from sendgrid.helpers.mail import Mail
from config import SENDGRID_API_KEY

def send_appointment_email(data):
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    message = Mail(
        from_email="agent@assorthealth.com",
        to_emails=["your.email@example.com"],  # Use test email first
        subject="✅ New Appointment Booked",
        html_content=f"""
        <strong>New Intake:</strong><br><br>
        Name: {data.get('name')}<br>
        DOB: {data.get('dob')}<br>
        Insurance: {data.get('insurance')}<br>
        Referral: {data.get('referral')}<br>
        Complaint: {data.get('complaint')}<br>
        Address: {data.get('address')}<br>
        Contact: {data.get('contact')}<br>
        Appointment: {data.get('appointment')}
        """
    )
    sg.send(message)
