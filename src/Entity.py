import random
from math import *


class Entity:
    entityCount = 0
    entityID = 0
    hitboxHeight = 0
    hitboxWidth = 0
    xCor = 0
    yCor = 0
    vel = 4
    health = 0
    healthImageFile = ["assets/Health0.png","assets/Health1.png","assets/Health2.png","assets/Health3.png"]
    def __init__(self, entityID, hitboxHeight, hitboxWidth, xCor, yCor, health):
        self.entityID = entityID
        self.hitboxHeight = hitboxHeight
        self.hitboxWidth = hitboxWidth
        self.xCor = xCor
        self.yCor = yCor
        self.health = health

    def move(self, event):
        dir = random.random() * 360
        self.xCor += int(4*cos(dir))
        self.yCor += int(4*sin(dir))

    def health(healthchange):
        health += healthchange

    def checkCollisions():
        pass

    

