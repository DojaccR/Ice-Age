from Entity import *
import pygame


class Player(Entity):
    
    entityTexturePath = "assets/player.png"
    playerTexture = pygame.image.load(entityTexturePath)
    temperature = 36.0
    hunger = 100
    thirst = 100
    freezing = False
    overheating = False
    mapXCor = 50
    mapYCor = 50
    inBlockXCor = 1
    inBlockYCor = 1

    def __init__(self, win):
        super().__init__(1, self.playerTexture.get_width(), self.playerTexture.get_height(), win.get_width()/2-self.playerTexture.get_width()/2, win.get_height()/2-self.playerTexture.get_height()/2, 4)

    def render(self, win):
        win.blit(self.playerTexture, (self.xCor, self.yCor))

    def dropItem(self):
        pass
