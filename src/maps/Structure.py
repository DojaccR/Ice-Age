import pygame

class Structure:
    xCor = 0
    yCor = 0
    structureTexturePath = ""
    structureTexture = pygame.image.load(structureTexturePath)

    def __init__(self, xCor, yCor, structureTexturePath):
        self.xCor = xCor
        self.yCor = yCor
        self.structureTexturePath = structureTexturePath

    def render(self, win):
        win.blit(self.structureTexture, (self.xCor, self.yCor))



class IndistructableStructure(Structure):
    pass

class DestructableStructure(Structure):
    health = 0