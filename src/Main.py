from Player import *
from Map import *
from Entity import *
from HostileEntity import *
from Inventory import *
from Item import *
import random as random
import pygame
import sys

ENTITY_MAX = 3
ITEM_MAX = 10
#window loading
pygame.init()

win = pygame.display.set_mode((1280,720))

pygame.display.set_caption("Ice Age")
pygame.display.set_icon(pygame.image.load('assets/Logo.png'))

map = Map(0)
#player loading
playerObj = Player()
inventory = Inventory()

#wolf loading
entityList = []
#bery spawning
itemList = []
def spawnItem():
    x = int(random.random()*win.get_width())
    y = int(random.random() * win.get_height())
    if Item.itemCount < ITEM_MAX:
        itemList.append(Berry(len(itemList), x, y))
    Item.itemCount += 1

def spawnEntity():
    if Entity.entityCount < ENTITY_MAX:
        entityList.append(DireWolf(len(entityList), 600, 300))
    Entity.entityCount += 1




#game loop
gameTick = 0
run = True

while True:
    pygame.time.delay(10)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and playerObj.xCor > 0:
        playerObj.xCor -= playerObj.vel

    if keys[pygame.K_d] and playerObj.xCor < 1280 - playerObj.hitboxWidth:
        playerObj.xCor += playerObj.vel

    if keys[pygame.K_w] and playerObj.yCor > 0:
        playerObj.yCor -= playerObj.vel

    if keys[pygame.K_s] and playerObj.yCor < 720 - playerObj.hitboxHeight:
        playerObj.yCor += playerObj.vel



    #Background render
    win.fill((0, 255, 0))

    map.render1(playerObj, win)
    #Midground render

    #entity stuff
    for i in range(ENTITY_MAX):
        spawnEntity()
        entityList[i].changeDir(entityList[i])
        entityList[i].move(entityList[i])
        entityList[i].render(win)
        HostileEntity.target(entityList[i], playerObj)

    #item on ground/ interactable structures
    #need to write code to detect item on ground distance and pick up item into inventory
    for i in range(ITEM_MAX):
        spawnItem()
        itemList[i].pickup(playerObj, inventory, win)
        if itemList[i].isPickedUp == False:
            itemList[i].render(win)

    #Foreground render
    playerObj.render(win)
    inventory.hotRender(win)
    inventory.invRender(win)

    if keys[pygame.K_e]:
        print("pressed")
        inventory.toggleInvRender(win)

    for i in range(24):
        if len(inventory.slot[i]) > 0:
            pass
            #print(inventory.slot[i][0].itemName)

    gameTick += 1
    pygame.display.update()

pygame.quit()




