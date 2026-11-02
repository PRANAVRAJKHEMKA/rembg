
from rembg import remove
from PIL import Image

input_path = "input/photo.png"
output_path = "output/transparent.png"

print("Loading image...")

with Image.open(input_path) as image:
    result = remove(image)
    result.save(output_path)

print("Background removed successfully!")
print("Saved to:", output_path)
