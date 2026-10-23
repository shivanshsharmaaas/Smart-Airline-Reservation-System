import qrcode


def generate_ticket_qr(data):

    qr = qrcode.make(data)

    file_name = f"{data}.png"

    qr.save(file_name)

    return file_name



