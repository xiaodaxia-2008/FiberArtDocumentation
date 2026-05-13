# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pillow",
# ]
# ///

from PIL import Image

img_path = 'docs/user_guides/images/FiberArtParameterSpecification.png'
img = Image.open(img_path)
print(f"Image size: {img.size}")
