import pygame
from InventorySlot import *
from Item import *
import sys


class Inventory:
    INVENTORY_MAX = 18
    HOTBAR_MAX = 6

    slot = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

    inventoryImageFile = "assets/Inventory.png"
    hotbarImageFile = "assets/Hotbar.png"
    hoverImageFile = "assets/Hover.png"
    hotbarImage = pygame.image.load(hotbarImageFile)
    inventoryImage = pygame.image.load(inventoryImageFile)

    isOpen = False

    def __init__(self):
        for i in range(24):
            self.slot.append(InventorySlot(i))

    def invRender(self, win):
        if self.isOpen == True:
            pygame.time.delay(10)
            win.blit(self.inventoryImage, (0, 0))

    def toggleInvRender(self, win):
        if self.isOpen == True:
            self.isOpen = False
        else:
            self.isOpen = True
            self.invRender(win)


    def hotRender(self, win):
        win.blit(self.hotbarImage, (int((win.get_width()-900)/2), int(win.get_height()-160)))
        for i in range(6):
            if len(self.slot[i]) > 0:
                win.blit(self.slot[i][0].itemImage, (i*150 + int((win.get_width()-900)/2), int(win.get_height()-160)))
        #win.blit(pygame.image.load(self.healthImageFile[4 - self.health]), (self.xCor, self.yCor + 60))

    def pickup(self, item, win):
        print('pickup')
        for i in range(self.INVENTORY_MAX + self.HOTBAR_MAX):
            if len(self.slot[i]) == 0 or (self.slot[i][0].itemName == item.itemName and len(self.slot[i]) < self.slot[i][0].itemStackMax):
                print("succes 1")
                self.slot[i].append(item)
                print(self.slot[i])
                break



