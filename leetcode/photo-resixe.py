from PIL import Image, ImageDraw

# Load your image (rename it to input.jpg)
img = Image.open("Path\YourPhoto.jpg")

# Convert sizes
dpi = 300

# 35x45 mm in pixels
w1 = int(35/25.4 * dpi)
h1 = int(45/25.4 * dpi)

# 2x2 inch in pixels
w2 = int(2 * dpi)
h2 = int(2 * dpi)

# Resize copies
photo_35x45 = img.resize((w1, h1))
photo_2x2 = img.resize((w2, h2))

# A4 canvas
A4 = (2480, 3508)
sheet = Image.new("RGB", A4, "white")

draw = ImageDraw.Draw(sheet)

# Paste 35x45 mm photo
sheet.paste(photo_35x45, (200, 200))

# Paste 3 copies of 2x2
sheet.paste(photo_2x2, (200, 900))
sheet.paste(photo_2x2, (900, 900))
sheet.paste(photo_2x2, (1600, 900))

# Save PDF
sheet.save("photo_sheet.pdf", "PDF", resolution=300)

print("Done! Your file is saved as photo_sheet.pdf")
