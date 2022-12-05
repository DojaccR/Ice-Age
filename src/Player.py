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

    def __init__(self):
        super().__init__(1, 100, 100, 200, 200, 4)

    def render(self, win):
        win.blit(self.playerImage, (self.xCor, self.yCor))
        win.blit(pygame.image.load(self.healthImageFile[4 - self.health]), (self.xCor, self.yCor + 60))