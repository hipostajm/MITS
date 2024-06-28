import sys

sys.path.insert(1, './')

from funcs.avg_color import avg_color
from PIL import Image
import os
import json

versions = os.listdir('./palett/blocks')

for version in versions:
    blocks_path = f'./palett/blocks/{version}/textures'
    blocks = os.listdir(blocks_path)

    colors = {}

    for block in blocks:
        block_splitted = block.split('.')
        if block_splitted[-1] == 'png' and 'top' not in block_splitted[0].split('_') and 'bottom' not in block_splitted[0].split('_') and 'side' not in block_splitted[0].split('_') and 'side1' not in block_splitted[0].split('_') and 'front' not in block_splitted[0].split('_') and 'side0' not in block_splitted[0].split('_') and 'side2' not in block_splitted[0].split('_') and 'side3' not in block_splitted[0].split('_') and 'side4' not in block_splitted[0].split('_'):
            img = Image.open(f'{blocks_path}/{block}').convert('RGBA')
            if img.width == img.height:
                result = avg_color(img,[0, img.width], [0, img.height])
                
                if result:
                    colors[block.split('.')[0]] = result

    with open(f"./palett/blocks/{version}/colors.json", "w") as file: 
        json.dump(colors, file)