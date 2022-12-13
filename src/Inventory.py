import pygame
from InventorySlot import *
from Item import *
import sys


class Inventory:
    INVENTORY_MAX = 18
    HOTBAR_MAX = 6

    slot = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

    isOpen = False

    def __init__(self):
        for i in range(24):
            self.slot.append(InventorySlot(i))

    def pickup(self, item):
        for i in range(self.INVENTORY_MAX + self.HOTBAR_MAX):
            if len(self.slot[i]) == 0 or (self.slot[i][0].itemName == item.itemName and len(self.slot[i]) < self.slot[i][0].itemStackMax):
                self.slot[i].append(item)
                break



