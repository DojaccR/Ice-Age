import pygame
from Player import *
from Entity import *
from Inventory import *

class UserInterface:
    healthbarImage = ["assets/PlayerHealth0.png","assets/PlayerHealth1.png","assets/PlayerHealth2.png","assets/PlayerHealth3.png","assets/PlayerHealth4.png"]
    hungerbarImage = "assets/HungerBar.png"
    hungerIconImage = "assets/HungerIcon.png"
    temperatureImage = "assets/TemperatureNeutral.png"
    hotbarImage = "assets/Hotbar.png"
    hotbarSelectorImage = "assets/InventorySlotHover.png"
    inventoryImage = "assets/Inventory.png"

    displayUI = True


    def draw_text(self, win, obj, colour, pos):
        self.font = pygame.font.SysFont("Arial", 20)
        self.text = self.font.render(obj, 1, pygame.Color(colour))
        win.blit(self.text, pos)


    def statRender(self, win, playerObj):
        if self.displayUI == True:
            win.blit(pygame.image.load(self.healthbarImage[playerObj.health]), (1134, 20))
            win.blit(pygame.image.load(self.hungerIconImage), (1126, 60))
            win.blit(pygame.transform.scale(pygame.image.load(self.hungerbarImage), (104*playerObj.hunger/100, 20)), (1156, 60))
            win.blit(pygame.image.load(self.temperatureImage), (1136, 88))



    def hotRender(self, inventory, win):
        if self.displayUI == True:
            if inventory.isOpen == False:
                win.blit(pygame.image.load(self.hotbarImage), (0, int(win.get_height()-120)))
                win.blit(pygame.image.load(self.hotbarSelectorImage), (120*inventory.hotbarSlot, int(win.get_height()-120)))
                for i in range(6):
                    if len(inventory.slot[i]) > 0:
                        win.blit(pygame.transform.scale(inventory.slot[i][0].itemImage, (100,100)), (i*120, int(win.get_height()-120)))
                        self.draw_text(win, str(len(inventory.slot[i])), "magenta", (i*120 + 100, int(win.get_height()-30)))



    def invRender(self, inventory, win):
        if self.displayUI == True:
            if inventory.isOpen == True:
                pygame.time.delay(10)
                win.blit(pygame.image.load(self.inventoryImage), (0, int(win.get_height()-490)))
                for i in range(6):
                    if len(inventory.slot[i]) > 0:
                        win.blit(pygame.transform.scale(inventory.slot[i][0].itemImage, (100,100)), (i*120, int(win.get_height()-120)))
                        self.draw_text(win, str(len(inventory.slot[i])), "magenta", (i*120 + 100, int(win.get_height()-30)))

    def toggleInvRender(self, inventory):
        if inventory.isOpen == True:
            inventory.isOpen = False
        else:
            inventory.isOpen = True


    def toggleUI(self):
        if self.displayUI == True:
            self.displayUI = False
        else:
            self.displayUI = True