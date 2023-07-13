# Generate QRcode for a url

import qrcode
import Image

def generate_qr():

    qr = qrcode.QRcode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border=4
    )
    url = input('Enter a URL: ')
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fillcolor='black', back_color='white')
    img.save('qrimg.png')

generate_qr()