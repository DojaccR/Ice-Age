from Entity import *
from math import *

class HostileEntity(Entity):
    damage = 0

    def __init__(self, entityID, hitboxHeight, hitboxWidth, xCor, yCor, health, damage):
        super().__init__(entityID, hitboxHeight, hitboxWidth, xCor, yCor, health)
        self.damage = damage
    
    def attack():
        pass

    def target(self, Player, event):
        if int(sqrt((self.xCor-Player.xCor)^2+(self.yCor-Player.yCor)^2)) < 100:
            print("attack, distance is " + str(sqrt((self.xCor-Player.xCor)^2+(self.yCor-Player.yCor)^2)))
    
class DireWolf(HostileEntity):
    entityImageFile = "assets/Wolf.png"
    hitboxHeight = 50
    hitboxWidth = 100
    health = 4
    damage = 1

    def __init__(self, entityID, xCor, yCor):
        super().__init__(entityID, 50, 100, xCor, yCor, 4, 1)
    
