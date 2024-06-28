from PIL import Image
from funcs.used_blocks import used_blocks

print(used_blocks(Image.open('./assets/6.jpg').convert('RGBA'),'1.20.4'))

