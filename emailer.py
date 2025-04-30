import sendgrid
from sendgrid.helpers.mail import Mail
from config import SENDGRID_API_KEY, TWILIO_EMAIL_RECIPIENTS

def send_appointment_email(data):
    message = Mail(
        from_email="agent@assorthealth.com",
        to_emails=TWILIO_EMAIL_RECIPIENTS,
        subject="New Patient Appointment Booked",
        html_content=f"""
        <strong>New appointment booked:</strong><br>
        Name: {data.get('name')}<br>
        DOB: {data.get('dob')}<br>
        Insurance: {data.get('insurance')}<br>
        Referral: {data.get('referral')}<br>
        Complaint: {data.get('complaint')}<br>
        Address: {data.get('address')}<br>
        Contact: {data.get('contact')}<br>
        Chosen Appointment: {data.get('appointment')}
        """
    )
    sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
    sg.send(message)
