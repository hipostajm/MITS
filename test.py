from nbt import nbt
nbtfile = nbt.NBTFile("bigtest.nbt",'rb')
nbtfile["listTest (compound)"].tags[0]["name"].value = "Different name"
nbtfile.write_file("newnbtfile.nbt")