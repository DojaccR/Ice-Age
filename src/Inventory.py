import pygame
import InventorySlot
import Item
import sys


class Inventory():
    INVENTORY_MAX = 18
    HOTBAR_MAX = 6
    hotbarSlot = 0
    curser = (0, 0)

    slot = [[],[],[],[],[],[],
            [],[],[],[],[],[],
            [],[],[],[],[],[],
            [],[],[],[],[],[]]

    isOpen = False

    # filling slot array with slot objects
    def __init__(self, entityManager):
        self.entityManager = entityManager
        for i in range(24):
            self.slot.append(InventorySlot.InventorySlot(i))

    # picking item off the floor. runs through the inventory checks if the slot contains an object of the same time and
    # if the max stack has been reached.
    def pickup(self, item):
        for i in range(self.INVENTORY_MAX + self.HOTBAR_MAX):
            if len(self.slot[i]) == 0 or (self.slot[i][0].itemName == item.itemName and len(self.slot[i]) < self.slot[i][0].itemStackMax):
                self.slot[i].append(item)
                break

    # function to call the use function of items. checks item types and gives the necessary parameters
    def use(self, playerObj):
        if len(self.slot[self.hotbarSlot]) > 0:
            if self.slot[self.hotbarSlot][len(self.slot[self.hotbarSlot])-1].itemType == "edible":
                self.slot[self.hotbarSlot][len(self.slot[self.hotbarSlot])-1].use(self.slot[self.hotbarSlot], playerObj)

            elif self.slot[self.hotbarSlot][len(self.slot[self.hotbarSlot])-1].itemType == "seed":
                self.slot[self.hotbarSlot][len(self.slot[self.hotbarSlot]) - 1].use(self.entityManager.structureList, self.slot[self.hotbarSlot], playerObj)

    # moves the curser of the inventory
    def movecurser(self, direction):
        if direction == 'u':
            if self.curser[0] < 3:
                self.curser[0] += 1

        elif direction == 'd':
            if self.curser[0] > 0:
                self.curser[0] -= 1

        elif direction == 'l':
            if self.curser[1] > 0:
                self.curser[1] -= 1

        else:
            if self.curser[1] < 5:
                self.curser[1] += 1
