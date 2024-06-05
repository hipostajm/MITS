from PIL import Image
from func.rgb_of_pixel import rgb_of_pixel
from func.avg_color import avg_color
import math


class notASquereOfNumber(Exception):
    pass


def down_grading_photo(
    path_to_file: str,
    downgrade_scale: int = 1,
) -> list[tuple[float | int, float | int, float | int]]:

    if not math.sqrt(downgrade_scale).is_integer():
        raise notASquereOfNumber

    img = Image.open(path_to_file).convert("RGB")

    img_width = img.width
    img_height = img.height

    downgrade_scale_x = int(math.sqrt(downgrade_scale))
    downgrade_scale_y = int(math.sqrt(downgrade_scale))

    new_width = int(img_width / int(math.sqrt(downgrade_scale)))
    new_height = int(img_height / int(math.sqrt(downgrade_scale)))

    collors = []

    for x in range(new_width):
        for y in range(new_height):
            collors_block = []
            for x_additiv in range(downgrade_scale_x):
                for y_additiv in range(downgrade_scale_y):
                    collors_block.append(
                        rgb_of_pixel(
                            img,
                            x * downgrade_scale_x + x_additiv,
                            y * downgrade_scale_y + y_additiv,
                        )
                    )
            collors.append(collors_block)

    return avg_color(collors)
