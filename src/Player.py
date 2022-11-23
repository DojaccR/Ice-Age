from Entity import *
class Player(Entity):
    
    entityImageFile = "assets/player.png"
    temperature = 0
    hunger = 0
    thirst = 0
    freezing = False
    overheating = False

    def __init__(self, entityID, hitboxHeight, hitboxWidth, xCor, yCor, health):
        super().__init__(entityID, hitboxHeight, hitboxWidth, xCor, yCor, health)
