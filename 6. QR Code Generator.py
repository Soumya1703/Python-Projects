import qrcode

# Function to generate a QR code
def generate_qr(data, file_name="qrcode.png"):
    # Create QR code object
    qr = qrcode.QRCode(
        version=1,  # Size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in pixels
        border=4,  # Thickness of the border
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the image file (overwriting the previous one)
    img.save(file_name)
    print(f"QR code saved as {file_name}")

# Ask the user for the input data
data = input("Enter the data or URL to be encoded in the QR code: ")

# Generate and save the QR code (always overwrites the same file)
generate_qr(data)
