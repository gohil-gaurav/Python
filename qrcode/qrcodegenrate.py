import qrcode
import image

qr = qrcode.QRCode(
    version= 15,
    box_size=10,
    border=5
)

data = str(input("Enter a link: "))

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", black_color = "white")
img.save("test.png")