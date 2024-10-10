pip install qrcode
pip install "qrcode[pil]"

#%% #simple generator

import qrcode
img = qrcode.make('data')
type(img)  # qrcode.image.pil.PilImage
img.save("file.png")


#%% cutomized generator
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
# img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))