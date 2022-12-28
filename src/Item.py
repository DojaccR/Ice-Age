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
    itemType = ""

    def __init__(self, itemID, itemName, xCor, yCor):
        self.itemID = itemID
        self.itemName = itemName
        self.xCor = xCor
        self.yCor = yCor

    def pickup(self, playerObj, inventory, itemList):
        if int(sqrt((self.xCor-playerObj.xCor)**2+(self.yCor-playerObj.yCor)**2)) < 20 and self.isPickedUp == False:
            inventory.pickup(self)
            itemList.remove(self)
            self.isPickedUp = True

            #print(str(int(sqrt((self.xCor-playerObj.xCor)**2+(self.yCor-playerObj.yCor)**2))))

    def render(self, win):
        if self.isPickedUp == False:
            win.blit(self.itemImage, (self.xCor, self.yCor))

    def use(self):
        pass

class Clothing(Item):
    itemStackMax = 1


class Tool(Item):
    itemStackMax = 1


class Consumable(Item):
    def __init__(self, itemID, itemName, xCor, yCor):
        super().__init__(itemID, itemName, xCor, yCor)

    itemStackMax = 15

class Berry(Consumable):
    itemType = "edible"
    def __init__(self, itemID, xCor, yCor):
        super().__init__(itemID, "berry", xCor, yCor)
        self.itemTexturePath = "assets/Berry.png"
        self.itemImage = pygame.image.load(self.itemTexturePath)

    def useItem(self, slot, playerObj):
        slot.remove(self)
        if playerObj.hunger + 10 <= 100:
            playerObj.hunger += 10
        else:
            playerObj.hunger = 100

        #win.blit(pygame.image.load(self.healthImageFile[4 - self.health]), (self.xCor, self.yCor + 60))

class WolfSkin(Consumable):
    itemType = "material"

    def __init__(self, itemID, xCor, yCor):
        super().__init__(itemID, "wolfskin", xCor, yCor)
        self.itemTexturePath = "assets/WolfSkin.png"
        self.itemImage = pygame.image.load(self.itemTexturePath)

class Flint(Consumable):
    itemType = "material"

    def __init__(self, itemID, xCor, yCor):
        super().__init__(itemID, "flint", xCor, yCor)
        self.itemTexturePath = "assets/Flint.png"
        self.itemImage = pygame.image.load(self.itemTexturePath)

class Seed(Consumable):
    itemType = "seed"

    def __init__(self, itemID, xCor, yCor):
        super().__init__(itemID, "seed", xCor, yCor)
        self.itemTexturePath = "assets/Seed.png"
        self.itemImage = pygame.image.load(self.itemTexturePath)