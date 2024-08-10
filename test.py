from PIL import Image
from funcs import used_blocks
import python_nbt.nbt as nbt
import json

file = nbt.read_from_nbt_file("./schemats/woah.nbt")
json_file = nbt.NBTTagBase.json_obj(self=file, full_json=True)

with open("your_json_file.json", "w") as fp:
    json.dump(json_file , fp) 