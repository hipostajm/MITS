from PIL import Image
from funcs.down_grade import down_grade

img = Image.open('./assets/30x30to10x10.png').convert('RGBA')

print(down_grade(img, 9))