import smtplib
from twilio.rest import Client

TWILIO_SID = "AC17c1e377008871012cc65605a65ba602"
TWILIO_AUTH_TOKEN = "7f2c786b69cdd61cdd169bd5cf6c1d7d"
TWILIO_VIRTUAL_NUMBER = "+12708133095"
TWILIO_VERIFIED_NUMBER = "+91 9389872806"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "as9389872806@gmail.com"
MY_PASSWORD = "Arun@123"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )