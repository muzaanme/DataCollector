from email.mime.text import MIMEText
import smtplib

def send_email(email, height):
    from_email = "manasmant@gmail.com"
    from_password = "(mahantamadhurmanas)"
    to_email = email

    subject = "Height Data"
    message = f"Hey there! your height is <strong>{height}</strong>."

    msg = MIMEText(message, "html")
    msg["subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.startls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
