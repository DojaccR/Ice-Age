import pygame
from InventorySlot import *


class Inventory:
    INVENTORY_MAX = 18
    HOTBAR_MAX = 6

    slot = [[None], [None], [None], [None], [None], [None],
            [None], [None], [None], [None], [None], [None],
            [None], [None], [None], [None], [None], [None],
            [None], [None], [None], [None], [None], [None]]

    inventoryImageFile = "assets/Inventory.png"
    hotbarImageFile = "assets/Hotbar.png"
    hoverImageFile = "assets/Hover.png"
    hotbarImage = pygame.image.load(hotbarImageFile)
    inventoryImage = pygame.image.load(inventoryImageFile)

    def __init__(self):
        for i in range(24):
            self.slot.append(InventorySlot(i))

    def open(self, win):
        isOpen = True

        while isOpen:
            pygame.time.delay(10)

            print("open")

            win.blit(self.inventoryImage, (0, 0))

            keys = pygame.key.get_pressed()
            print(keys)
            #if keys[pygame.K_e]:
                #isOpen = False

    def render(self, win):
        win.blit(self.hotbarImage, (int((win.get_width()-900)/2), int(win.get_height()-160)))
        for i in range(6):
            if self.slot[i][0] != None:
                win.blit(self.slot[i][0].itemImage, (i*150 + 150, 850))
        #win.blit(pygame.image.load(self.healthImageFile[4 - self.health]), (self.xCor, self.yCor + 60))

    def pickup(self, item):
        print("pickup")
        for i in range(self.INVENTORY_MAX + self.HOTBAR_MAX):
            print("inventory")
            if self.slot[i][0] == None or (item.itemName == self.slot[i][0].itemName and self.slot[i][item.itemStackMax] == None):
                print("item appended")
                self.slot[i].append(item)
                break



