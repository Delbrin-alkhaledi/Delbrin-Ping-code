import qrcode
img = qrcode.make("https://www.getacademy.no/")
img.save("new.png")