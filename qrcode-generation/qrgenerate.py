import qrcode

# The URL you want to encode
url = "https://github.com/WoongheeLee/woongheelee.github.io/blob/master/downloads/AI%20Research%20Performance%20Comparison_%20ChatGPT%2C%20Gemini%2C%20Claude%2C%20and%20Perplexity%20(2024-2025).pdf"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image file
img.save("qrcode.png")
