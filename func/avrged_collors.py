from PIL import Image
from rgb_of_pixel import rgb_of_pixel
import math

filepath = "./assets/30x30to10x10.png"
downgrade_scale_for_test = 9


def avrged_collors(
    path_to_file: str,
    downgrade_scale: int,
) -> list[tuple[float | int, float | int, float | int]]:

    img = Image.open(path_to_file).convert("RGB")

    img_width = img.width
    img_height = img.height

    downgrade_scale_x = int(math.sqrt(downgrade_scale))
    downgrade_scale_y = int(math.sqrt(downgrade_scale))

    new_width = int(img_width / int(math.sqrt(downgrade_scale)))
    new_height = int(img_height / int(math.sqrt(downgrade_scale)))

    for x in range(new_width):
        for y in range(new_height):
            collors = []
            print(x * downgrade_scale_x)
            print(y * downgrade_scale_y)
            for x_additiv in range(downgrade_scale_x):
                for y_additiv in range(downgrade_scale_y):
                    collors.append(
                        rgb_of_pixel(
                            img,
                            x * downgrade_scale_x + x_additiv,
                            y * downgrade_scale_y + y_additiv,
                        )
                    )
            print(collors)


avrged_collors(filepath, downgrade_scale_for_test)
