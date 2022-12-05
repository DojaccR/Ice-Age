import pygame
from InventorySlot import *


class Inventory:
    INVENTORY_MAX = 18
    HOTBAR_MAX = 6
    slot = []
    inventoryImageFile = "assets/Inventory.png"
    hotbarImageFile = "assets/Hotbar.png"
    hoverImageFile = "assets/Hover.png"
    hotbarImage = pygame.image.load(hotbarImageFile)

    def __init__(self):
        for i in range(24):
            self.slot.append(InventorySlot(i))

    def open(self, win):
        isOpen = True

        while isOpen:
            pygame.time.delay(10)

            print("open")

            win.blit(pygame.image.load("assets/Inventory.png"), (0, 0))

            keys = pygame.key.get_pressed()
            print(keys)
            if keys[pygame.K_e]:
                isOpen = False

    def render(self, win):
        win.blit(self.hotbarImage, (int((win.get_width()-900)/2), int(win.get_height()-160)))
        #win.blit(pygame.image.load(self.healthImageFile[4 - self.health]), (self.xCor, self.yCor + 60))

    def pickup(self, item):
        pass

