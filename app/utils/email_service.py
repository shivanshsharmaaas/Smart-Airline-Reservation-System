# def send_ticket_email(
#     user_email,
#     booking_id,
#     pdf_file
# ):

#     print("\n========== EMAIL SENT ==========")

#     print(f"To : {user_email}")

#     print("Subject : Flight Ticket")

#     print(
#         f"Booking ID : {booking_id}"
#     )

#     print(
#         f"Attached Ticket : {pdf_file}"
#     )

#     print("================================\n")

#     return True




import os
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


def send_ticket_email(
    user_email,
    booking_id,
    pdf_file
):

    sender_email = os.getenv(
        "EMAIL_ADDRESS"
    )

    sender_password = os.getenv(
        "EMAIL_PASSWORD"
    )

    msg = EmailMessage()

    msg["Subject"] = "Flight Ticket Confirmation"

    msg["From"] = sender_email

    msg["To"] = user_email

    msg.set_content(
        f"""
Hello,

Your flight booking has been confirmed.

Booking ID : {booking_id}

Please find the attached PDF ticket.

Thank You,
Smart Airline System
"""
    )

    with open(pdf_file, "rb") as f:

        file_data = f.read()

        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="pdf",
            filename=pdf_file
        )

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:

        smtp.login(
            sender_email,
            sender_password
        )

        smtp.send_message(msg)

    print(
        "REAL EMAIL SENT SUCCESSFULLY"
    )

    return True



    

