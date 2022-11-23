from GUI import *
from Entity import *


gui = GUI
gui.__init__(gui)

player = Entity
hitbox = [20, 20]
coords = [0,0]
player.__init__(player, 1, hitbox, coords, 10)

print(player.health)

