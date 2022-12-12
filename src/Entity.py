import random
from math import *
import pygame


class Entity:
    wonder = False
    entityCount = 0
    entityID = 0
    hitboxHeight = 0
    hitboxWidth = 0
    xCor = 0
    yCor = 0
    vel = 2
    health = 0
    dir = 0
    persist = 0
    tickCount = 0
    healthTexturePath = ["assets/EntityHealth0.png","assets/EntityHealth1.png","assets/EntityHealth2.png","assets/EntityHealth3.png","assets/EntityHealth4.png"]
    entityTexturePath = ""

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
            self.vel = int(random.random()*3)
            self.tickCount = 0
        else:
            self.tickCount+=1

    def move(self, event):
        self.xCor += int(self.vel*cos(self.dir))
        self.yCor += int(self.vel*sin(self.dir))

    def healthChange(self, healthchange):
        self.health += healthchange

    def checkCollisions(self):
        pass

    def render(self, win):
        win.blit(pygame.image.load(self.entityTexturePath), (self.xCor, self.yCor))
        win.blit(pygame.image.load(self.healthTexturePath[self.health]), (self.xCor, self.yCor + 60))

