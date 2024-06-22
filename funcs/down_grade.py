from PIL import Image
from funcs.rgba_of_pixel import rgba_of_pixel
from funcs.avg_color import avg_color
import math


class NotASquereOfNumber(Exception):
    pass

def down_grade(image: Image, down_grade_scale: int = 1) -> list:
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
            collors.append(
                avg_color(image, [x * x_dg_scale, x*x_dg_scale + x_dg_scale], [y * y_dg_scale, y*y_dg_scale + y_dg_scale])
            )

    return collors


