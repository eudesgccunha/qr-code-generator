# QR code generator with python

The 'qr-code.py' archive was forked of [lincolnloop repository](https://github.com/lincolnloop/python-qrcode). 
On the other hand, the 'qrcode.py' was made from previous testing on qrcode library.

## Simple usage

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
