from pyblockworld import World

from Wall import Wall
from Roof import Roof


class House:

    def __init__(self, pos: tuple, bw: World):

        self.wallFront: Wall
        self.wallBack: Wall
        self.wallLeft: Wall
        self.wallRight: Wall
        self.roof: Roof
        self.pos = pos
        self.bw = bw

    def build(self):

        if self.pos is None:
            raise ValueError("Wall position (x, y, z) is not set.")
        if self.bw is None:
            raise ValueError("Wall is not associated with a PyBlockWorld instance.")

        x, y, z = self.pos

        if self.rotated:
            self.bw.setBlocks(x, y, z, x + self.width - 1, y + self.height, z, self.material_id)
        else:
            self.bw.setBlocks(x, y, z, x, y + self.height, z + self.width - 1, self.material_id)

    def change_wall_material(new_material_id:str):
        print
