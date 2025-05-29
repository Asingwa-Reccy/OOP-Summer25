import qrcode
from PIL import Image

# URL you want to encode
url = "https://reccy-kenya-creates.lovable.app/"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction
    box_size=10,  # size of each box in pixels
    border=4,  # thickness of the border (minimum is 4)
)

# Add data to the QR code
qr.add_data(url)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("reccy_qr_code.png")

# Optional: Show the image
img.show()
