import Entity
import pygame


class PeacefulEntity(Entity.Entity):

    def __init__(self, entityID, hitboxHeight, hitboxWidth, xCor, yCor, health):
        super().__init__(entityID, hitboxHeight, hitboxWidth, xCor, yCor, health)

    def retaliate(self):
        pass

    def graze(self):
        pass


class Mammoth(PeacefulEntity):
    entityTexturePath = "assets/Mammoth.png"
    entityTexture = pygame.image.load(entityTexturePath)
    hitboxHeight = entityTexture.get_height()
    hitboxWidth = entityTexture.get_width()
    health = 4

    def __init__(self, entityID, xCor, yCor):
        super().__init__(entityID, self.hitboxHeight, self.hitboxWidth, xCor, yCor, self.health)

    def render(self, win):
        win.blit(Mammoth.entityTexture, (self.xCor, self.yCor))
        win.blit(Entity.Entity.healthTexture[self.health], (self.xCor, self.yCor + 60))
