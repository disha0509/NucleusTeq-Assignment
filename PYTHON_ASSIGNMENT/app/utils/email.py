import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi import HTTPException,status
from dotenv import load_dotenv

load_dotenv()

def sending_email_with_token(sender,receiver,reset_token,receiver_name):

    password = os.getenv("EMAIL_PASSWORD")

    subject_line = "Password Reset Token for E-commerce login"
    
    body = f"""
Hi {receiver_name},

We received a request to reset your password for your E-commerce account.

Your password reset token is:

    {reset_token}

This token is valid for 5 minutes. Please use it to reset your password as soon as possible.

If you did not request a password reset, you can safely ignore this email.

Thank you,
E-commerce Support Team
"""

    msg  = MIMEMultipart()

    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject_line

    msg.attach(MIMEText(body,"plain"))


    try:
        with smtplib.SMTP("smtp.gmail.com",587) as my_server:
            my_server.starttls()
            my_server.login(sender,password)
            my_server.sendmail(sender,receiver,msg.as_string())
            print("email sent successfully")

    except Exception as e:
        print("Error in sending mail : ",e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to send reset email. Please try again later.")