from PIL import Image
import json
import math

class NotASquereOfNumber(Exception):
    pass

def rgba_of_pixel(image: Image, x: int, y: int) -> tuple[int, int, int, int]:  # Image needs to be converted with .convert('RGBA')
    r, g, b, a = image.getpixel((x, y))
    return (r, g, b, a)

def avg_color(image: Image, x_range: list[int,int]|tuple[int,int], y_range: list[int,int]|tuple[int,int]) -> list[int,int,int]|bool:
    r_list = []
    g_list = []
    b_list = []

    for y in range(y_range[0], y_range[1]):
        for x in range(x_range[0], x_range[1]):
            rgba = rgba_of_pixel(image, x, y)

            if rgba[3] == 255:
                r_list.append(rgba[0])            
                b_list.append(rgba[1])            
                g_list.append(rgba[2])
            else:
                return False

    return (int(sum(r_list)/len(r_list)),  int(sum(g_list)/len(g_list)), int(sum(b_list)/len(b_list)))     

def down_grade(image: Image, down_grade_scale: int = 1) -> list|bool:
    if not math.sqrt(down_grade_scale).is_integer():
        raise NotASquereOfNumber

    x_dg_scale = int(math.sqrt(down_grade_scale))
    y_dg_scale = int(math.sqrt(down_grade_scale))

    width = image.width
    height = image.height

    new_width = int(width/x_dg_scale)
    new_height = int(height/y_dg_scale)

    collors = []

    for x in range (new_width):
        for y in range(new_height):
            avg = avg_color(image, [x * x_dg_scale, x*x_dg_scale + x_dg_scale], [y * y_dg_scale, y*y_dg_scale + y_dg_scale])
            if avg:
                collors.append(
                    avg
                )
            else:
                return False

    return collors

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