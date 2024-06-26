import pygame
import random as Random
import HostileEntity
import Item

class Structure():
    xCor = 0
    yCor = 0


    def __init__(self, xCor, yCor):
        self.xCor = xCor
        self.yCor = yCor
        self.structureTexture = pygame.image.load(self.structureTexturePath)

    def render(self, win):
        win.blit(self.structureTexture, (self.xCor, self.yCor))


class IndestructableStructure(Structure):
    pass


class DestructableStructure(Structure):
    health = 0

    def die(self):
        pass

berryTexture = [pygame.image.load("assets/Bush0.png"),
                pygame.image.load("assets/Bush1.png"),
                pygame.image.load("assets/Bush2.png"),
                pygame.image.load("assets/Bush3.png"),
                pygame.image.load("assets/Bush4.png"),
                pygame.image.load("assets/Bush5.png")]
class BerryBush(DestructableStructure):
    berryCount = 0
    health = 2

    def __init__(self, xCor, yCor):
        self.xCor = xCor
        self.yCor = yCor

    def growBerry(self, tickCount):
        if tickCount % 400 == 0 and self.berryCount < 5:
            self.berryCount += 1

    def render(self, win):
        win.blit(berryTexture[self.berryCount], (self.xCor, self.yCor))

    def dropBerry(self, itemList):
        if self.berryCount > 0:
            self.berryCount -= 1
            itemList.append(Item.Berry(len(itemList), self.xCor, self.yCor))

    # deletes self
    def die(self, itemList, structureList):
        if self.health == 0:
            structureList.remove(self)
            itemList.append(Item.Seed(len(itemList), self.xCor, self.yCor))



class Cave(IndestructableStructure):
    structureTexturePath = "assets/Cave.png"
    caveType = ""

    def __init__(self, xCor, yCor):
        self.xCor = xCor
        self.yCor = yCor
        type = int(Random.random() * 2)
        if type == 0:
            self.caveType = "DireWolf"
        else:
            self.caveType = "SabreTooth"

    # spawns a wolf
    def spawnWolf(self, playerObj, mobList, renderedMobList, win, tickCount):
        if tickCount % 30 == 0:
            if self.caveType == "DireWolf":
                if self.xCor <= win.get_width() and self.xCor >= 0 and self.yCor <= win.get_height() and self.yCor >= 0 and len(renderedMobList) < 10:
                    mobList.append(HostileEntity.DireWolf(len(mobList), self.xCor + (pygame.image.load(self.structureTexturePath)).get_width()/2, self.yCor + (pygame.image.load(self.structureTexturePath)).get_height()))
            else:
                if self.xCor <= win.get_width() and self.xCor >= 0 and self.yCor <= win.get_height() and self.yCor >= 0 and len(renderedMobList) < 5:
                    mobList.append(HostileEntity.SabreTooth(len(mobList), self.xCor + (pygame.image.load(self.structureTexturePath)).get_width()/2, self.yCor + (pygame.image.load(self.structureTexturePath)).get_height()))

    def render(self, win):
        win.blit(pygame.image.load(self.structureTexturePath), (self.xCor, self.yCor))

