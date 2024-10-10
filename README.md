# QR code generator with python

The 'qrcode.py' was made from previous testing on qrcode library.On the other hand, the 'qr-code.py' archive was forked of [lincolnloop repository](https://github.com/lincolnloop/python-qrcode).
 

## Simple usage with qrcode.py

### Place you data

To generate your qrcode, download and open the 'qrcode.py' archive. 

Next, you need change the data between the quotes:<br>
`data = 'place-here-your-url-or-other-data'`

Data can be an url from website, number or other type.

### Choose format

In sequence, change the output file format name.
Two format options are available: .png and .svg. Choose both or only one. You can remove deleting the line command or by comment line with '#'.

```
# Saving as an image file
img.png('myQRCode.png')

# Saving as an SVG code
img.svg("qrCode.svg", scale = 8)
```

Note: You can change size (the default is 8). Try by yourself.

### Rename archive file

Finally, you need to change the file name and you code is ready for run. 


## Simple usage with qr-code.py

### Place you data

To generate your qrcode, download and open the 'qr-code.py' archive. 

Next, you need change the data between the quotes:<br>
`img = qrcode.make('place-your-data-here')`

Data can be an url from website, number or other type.

### Rename archive file

Change the file name and you code is ready for run. 
`img.save("file.png")`

## Customized usage with qr-code.py

### Place you data

Firt, change the data between the quotes.
`qr.add_data('place-your-data-here')`

### Customizing color 

You can change the qr code color placing the color name or RGB code.

```
img = qr.make_image(fill_color="black", back_color="white")

img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
```
Choose one and delete (or comment) the other.


You can find more information by clicking [here](https://github.com/lincolnloop/python-qrcode).