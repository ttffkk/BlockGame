from pyblockworld import World


class Roof:

    def __init__(self, pos: tuple, bw: World):

        self.width = 6
        self.height = 5
        self.rotated = False
        self.pos = pos
        self.material_id = "default:stone"
        self._bw = bw

    def build(self):

        if self.pos is None:
            raise ValueError("Wall position (x, y, z) is not set.")
        if self._bw is None:
            raise ValueError("Wall is not associated with a PyBlockWorld instance.")

        x, y, z = self.pos
