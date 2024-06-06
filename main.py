from nbtlib import parse_nbt, File
from PIL import Image
from func.down_grading_photo import down_grading_photo
import math
import json

#TODO: Ogarnąć generowanie NBT i tyle

path = "./assets/t.png"
version = '1.20.2'
down_grade_scale = 1

img = Image.open(path)
collors = down_grading_photo(path, down_grade_scale)

blocks = ''

json.load(f'./pallet_making/versions/{version}/avg_collors.json')

main_nbt = f">w:>size: [{img.width/math.sqrt(down_grade_scale)},{img.height/math.sqrt(down_grade_scale)},1],blocks: [{blocks}],"""

nbt = parse_nbt("""
{
w:{
  size: [69,74,1],
  blocks: [
    {
    pos: [0,0,0]
    ,tate: 0
    },
    {
      pos: [1, 0, 0],
      state: 1
    }
  ],
  palette: [
    {Name: "minecraft:cobblestone"},
    {Name: "minecraft:dirt"}
  ]
}
}
""")

File(nbt).save('test2.nbt')