import Entity
import pygame
import Map


class Player(Entity.Entity):
    
    entityTexturePath = "assets/player.png"
    playerTexture = pygame.image.load(entityTexturePath)
    temperature = 36.0
    hunger = 100
    thirst = 100
    freezing = False
    overheating = False
    # could not get numbers from Map class, I have no idea why. If can be fixed please do.
    mapXCor = 500
    mapYCor = 500
    inBlockXCor = 1
    inBlockYCor = 1

    def __init__(self, win):
        super().__init__(1, self.playerTexture.get_width(), self.playerTexture.get_height(), win.get_width()/2-self.playerTexture.get_width()/2, win.get_height()/2-self.playerTexture.get_height()/2, 4)

    def render(self, win):
        win.blit(self.playerTexture, (self.xCor, self.yCor))

    def dropItem(self):
        pass
