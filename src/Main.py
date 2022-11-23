from GUI import *
from Entity import *
from Player import *


gui = GameScreen
gui.__init__(gui)

player = Player
player.__init__(player, 1, [20, 20], [0, 0], 10)

gui.initPlayer()



