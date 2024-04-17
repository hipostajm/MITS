from PIL import Image, ImageDraw
import math

down_grade_size = 4
img = "test.png"

size = Image.open(img).size
new_size = (int(size[0]/math.sqrt(down_grade_size)),int(size[1]/math.sqrt(down_grade_size)))

new_imige = Image.new(mode='RGB', size=(size[0],size[1]), color='orange')

pixels_new = new_imige.load()

print(new_size)


def rgb_of_pixel(img_path: str, x: int, y: int):
    im = Image.open(img_path).convert('RGB')
    r, g, b = im.getpixel((x, y))
    a = (r, g, b)
    return a

for x in range(size[0]):
    for y in range(size[1]):
        a = rgb_of_pixel(img,x,y)
        # print(f'x: {x}, y: {y}, rgb: {rgb_of_pixel(img,x,y)}')
        pixels_new[x,y] = a[0],a[1],a[2]

new_imige.save('t.png')