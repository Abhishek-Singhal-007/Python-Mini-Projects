import qrcode as qr
qr = qr.QRCode(version=1, error_correction=qr.constants.ERROR_CORRECT_H, box_size=10,border=4,)
# QRcode change the functionality of qr.
link = input("Enter any link that you convert to QR -:-")
qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("QR.png")