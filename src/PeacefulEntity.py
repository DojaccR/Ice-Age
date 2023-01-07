import Entity
import pygame

class PeacefulEntity(Entity.Entity):

    def __init__(self, entityID, hitboxHeight, hitboxWidth, xCor, yCor, health):
        super().__init__(entityID, hitboxHeight, hitboxWidth, xCor, yCor, health)


class Mammoth(PeacefulEntity):
    entityTexturePath = "assets/Mammoth.png"
    entityTexture = pygame.image.load(entityTexturePath)
    hitboxHeight = entityTexture.get_height()
    hitboxWidth = entityTexture.get_width()
    health = 4
    def __init__(self, entityID, xCor, yCor):
        super().__init__(entityID, self.hitboxHeight, self.hitboxWidth, xCor, yCor, self.health)
