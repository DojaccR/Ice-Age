from Entity import *
from math import *
import pygame

class HostileEntity(Entity):
    damage = 0
    aggroRange = 0
    aggro = False
    atkRange = 0

    def __init__(self, entityID, hitboxHeight, hitboxWidth, xCor, yCor, health, damage):
        super().__init__(entityID, hitboxHeight, hitboxWidth, xCor, yCor, health)
        self.damage = damage

    def changeDir(self, event):
        if self.tickCount >= self.persist and self.aggro == False:
            self.dir = int(random.random() * 360)
            self.persist = int(random.random()*20)+8
            self.vel = int(random.random()*3)
            self.tickCount = 0
        else:
            self.tickCount+=1

    def move(self, event):
        self.xCor += int(self.vel*cos(self.dir))
        self.yCor += int(self.vel*sin(self.dir))
    
    def attack(self):
        pass

    def target(self, playerObj):
        if int(sqrt((self.xCor-playerObj.xCor)**2+(self.yCor-playerObj.yCor)**2)) < self.aggroRange:
            self.aggro = True
            self.vel = 3
            if playerObj.yCor-self.yCor > 0 and playerObj.xCor-self.xCor < 0:
                self.dir = atan((playerObj.yCor-self.yCor)/(playerObj.xCor-self.xCor)) + 180
            elif playerObj.yCor-self.yCor < 0 and playerObj.xCor-self.xCor < 0:
                self.dir = atan((playerObj.yCor-self.yCor)/(playerObj.xCor-self.xCor)) - 180
            elif playerObj.xCor-self.xCor != 0:
                self.dir = atan((playerObj.yCor-self.yCor)/(playerObj.xCor-self.xCor))
            self.move(e)
            if int(sqrt((self.xCor-playerObj.xCor)**2+(self.yCor-playerObj.yCor)**2)) <= self.atkRange and playerObj.health > 1 and self.tickCount%100 == 0:
                playerObj.health -= self.damage
                print("player health is "+str(playerObj.health))
            print(playerObj.xCor)
            print(self.xCor)
            print("attack, distance is " + str((self.xCor-playerObj.xCor)**2) + " "+ str((self.yCor-playerObj.yCor)**2) + " " + str(sqrt((self.xCor-playerObj.xCor)**2+(self.yCor-playerObj.yCor)**2)))
        else:
            self.aggro = False

    
class DireWolf(HostileEntity):
    entityImageFile = "assets/Wolf.png"
    hitboxHeight = 50
    hitboxWidth = 100
    health = 4
    damage = 1
    aggroRange = 150
    atkRange = 10

    def __init__(self, entityID, xCor, yCor):
        super().__init__(entityID, 50, 100, xCor, yCor, 4, 1)

    def render(self, i, win):
        win.blit(pygame.image.load(self.entityImageFile), (self.xCor, self.yCor))
        win.blit(pygame.image.load(self.healthImageFile[4 - self.health]), (self.xCor, self.yCor + 60))


    
