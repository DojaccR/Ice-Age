import Entity
import Item
import math
import pygame
import random as random

class HostileEntity(Entity.Entity):
    damage = 0
    aggroRange = 0
    aggro = False
    atkRange = 0

    def __init__(self, entityID, hitboxHeight, hitboxWidth, xCor, yCor, health, damage):
        super().__init__(entityID, hitboxHeight, hitboxWidth, xCor, yCor, health)
        self.damage = damage

    def changeDirection(self):

        if self.tickCount >= self.persist and self.aggro == False:
            self.direction = int(random.random() * 360)
            self.persist = int(random.random()*20)+8
            self.vel = int(random.random()*3)
            self.tickCount = 0
        else:
            self.tickCount+=1
    
    def attack(self):
        pass

    def target(self, playerObj):

        if int(math.sqrt((self.xCor-playerObj.xCor)**2+(self.yCor-playerObj.yCor)**2)) < self.aggroRange:
            self.aggro = True
            self.vel = 3

            if playerObj.yCor-self.yCor > 0 and playerObj.xCor-self.xCor < 0:
                self.direction = math.atan((playerObj.yCor-self.yCor)/(playerObj.xCor-self.xCor)) + 180
            elif playerObj.yCor-self.yCor < 0 and playerObj.xCor-self.xCor < 0:
                self.direction = math.atan((playerObj.yCor-self.yCor)/(playerObj.xCor-self.xCor)) - 180
            elif playerObj.xCor-self.xCor != 0:
                self.direction = math.atan((playerObj.yCor-self.yCor)/(playerObj.xCor-self.xCor))

            self.move()

            if int(math.sqrt((self.xCor-playerObj.xCor)**2+(self.yCor-playerObj.yCor)**2)) <= self.atkRange and playerObj.health > 1 and self.tickCount%100 == 0:
                playerObj.health -= self.damage
        else:
            self.aggro = False

    
class DireWolf(HostileEntity):
    entityTexturePath = "assets/Wolf.png"
    entityTexture = pygame.image.load(entityTexturePath)
    hitboxHeight = entityTexture.get_height()
    hitboxWidth = entityTexture.get_width()
    health = 4
    damage = 1
    aggroRange = 150
    atkRange = 10

    def __init__(self, entityID, xCor, yCor):
        super().__init__(entityID, self.hitboxHeight, self.hitboxWidth, xCor, yCor, self.health, self.damage)

    def dropItem(self, itemList):
        itemList.append(Item.WolfSkin(len(itemList), self.xCor, self.yCor))


class SabreTooth(HostileEntity):
    entityTexturePath = "assets/Sabre.png"
    entityTexture = pygame.image.load(entityTexturePath)
    hitboxHeight = entityTexture.get_height()
    hitboxWidth = entityTexture.get_width()
    health = 4
    damage = 1
    aggroRange = 600
    atkRange = 15

    def __init__(self, entityID, xCor, yCor):
        super().__init__(entityID, self.hitboxHeight, self.hitboxWidth, xCor, yCor, self.health, self.damage)

    def dropItem(self, itemList):
        itemList.append(Item.WolfSkin(len(itemList), self.xCor, self.yCor))
