import os
from PIL import Image

def generate_image(dest_path, width, height, count):
    img = Image.new('RGB', (width, height), "black")     
    pixels = img.load()

    for x in range(width):
        for y in range(height):
            # Example: Create a simple gradient
            # Red component increases with x, Green with y
            r = int((x / width) * 255)
            g = int((y / height) * 255)
            b = int((y / height) * 255)

            pixels[x, y] = (r, g, b)

            file_string = "generated_image_" + str(count) + ".png"
            os.path.join(dest_path, file_string)
            img.save(file_string, format="PNG")

