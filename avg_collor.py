from PIL import Image, ImageDraw
import math


class NotASquereOfNumber(Exception):
    pass


down_grade_size = 9

if not math.sqrt(down_grade_size.is_integer()):
    raise NotASquereOfNumber

img = "Woah.png"
size = Image.open(img).size
new_size = (
    int(size[0] / math.sqrt(down_grade_size)),
    int(size[1] / math.sqrt(down_grade_size)),
)

new_imige = Image.new(mode="RGB", size=(new_size[0], new_size[1]), color="orange")

pixels_new = new_imige.load()

print(new_size)


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

    print(r_avg, g_avg, b_avg)

    return (r_avg, g_avg, b_avg)


avg_collors = []

for x in range(new_size[0]):
    for y in range(new_size[1]):

        x_list = []
        y_list = []
        comperd = []

        for i in range(int(math.sqrt(down_grade_size))):
            x_list.append(x * math.sqrt(down_grade_size) + i)
            y_list.append(y * math.sqrt(down_grade_size) + i)

        for x_comperd in x_list:
            for y_compard in y_list:
                comperd.append((x_comperd, y_compard))

        avg_color = avriging_pixeles(comperd, img)
        avg_collors.append((avg_color, x, y))

for value in avg_collors:
    pixels_new[value[1], value[2]] = value[0]


new_imige.save("t.png")
