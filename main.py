import os, sys
from PIL import Image

def resize_image(input_image, output_image, size):


    with Image.open(input_image) as img:
        img = img.convert('RGBA')
        bbox = img.getbbox()
        cropped_img = img.crop(bbox)

        original_width, original_height = cropped_img.size
        aspect_ratio = original_width / original_height

        new_width = int(new_size[0])
        new_height = int(new_width / aspect_ratio)

        resized_img = cropped_img.resize((new_width, new_height), resample=Image.LANCZOS)

        resized_img.save(output_image, format='PNG')


input_img = "C:/Users/Dypko/resizer_v01/Images/Idle/0_Dark_Elves_Idle_000.png"
output_img = "C:/Users/Dypko/resizer_v01/Images/Idle/1.png"
new_size = (75, 75)

resize_image(input_img, output_img, new_size)