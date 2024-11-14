from pyblockworld import World
from Wall import Wall


class WallWithDoor(Wall):

    def __init__(self, pos: tuple, bw: World):
        super().__init__(pos, bw)
        self.door_material_id = "air"

    def build(self):

        x, y, z = self.pos
        super().build()
        if self.rotated:
            self._bw.setBlocks(x + 3, y, z, x + 2, y + 3, z, self.door_material_id)
        else:
            self._bw.setBlocks(x, y, z + 3, x, y + 3, z + 2, self.door_material_id)
