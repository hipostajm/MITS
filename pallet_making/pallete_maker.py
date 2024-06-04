import sys

sys.path.insert(1, './func')

from PIL import Image
from avg_color import avg_color
from rgb_of_pixel import rgb_of_pixel
import json
import os

path = './pallet_making/versions/1.20.4/textures'
list_of_files = os.listdir(path)

colors_dict = {}

for image in list_of_files:
    if image.split('.')[-1] == 'png':
        img = Image.open(f'{path}/{image}').convert('RGB')
        if img.width == 16 and img.height == 16:
            collors = []

            for x in range(img.width):
                for y in range(img.height):
                    collors.append(rgb_of_pixel(img, x, y))

            colors_dict[image] = avg_color([collors])


print(colors_dict)