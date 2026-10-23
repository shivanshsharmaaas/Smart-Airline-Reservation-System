# from reportlab.pdfgen import canvas


# def generate_ticket_pdf(
#     booking_id,
#     user_id,
#     flight_id,
#     seat_no
# ):

#     file_name = f"TICKET-{booking_id}.pdf"

#     pdf = canvas.Canvas(file_name)

#     pdf.setFont("Helvetica-Bold", 16)

#     pdf.drawString(
#         180,
#         800,
#         "AIRLINE TICKET"
#     )

#     pdf.setFont(
#         "Helvetica",
#         12
#     )

#     pdf.drawString(
#         100,
#         720,
#         f"Booking ID : {booking_id}"
#     )

#     pdf.drawString(
#         100,
#         690,
#         f"User ID : {user_id}"
#     )

#     pdf.drawString(
#         100,
#         660,
#         f"Flight ID : {flight_id}"
#     )

#     pdf.drawString(
#         100,
#         630,
#         f"Seat Number : {seat_no}"
#     )

#     pdf.save()

#     return file_name




from reportlab.pdfgen import canvas


def generate_ticket_pdf(
    booking_id,
    user_id,
    flight_id,
    seat_no
):

    file_name = f"TICKET-{booking_id}.pdf"

    pdf = canvas.Canvas(file_name)

    pdf.setFont(
        "Helvetica-Bold",
        18
    )

    pdf.drawString(
        180,
        800,
        "AIRLINE TICKET"
    )

    pdf.setFont(
        "Helvetica",
        12
    )

    pdf.drawString(
        100,
        740,
        f"Booking ID : {booking_id}"
    )

    pdf.drawString(
        100,
        710,
        f"User ID : {user_id}"
    )

    pdf.drawString(
        100,
        680,
        f"Flight ID : {flight_id}"
    )

    pdf.drawString(
        100,
        650,
        f"Seat Number : {seat_no}"
    )

    qr_file = f"BOOKING-{booking_id}.png"

    pdf.drawImage(
        qr_file,
        100,
        420,
        width=150,
        height=150
    )

    pdf.save()

    return file_name


    