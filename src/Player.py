from Entity import *
import pygame


class Player(Entity):
    
    entityImageFile = "assets/player.png"
    temperature = 36.0
    hunger = 100
    thirst = 100
    freezing = False
    overheating = False
    playerImage = pygame.image.load(entityImageFile)
    mapXCor = 50
    mapYCor = 50
    inBlockXCor = 1
    inBlockYCor = 1

    def __init__(self, win):
        super().__init__(1, self.playerImage.get_width(), self.playerImage.get_height(), win.get_width()/2-self.playerImage.get_width()/2, win.get_height()/2-self.playerImage.get_height()/2, 4)

    def render(self, win):
        win.blit(self.playerImage, (self.xCor, self.yCor))

    def dropItem(self):
        pass
