from BlockWorld import World

from House import House


def b_key_pressed(welten: World):
    hause=House (welten.player_position(),welten)
    hause.build()



welt = World()
welt.build_key_pressed = b_key_pressed
welt.run()
