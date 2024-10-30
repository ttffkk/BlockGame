from BlockWorld import World
from Wall import Wall
from WallWithWindow import WallWithWindow


def b_key_pressed(welten: World):
    x, y, z = welten.player_position()
    y= y-1
    wallis = WallWithWindow(pos=(x, y, z), bw=welten)
    wallis.build()
    wonder = WallWithWindow(pos=(x, y, z), bw=welten)
    wonder.rotated = True
    wonder.build()


welt = World()
welt.build_key_pressed = b_key_pressed
welt.run()
