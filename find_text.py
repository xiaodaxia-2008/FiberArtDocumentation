# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pillow",
#     "pytesseract",
# ]
# ///
import pytesseract
from PIL import Image

try:
    img = Image.open('docs/user_guides/images/FiberArtParameterSpecification.png')
    data = pytesseract.image_to_data(img, lang='chi_sim', output_type=pytesseract.Output.DICT)
    for i in range(len(data['text'])):
        text = data['text'][i].strip()
        if text:
            print(f"Found: '{text}' at ({data['left'][i]}, {data['top'][i]}) w={data['width'][i]} h={data['height'][i]}")
except Exception as e:
    print("Error:", e)
