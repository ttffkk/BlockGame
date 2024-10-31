from pyblockworld import World
from Wall import Wall


class WallWithWindow(Wall):

    def __init__(self, pos: tuple, bw: World):
        super().__init__(pos, bw)
        self.window_material_id = "air"

    def build(self):

        x, y, z = self.pos
        super().build()
        if self.rotated:
            self.bw.setBlocks(x + 3, y + 1, z, x + 2, y + 3, z, self.window_material_id)
        else:
            self.bw.setBlocks(x, y + 1, z + 3, x, y + 3, z + 2, self.window_material_id)
