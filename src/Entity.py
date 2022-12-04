import random
from math import *


class Entity:
    wonder = False
    entityCount = 0
    entityID = 0
    hitboxHeight = 0
    hitboxWidth = 0
    xCor = 0
    yCor = 0
    vel = 1.5
    health = 0
    dir = 0
    persist = 0
    tickCount = 0
    healthImageFile = ["assets/Health0.png","assets/Health1.png","assets/Health2.png","assets/Health3.png"]
    entityImageFile = ""

    def __init__(self, entityID, hitboxHeight, hitboxWidth, xCor, yCor, health):
        self.entityID = entityID
        self.hitboxHeight = hitboxHeight
        self.hitboxWidth = hitboxWidth
        self.xCor = xCor
        self.yCor = yCor
        self.health = health

    def changeDir(self, event):
        if self.tickCount == self.persist:
            self.dir = int(random.random() * 360)
            self.persist = int(random.random()*20)+8
            self.tickCount = 0
        else:
            self.tickCount+=1

    def move(self, event):
        self.xCor += int(self.vel*cos(self.dir))
        self.yCor += int(self.vel*sin(self.dir))

    def health(self, healthchange):
        self.health += healthchange

    def checkCollisions():
        pass

    

