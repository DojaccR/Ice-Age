import random
import math
import pygame


class Entity:

    entityCount = 0
    healthTexturePath = ["assets/EntityHealth0.png","assets/EntityHealth1.png","assets/EntityHealth2.png","assets/EntityHealth3.png","assets/EntityHealth4.png"]

    # default constructor
    def __init__(self):
        self.entityID = 0
        self.hitboxHeight = 0
        self.hitboxWidth = 0
        self.xCor = 0
        self.yCor = 0
        self.wonder = False
        self.entityTexturePath = ""
        self.entityTexture = None
        self.vel = 2
        self.health = 0
        self.dir = 0
        self.persist = 0
        self.tickCount = 0

    # parameterised constructor
    # removed params for testing , entityTexturePath, vel
    def __init__(self, entityID, hitboxHeight, hitboxWidth, xCor, yCor, health):
        self.entityID = entityID
        self.hitboxHeight = hitboxHeight
        self.hitboxWidth = hitboxWidth
        self.xCor = xCor
        self.yCor = yCor
        self.health = health
        self.wonder = False
        self.entityTexturePath = ""
        # self.entityTexture = pygame.image.load(self.entityTexturePath)
        self.vel = 2
        self.dir = 0
        self.persist = 0
        self.tickCount = 0

    def changeDir(self):

        if self.tickCount == self.persist:
            self.dir = int(random.random() * 360)
            self.persist = int(random.random()*20)+8
            self.vel = int(random.random()*3)
            self.tickCount = 0
        else:
            self.tickCount+=1

    def move(self):
        self.xCor += int(self.vel*math.cos(self.dir))
        self.yCor += int(self.vel*math.sin(self.dir))

    def healthChange(self, healthchange):
        self.health += healthchange

    def checkCollisions(self):
        pass

    def render(self, win):
        win.blit(self.entityTexture, (self.xCor, self.yCor))
        win.blit(pygame.image.load(self.healthTexturePath[self.health]), (self.xCor, self.yCor + 60))

    def die(self, mobList, itemList):
        if self.health == 0:
            mobList.remove(self)
            self.dropItem(itemList)

    def dropItem(self):
        pass