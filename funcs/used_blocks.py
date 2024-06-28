import math
import json
from PIL import Image
from funcs.down_grade import down_grade

def used_blocks(img: Image, version: str, down_grade_scale: int = 1) -> tuple[list, list]:
    colors = down_grade(img, down_grade_scale)

    with open(f'./palett/blocks/{version}/colors.json') as file:
        version_blocks = json.load(file)

    used_colors = {}

    for color in colors:
        if color not in used_colors:
            used_block = ''
            min_distance = math.inf

            for block in version_blocks:
                r_c = color[0]
                g_c = color[1]
                b_c = color[2]
                
                r_b = version_blocks[block][0]
                g_b = version_blocks[block][0]
                b_b = version_blocks[block][0]

                r_dif = abs(r_c - r_b)
                g_dif = abs(g_c - g_b)
                b_dif = abs(b_c - b_b)

                distance = math.sqrt(r_dif**2+g_dif**2+b_dif**2)

                min_distance = min(distance, min_distance)

                if min_distance == distance:
                    used_block = block

            used_colors[color] = used_block


        
    return used_colors