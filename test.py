from funcs.avg_collor import avg_collor
from funcs.rgba_of_pixel import rgba_of_pixel
from PIL import Image

img = Image.open('./assets/30x30to10x10.png').convert('RGBA')

print(avg_collor(img, [0,1,2,3,4,5], [0]))
print(rgba_of_pixel(img,1,0))

# for x in range(img.width):
#     for y in range(img.height):
#         print(rgba_of_pixel(img, x , y))