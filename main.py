import qrcode

print("Welcom to QR Code Generator!")
text = input("Enter your text here: ")

img = qrcode.make(text)

img.save('hello.png')