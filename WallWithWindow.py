from pyblockworld import World
from Wall import Wall


class WallWithWindow(Wall):

    def __init__(self, pos: tuple, bw: World):

        self.width = 6
        self.height = 5
        self.rotated = False
        self.pos = pos
        self.material_id = "default:stone"
        self.window_material_id = "air"
        self.bw = bw

    def build(self):

        if self.pos is None:
            raise ValueError("Wall position (x, y, z) is not set.")
        if self.bw is None:
            raise ValueError("Wall is not associated with a PyBlockWorld instance.")

        x, y, z = self.pos

        if self.rotated:
                self.bw.setBlocks(x,y,z,x+self.width-1,y+self.height,z,self.material_id)
                self.bw.setBlocks(x+3,y+1,z,x+2,y+3,z,self.window_material_id)
        else:
                self.bw.setBlocks(x,y,z,x,y+self.height,z+self.width-1,self.material_id)
                self.bw.setBlocks(x,y+1,z+3,x,y+3,z+2,self.window_material_id)
