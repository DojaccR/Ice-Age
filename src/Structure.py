import pygame

class Structure:
    xCor = 0
    yCor = 0
    structureTexturePath = ""


    def __init__(self, xCor, yCor, structureTexturePath):
        self.xCor = xCor
        self.yCor = yCor
        self.structureTexturePath = structureTexturePath
        self.structureTexture = pygame.image.load(self.structureTexturePath)

    def render(self, win):
        win.blit(self.structureTexture, (self.xCor, self.yCor))



class IndestructableStructure(Structure):
    pass

class DestructableStructure(Structure):
    health = 0

class BerryBush(DestructableStructure):
    berryCount = 0

    def __init__(self):
        pass

    def growBerry(self):
        pass

    def pickBerry(self):
        pass



