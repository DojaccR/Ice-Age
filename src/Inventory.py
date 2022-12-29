import pygame
from InventorySlot import *
from Item import *
import sys


class Inventory:
    INVENTORY_MAX = 18
    HOTBAR_MAX = 6
    hotbarSlot = 0

    slot = [[],[],[],[],[],[],
            [],[],[],[],[],[],
            [],[],[],[],[],[],
            [],[],[],[],[],[]]

    isOpen = False

    def __init__(self, entityManager):
        self.entityManager = entityManager
        for i in range(24):
            self.slot.append(InventorySlot(i))

    def pickup(self, item):
        for i in range(self.INVENTORY_MAX + self.HOTBAR_MAX):
            if len(self.slot[i]) == 0 or (self.slot[i][0].itemName == item.itemName and len(self.slot[i]) < self.slot[i][0].itemStackMax):
                self.slot[i].append(item)
                break


    def use(self, playerObj):
        if len(self.slot[self.hotbarSlot]) > 0:
            if self.slot[self.hotbarSlot][len(self.slot[self.hotbarSlot])-1].itemType == "edible":
                self.slot[self.hotbarSlot][len(self.slot[self.hotbarSlot])-1].use(self.slot[self.hotbarSlot], playerObj)

            elif self.slot[self.hotbarSlot][len(self.slot[self.hotbarSlot])-1].itemType == "seed":
                self.slot[self.hotbarSlot][len(self.slot[self.hotbarSlot]) - 1].use(self.entityManager.structureList, self.slot[self.hotbarSlot], playerObj)
