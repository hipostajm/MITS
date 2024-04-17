from nbtlib.tag import *
from nbtlib import File
import nbtlib

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
                "size": List[Int]([1, 1, 1]),
            }
        )
    }
)
new_file.save("nbt_files/new_file.nbt")

loaded_file = nbtlib.load("nbt_files/new_file.nbt")
loaded_file.gzipped

print(loaded_file.values())