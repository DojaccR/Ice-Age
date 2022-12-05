import pygame
from InventorySlot import *


class Inventory:
    INVENTORY_MAX = 18
    HOTBAR_MAX = 6
    slot = []
    inventoryImageFile = "assets/Inventory.png"
    hotbarImageFile = "assets/Hotbar.png"
    hoverImageFile = "assets/Hover.png"

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

