import json
import random
import math
import nbtlib
from PIL import Image
from funcs.avg_color import avg_color
from funcs.down_grade import down_grade
from funcs.rgba_of_pixel import rgba_of_pixel

path = './assets/t.png'
version = '1.20.4'
down_grade_scale = 1

palette_blocks = ['']

nbt = nbtlib.parse_nbt("""
{
    size           
                       
                       
                       

                       
}
""")