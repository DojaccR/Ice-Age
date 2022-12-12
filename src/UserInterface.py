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


    def healthRender(self, win):
        win.blit(pygame.image.load(self.healthbarImage[Player.health]), (1134, 20))







    def hotRender(self, Inventory, win):
        if Inventory.isOpen == False:
            win.blit(self.hotbarImage, (0, int(win.get_height()-120)))
            for i in range(6):
                if len(Inventory.slot[i]) > 0:
                    win.blit(Inventory.slot[i][0].itemImage, (i*120 + int((win.get_width()-720)/2), int(win.get_height()-130)))



    def invRender(self, Inventory, win):
        if Inventory.isOpen == True:
            pygame.time.delay(10)
            win.blit(self.inventoryImage, (0, int(win.get_height()-490)))

    def toggleInvRender(self, Inventory):
        if Inventory.isOpen == True:
            Inventory.isOpen = False
        else:
            Inventory.isOpen = True