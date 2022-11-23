from Entity import *
class Player(Entity):
    
    imageFile = "asstes/player.png"
    temperature = 0
    hunger = 0
    thirst = 0
    freezing = False
    overheating = False

    def __init__(self, entityID, hitbox, coords, health):
        super.__init__(super, entityID, hitbox, coords, health)

    def keyInput():
        pass

    def weather():
        pass
