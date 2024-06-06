from nbtlib import parse_nbt, File

a = parse_nbt("""
{
w:{
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
  ],
  size: [69,74,1]
}
}
""")

File(a).save('test2.nbt')