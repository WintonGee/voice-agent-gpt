from emailer import send_appointment_email

# Mocked patient intake data
mock_data = {
    "name": "Test Patient",
    "dob": "1990-01-01",
    "insurance": "BlueShield ID123456",
    "referral": "Dr. House",
    "complaint": "Migraine",
    "address": "123 Main St, Springfield, IL",
    "contact": "+15550001111, test@example.com",
    "appointment": "Dr. Jane – Monday @ 10AM"
}

print("📬 Sending test email with mocked data...")

try:
    send_appointment_email(mock_data)
    print("✅ Test email sent.")
except Exception as e:
    print(f"❌ Email failed: {e}")
