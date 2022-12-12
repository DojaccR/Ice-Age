import pygame
from Player import *
from Entity import *
from Inventory import *

class UserInterface:
    healthbarImage = ["assets/PlayerHealth0.png","assets/PlayerHealth1.png","assets/PlayerHealth2.png","assets/PlayerHealth3.png","assets/PlayerHealth4.png"]
    hungerbarImage = "assets/Hunger100.png"
    temperatureImage = "assets/TemperatureNeutral.png"
    hotbarImage = "assets/Hotbar.png"
    inventoryImage = "assets/Inventory.png"

    displayUI = True


    def draw_text(self, win, obj, colour, pos):
        self.font = pygame.font.SysFont("Arial", 20)
        self.text = self.font.render(obj, 1, pygame.Color(colour))
        win.blit(self.text, pos)


    def statRender(self, win):
        if self.displayUI == True:
            win.blit(pygame.image.load(self.healthbarImage[Player.health]), (1134, 20))

            win.blit(pygame.image.load(self.hungerbarImage), (1126, 60))

            win.blit(pygame.image.load(self.temperatureImage), (1136, 88))



    def hotRender(self, Inventory, win):
        if self.displayUI == True:
            if Inventory.isOpen == False:
                win.blit(pygame.image.load(self.hotbarImage), (0, int(win.get_height()-120)))
                for i in range(6):
                    if len(Inventory.slot[i]) > 0:
                        win.blit(Inventory.slot[i][0].itemImage, (i*120, int(win.get_height()-120)))



    def invRender(self, Inventory, win):
        if self.displayUI == True:
            if Inventory.isOpen == True:
                pygame.time.delay(10)
                win.blit(pygame.image.load(self.inventoryImage), (0, int(win.get_height()-490)))

    def toggleInvRender(self, Inventory):
        if Inventory.isOpen == True:
            Inventory.isOpen = False
        else:
            Inventory.isOpen = True


    def toggleUI(self):
        if self.displayUI == True:
            self.displayUI = False
        else:
            self.displayUI = True