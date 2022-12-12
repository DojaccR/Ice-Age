from Entity import *
import pygame


class Player(Entity):
    
    entityImageFile = "assets/player.png"
    temperature = 0
    hunger = 0
    thirst = 0
    freezing = False
    overheating = False
    playerImage = pygame.image.load(entityImageFile)
    mapXCor = 50
    mapYCor = 50
    inBlockXCor = 1
    inBlockYCor = 1

    def __init__(self, win):
        super().__init__(1, 100, 100, win.get_width()/2, win.get_height()/2, 4)

    def render(self, win):
        win.blit(self.playerImage, (self.xCor, self.yCor))

    def pickup(self, itemList, inventory):
        pass
