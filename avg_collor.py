from PIL import Image, ImageDraw
import math

down_grade_size = 4
img = "test.png"

size = Image.open(img).size
new_size = (
    int(size[0] / math.sqrt(down_grade_size)),
    int(size[1] / math.sqrt(down_grade_size)),
)

new_imige = Image.new(mode="RGB", size=(size[0], size[1]), color="orange")

pixels_new = new_imige.load()

print(new_size)


def rgb_of_pixel(img_path: str, x: int, y: int):
    im = Image.open(img_path).convert("RGB")
    r, g, b = im.getpixel((x, y))
    a = (r, g, b)
    return a


# for x in range(size[0]):
#     for y in range(size[1]):
#         if x % math.sqrt(down_grade_size) == 0 and y % math.sqrt(down_grade_size) == 0:
#             r_list = []
#             g_list = []
#             b_list = []
#             for new_x in range(int(math.sqrt(down_grade_size) - 1)):
#                 for new_y in range(int(math.sqrt(down_grade_size) - 1)):
#                     r_list.append(rgb_of_pixel(img, new_x, new_y)[0])
#                     g_list.append(rgb_of_pixel(img, new_x, new_y)[1])
#                     b_list.append(rgb_of_pixel(img, new_x, new_y)[2])

#             r =

for x in range(new_size[0]):
    for y in range(new_size[1]):
        print("x: ", x * math.sqrt(down_grade_size), x * math.sqrt(down_grade_size) + 1)
        print("y: ", y * math.sqrt(down_grade_size), y * math.sqrt(down_grade_size) + 1)


new_imige.save("t.png")
