from pyblockworld import World

from House import House
import unittest


class HouseTest(unittest.TestCase):

    def setUp(self):
        self.bw = World()
        self.p = House(self.bw.player_position(), self.bw)


    def test_change_wall_material(self):
        vorher = [self.p.wallFront.material_id, self.p.wallBack.material_id, self.p.wallLeft.material_id,
                  self.p.wallRight.material_id]
        self.p.change_wall_material("default:brick")

        nachher = [self.p.wallFront.material_id, self.p.wallBack.material_id, self.p.wallLeft.material_id,
                   self.p.wallRight.material_id]

        self.assertFalse(all(a == b for a, b in zip(vorher, nachher)))
