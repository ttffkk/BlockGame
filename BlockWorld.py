from pyblockworld import World


def set_block(x, y, z, block):
    World.setBlock(World, x, y, z, block)


def set_blocks(x1, y1, z1, x2, y2, z2, blocks):
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            for z in range(min(z1, z2), max(z1, z2) + 1):
                World.setBlock(x, y, z, blocks)



def player_position():
    return World.player_position(World, False)
