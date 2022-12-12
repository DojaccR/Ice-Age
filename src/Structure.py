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
    structureTexturePath = ["assets/Bush0.png",
                            "assets/Bush1.png",
                            "assets/Bush2.png",
                            "assets/Bush3.png",
                            "assets/Bush4.png",
                            "assets/Bush5.png"]

    def __init__(self, xCor, yCor):
        self.xCor = xCor
        self.yCor = yCor

    def growBerry(self, tickCount):
        if tickCount % 400 == 0 and self.berryCount < 5:
            self.berryCount += 1

    def pickBerry(self):
        pass

    def render(self, win):
        win.blit(pygame.image.load(self.structureTexturePath[self.berryCount]), (self.xCor, self.yCor))


class Cave(IndestructableStructure):
    structureTexturePath = "assets/Cave.png"
    def __init__(self):
        pass

    def spawnWolf(self):
        pass

    def render(self, win):
        pass

