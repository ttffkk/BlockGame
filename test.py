from pyblockworld import World



def b_key_pressed(world: World):
  x, y, z = world.player_position()
  world.setBlock(x, y, z, "default:brick")
  world.setBlocks(x,y,z,x+3, y, z, "default:brick")
  world.setBlocks(x,y,z,x, y+4, z, "default:grass")
  world.setBlocks(x,y,z,x, y, z+5, "default:stone")



world = World()
world.build_key_pressed = b_key_pressed
world.run()
