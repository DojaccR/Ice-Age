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

    def open(self):
        isOpen = True

        while isOpen:
            print("opena")
            keys = pygame.key.get_pressed()

            if keys[pygame.K_e]:
                isOpen = False

