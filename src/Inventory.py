import pygame
from InventorySlot import *
from Item import *


class Inventory:
    INVENTORY_MAX = 18
    HOTBAR_MAX = 6

    #slot = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            #[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            #[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            #[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]

    #stackCount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    slot = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

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
            if len(self.slot[i]) > 0:
                win.blit(self.slot[i][0].itemImage, (i*150 + int((win.get_width()-900)/2), int(win.get_height()-160)))
        #win.blit(pygame.image.load(self.healthImageFile[4 - self.health]), (self.xCor, self.yCor + 60))

    #def pickup(self, item, win):
        #print("pickup")
        #for i in range(self.INVENTORY_MAX + self.HOTBAR_MAX):
            #print(self.slot[i][item.itemStackMax-1])
            #if self.slot[i][0] == None or (item.itemName == self.slot[i][0].itemName and self.slot[i][item.itemStackMax-1] > self.stackCount[i]):
                #print("item appended")
                #self.slot.insert([i][self.stackCount[i]], item)
                #self.stackCount[i] += 1
                #print(self.slot[i][0])
                #break

    def pickup(self, item, win):
        print('pickup')
        for i in range(self.INVENTORY_MAX + self.HOTBAR_MAX):
            if len(self.slot[i]) == 0 or (self.slot[i][0].itemName == item.itemName and len(self.slot[i]) < self.slot[i][0].itemStackMax):
                print("succes 1")
                self.slot[i].append(item)
                print(self.slot[i])
                break



