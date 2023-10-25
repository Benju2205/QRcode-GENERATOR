import qrcode

def generate_qrcode(text):
    
    qr = qrcode.QRCode(     #//we are only creating the qrcode without any data in it
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black",back_color="white")
    img.save("qrimg.png")

url = input("Enter your url: ")
generate_qrcode(url)