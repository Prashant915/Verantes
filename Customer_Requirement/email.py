from django.core.mail import send_mail
from django.conf import settings

def send_otp_via_email(email,otp):
    subject="Verantes account verification email"
    print("this is email",otp)
    message=f'Your otp is {otp}'
    email_from=settings.EMAIL_HOST
    send_mail(subject,message,email_from,[email])