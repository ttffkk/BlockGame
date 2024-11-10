from pyblockworld import World


class Roof:

    def __init__(self, pos: tuple, bw: World):

        self.width = 6
        self.depth = 6
        self.rotated = False
        self.pos = pos
        self.roof_material_id = "default:stone"
        self.__bw = bw

    def build(self):

        if self.pos is None:
            raise ValueError("Wall position (x, y, z) is not set.")
        if self.__bw is None:
            raise ValueError("Wall is not associated with a PyBlockWorld instance.")

        x, y, z = self.pos

        self.__bw.setBlocks(x, y, z, x + self.width - 1, y , z+self.depth, self.roof_material_id)
