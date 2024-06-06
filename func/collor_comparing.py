from PIL import Image
from down_grading_photo import down_grading_photo
from in_used_collors import in_used_collors
import json
import math

def collor_comparing(game_version: str, path: str, downgrade_scale) -> dict:
    f = open(f'./pallet_making/versions/{game_version}/avg_collors.json')

    block_collors: dict = json.load(f)
    downgrade_scale_rooted = math.sqrt(downgrade_scale)
    collors = down_grading_photo(path, downgrade_scale)
    img = Image.open(path).convert('RGB')

    used_collors = {}

    for color in collors:
        if not in_used_collors(used_collors, color):
            posible_collors = {}
            minimal_length = math.inf
            used_block = ''

            for name_of_block in block_collors:
                x_len = abs(color[0] - block_collors[name_of_block][0])
                y_len = abs(color[1] - block_collors[name_of_block][1])
                z_len = abs(color[2] - block_collors[name_of_block][2])
                
                xy_diagonal = math.sqrt(x_len**2+y_len**2)

                length = math.sqrt(xy_diagonal**2+z_len**2)

                posible_collors[name_of_block] = length
            
            for name_of_block in posible_collors:
                if posible_collors[name_of_block] < minimal_length:
                    minimal_length = posible_collors[name_of_block]
                    used_block = name_of_block
            
            used_collors[used_block] = color
        
    return used_collors
