from BlockWorld import World
from Wall import Wall
from WallWithWindow import WallWithWindow
from WallWithDoor import WallWithDoor
from House import House


def b_key_pressed(welten: World):
    x, y, z = welten.player_position()
    y= y-1
    huse=House (welten.player_position(),welten)
    huse.build()



welt = World()
welt.build_key_pressed = b_key_pressed
welt.run()
