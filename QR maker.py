import qrcode


linkedin_url = input("https://www.linkedin.com/in/User_Name/")

qr = qrcode.make(linkedin_url)
qr.save("linkedin_qr.png")

print("QR Code created!")
