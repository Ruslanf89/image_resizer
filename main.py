import os, sys
from PIL import Image

def resize_image(input_image, size):


    with Image.open(input_image) as img:
        img = img.convert('RGBA')
        bbox = img.getbbox()
        cropped_img = img.crop(bbox)

        original_width, original_height = cropped_img.size
        aspect_ratio = original_width / original_height

        new_width = int(new_size[0])
        new_height = int(new_width / aspect_ratio)

        resized_img = cropped_img.resize((new_width, new_height), resample=Image.LANCZOS)

        base, ext = os.path.splitext(input_image)
        resized_img.save(base + "_resized" + ext, format='PNG')


input_folder = "Images/Idle/"
new_size = (90, 90)

for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        input_img = os.path.join(input_folder, filename)
        resize_image(input_img, new_size)