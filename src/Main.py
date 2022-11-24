from Player import *
from Entity import *
from HostileEntity import *
import pygame

ENTITY_MAX = 2
#window loading
pygame.init()

win = pygame.display.set_mode((1280,720))

pygame.display.set_caption("Ice Age")
pygame.display.set_icon(pygame.image.load('assets/Logo.png'))


#player loading
playerObj = Player(1, 100, 100, 200, 200, 4)
playerImage = pygame.image.load(playerObj.entityImageFile)

def player():
    win.blit(playerImage, (playerObj.xCor, playerObj.yCor))
    win.blit(pygame.image.load(playerObj.healthImageFile[4-playerObj.health]), (playerObj.xCor, playerObj.yCor+60))

#wolf loading
entityList = []

def spawnEntity():
    if Entity.entityCount < ENTITY_MAX:
        entityList.append(DireWolf(len(entityList), 600, 300))
    Entity.entityCount += 1

def wolf(i):
    win.blit(pygame.image.load(entityList[i].entityImageFile), (entityList[i].xCor, entityList[i].yCor))
    win.blit(pygame.image.load(entityList[i].healthImageFile[4-entityList[i].health]), (entityList[i].xCor, entityList[i].yCor+60))


def target(self, playerObj):
    if int(sqrt((self.xCor - playerObj.xCor) ** 2 + (self.yCor - playerObj.yCor) ** 2)) < 100:
        print(playerObj.xCor)
        print(self.xCor)
        print("attack, distance is " + str((self.xCor - playerObj.xCor) ** 2) + " " + str(
            (self.yCor - playerObj.yCor) ** 2) + " " + str(
            sqrt((self.xCor - playerObj.xCor) ** 2 + (self.yCor - playerObj.yCor) ** 2)))


#game loop
gameTick = 0
run = True

while playerObj.health > 0:
    pygame.time.delay(10)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and playerObj.xCor > 0:
        playerObj.xCor -= playerObj.vel

    if keys[pygame.K_RIGHT] and playerObj.xCor < 1280 - playerObj.hitboxWidth:
        playerObj.xCor += playerObj.vel

    if keys[pygame.K_UP] and playerObj.yCor > 0:
        playerObj.yCor -= playerObj.vel

    if keys[pygame.K_DOWN] and playerObj.yCor < 720 - playerObj.hitboxHeight:
        playerObj.yCor += playerObj.vel

    win.fill((0,255,0))
  
    player()
  
    for i in range(ENTITY_MAX):
        spawnEntity()
        entityList[i].changeDir(entityList[i])
        entityList[i].move(entityList[i])
        wolf(i)
        target(entityList[i], playerObj)


    
    gameTick+=1
    pygame.display.update()

pygame.quit()




