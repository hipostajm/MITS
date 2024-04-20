from PIL import Image, ImageDraw
import math
import threading


class NotASquereOfNumber(Exception):
    pass


down_grade_size = 36
if not math.sqrt(down_grade_size).is_integer():
    raise NotASquereOfNumber

img = "w.png"
size = Image.open(img).size
new_size = (
    int(size[0] / math.sqrt(down_grade_size)),
    int(size[1] / math.sqrt(down_grade_size)),
)
new_imige = Image.new(mode="RGB", size=(new_size[0], new_size[1]), color="orange")
pixels_new = new_imige.load()
threads = 100


def rgb_of_pixel(img_path: str, x: int, y: int):
    im = Image.open(img_path).convert("RGB")
    r, g, b = im.getpixel((x, y))
    a = (r, g, b)
    return a


def avriging_pixeles(cords_of_pixels: list, imige: str):

    r_list = []
    g_list = []
    b_list = []

    r_sum = 0
    g_sum = 0
    b_sum = 0

    for cords in cords_of_pixels:
        a = rgb_of_pixel(imige, cords[0], cords[1])
        r_list.append(a[0])
        g_list.append(a[1])
        b_list.append(a[2])

    for r in r_list:
        r_sum += r

    for g in g_list:
        g_sum += g

    for b in b_list:
        b_sum += b

    r_avg = round(r_sum / len(r_list))
    g_avg = round(g_sum / len(g_list))
    b_avg = round(b_sum / len(b_list))

    return (r_avg, g_avg, b_avg)


avg_collors = []

def getting_color(x_range: int,y_range: int,down_grading_size: int):
    for x in range(x_range):
        for y in range(y_range):

            x_list = []
            y_list = []
            comperd = []

            for i in range(int(math.sqrt(down_grading_size))):
                x_list.append(x * math.sqrt(down_grading_size) + i)
                y_list.append(y * math.sqrt(down_grading_size) + i)

            for x_comperd in x_list:
                for y_compard in y_list:
                    comperd.append((x_comperd, y_compard))

            avg_color = avriging_pixeles(comperd, img)
            avg_collors.append((avg_color, x, y))

# for thread in range(threads):
    
#     x_blocks = math.ceil(size[0]/down_grade_size)
#     y_blocks = math.ceil(size[1]/down_grade_size)
#     num_of_blocks = x_blocks*y_blocks
#     block_per_thread = math.ceil(num_of_blocks/threads)

#     list_of_blocks = []

#     if size[0] < num_of_blocks*down_grade_size:


getting_color(new_size[0],new_size[1],down_grade_size)


for value in avg_collors:
    pixels_new[value[1], value[2]] = value[0]

new_imige.save("t.png")
