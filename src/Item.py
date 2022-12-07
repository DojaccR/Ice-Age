import pygame
from Inventory import *
from math import *

class Item:
    itemID = 0
    itemName = ""
    itemTexturePath = ""
    itemImage = None
    isPickedUp = False
    xCor = 0
    yCor = 0
    itemCount = 0

    def __init__(self, itemID, itemName, xCor, yCor):
        self.itemID = itemID
        self.itemName = itemName
        self.xCor = xCor
        self.yCor = yCor

    def pickup(self, playerObj, inventory, win):
        if int(sqrt((self.xCor-playerObj.xCor)**2+(self.yCor-playerObj.yCor)**2)) < 20 and self.isPickedUp == False:
            inventory.pickup(self, win)
            self.isPickedUp = True

            #print(str(int(sqrt((self.xCor-playerObj.xCor)**2+(self.yCor-playerObj.yCor)**2))))


class Clothing(Item):
    itemStackMax = 1


class Tool(Item):
    itemStackMax = 1


class Consumable(Item):
    def __init__(self, itemID, itemName, xCor, yCor):
        super().__init__(itemID, itemName, xCor, yCor)

    itemStackMax = 15


class Berry(Consumable):
    def __init__(self, itemID, xCor, yCor):
        super().__init__(itemID, "berry", xCor, yCor)
        self.itemTexturePath = "assets/Berry.png"
        self.itemImage = pygame.image.load(self.itemTexturePath)

    def render(self, win):
        win.blit(self.itemImage, (self.xCor, self.yCor))
        #win.blit(pygame.image.load(self.healthImageFile[4 - self.health]), (self.xCor, self.yCor + 60))