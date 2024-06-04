from nbtlib.tag import Compound, List, String, Int
from PIL import Image
from nbtlib import File, load
from func.down_grading_photo import down_grading_photo

path = './assets/t.png'

img = Image.open(path)
collors = down_grading_photo(path, 4)

new_file = File(
    {
        "w": Compound(
            {
                "blocks": List[Compound](
                    [Compound({"pos": List[Int]([0, 0, 0]), "state": Int(0)})]
                ),
                "palette": List[Compound](
                    [Compound({"Name": String("minecraft:cobblestone")})]
                ),
                "size": List[Int]([img.width, img.height, 1]),
            }
        )
    }
)
new_file.save("nbt_files/new_file.nbt")

loaded_file = load("nbt_files/new_file.nbt")
loaded_file.gzipped 

print(loaded_file.values())