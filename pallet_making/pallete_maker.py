import sys

sys.path.insert(1, './func')

from PIL import Image
from avg_color import avg_color
from rgb_of_pixel import rgb_of_pixel
import json
import os

path = './pallet_making/versions/'
list_of_versions = os.listdir(path)

for version in list_of_versions:
    version_path = f'./pallet_making/versions/{version}/textures'
    list_of_files = os.listdir(version_path)

    colors_dict = {}

    for image in list_of_files:
        if image.split('.')[-1] == 'png':
            img = Image.open(f'{version_path}/{image}').convert('RGB')
            if img.width == 16 and img.height == 16:
                collors = []

                for x in range(img.width):
                    for y in range(img.height):
                        collors.append(rgb_of_pixel(img, x, y))

                colors_dict[image.split('.')[0]] = avg_color([collors])[0]

    with open(f'./pallet_making/versions/{version}/avg_collors.json','w') as output:
        json.dump(colors_dict, output)