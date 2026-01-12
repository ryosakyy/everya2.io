import qrcode

# URL target (Placeholder or local)
# In a real scenario, this would be the hosted URL.
url = "https://everyamarket.com/20-discount"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="#ff85a2", back_color="white")
img.save("qr_code.png")
print("QR Code generated as qr_code.png")
