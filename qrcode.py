# Installing qrcode lib

pip install pyqrcode

# Importing library
import pyqrcode

# Data to be encoded
data = 'place-here-your-url-or-other-data'

# Encoding data using make() function
img = pyqrcode.create(data)

# Saving as an image file
img.png('myQRCode.png')

# Saving as an SVG code
img.svg("qrCode.svg", scale = 8)