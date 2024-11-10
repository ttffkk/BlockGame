from pyblockworld import World

from Wall import Wall
from Roof import Roof
from WallWithDoor import WallWithDoor
from WallWithWindow import WallWithWindow

class House:

    def __init__(self, pos: tuple, bw: World):

        self.wallFront: Wall
        self.wallBack: Wall
        self.wallLeft: Wall
        self.wallRight: Wall
        self.roof: Roof
        self.pos = pos
        self.__bw = bw

    def build(self):

        if self.pos is None:
            raise ValueError("Wall position (x, y, z) is not set.")
        if self.__bw is None:
            raise ValueError("Wall is not associated with a PyBlockWorld instance.")

        x, y, z = self.pos
        self.wallFront = Wall((x + 2, y - 1, z - 3), self.__bw)
        self.wallFront.build()
        self.wallBack = WallWithWindow((x - 3, y - 1, z + 3), self.__bw)
        self.wallBack.rotated = True
        self.wallBack.build()
        self.wallLeft = WallWithDoor((x - 3, y - 1, z - 3), self.__bw)
        self.wallLeft.build()
        self.wallRight = WallWithWindow((x - 3, y - 1, z - 3), self.__bw)
        self.wallRight.rotated = True
        self.wallRight.build()
        self.roof = Roof((x -3, y+self.wallFront.height , z -3), self.__bw)
        self.roof.build()


    def change_wall_material(self, new_material_id: str):
        self.wallFront.material = new_material_id
        self.wallBack.material = new_material_id
        self.wallLeft.material = new_material_id
        self.wallRight.material = new_material_id
        self.roof = new_material_id
