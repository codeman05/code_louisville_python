from django.conf import settings

import random
import qrcode
import numpy
import png


def get_barcode_number():
    # Generates a random number to be used.
    x = random.randint(1000000, 990000000)  # Create a random number to be use for barcode.

    return x


def generate_qrcode(x):
    # Takes a randomly generated number and turns it into an array matrix.
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=6,
        border=0
    )
    qr.add_data(x)
    qr.make(fit=True)

    img = qr.make_image()

    # Save QR code as a numbered array.
    output = numpy.asarray(img)

    return output


def print_qrcode(x, y):
    # Accepts two arguments: the first is the barcode array matrix, the second is the filename used to save image.
    static_root = settings.STATIC_ROOT
    filename = static_root + '/barcodes/{}.png'.format(x)
    png.from_array(y, 'L').save(filename)

    return filename

def get_barcode():
    data_to_encode = get_barcode_number()
    barcode_array = generate_qrcode(data_to_encode)  # Generate the barcode array matrix.
    print_qrcode(data_to_encode, barcode_array)  # Transform barcode array matrix to an image and save file.

    return data_to_encode
