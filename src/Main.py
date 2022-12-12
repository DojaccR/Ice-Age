from Player import *
from Map import *
from Entity import *
from HostileEntity import *
from Inventory import *
from Item import *
import random as random
import pygame
from UserInterface import *
from EntityManager import *

ENTITY_MAX = 3
ITEM_MAX = 10
CAMERA_SPEED = 10
#window loading
pygame.init()

win = pygame.display.set_mode((1280,720))

pygame.display.set_caption("Ice Age")
pygame.display.set_icon(pygame.image.load('assets/Logo.png'))

map = Map(0)
entityManager = EntityManager()
#player loading
playerObj = Player(win)
inventory = Inventory()

'''
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


'''

#game loop
clock = pygame.time.Clock()
gameTick = 0
run = True

while True:
    pygame.time.delay(10)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                run = False

            if event.key == pygame.K_e:
                print("inventory open")
                UserInterface.toggleInvRender(UserInterface, Inventory)

            #toggle UI rendering
            if event.key == pygame.K_F1:
                UserInterface.toggleUI(UserInterface)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and playerObj.xCor > 0:
        #playerObj.xCor -= playerObj.vel
        playerObj.inBlockXCor += CAMERA_SPEED#playerObj.vel
        map.blockChange(playerObj)
        entityManager.move("x", "positive", CAMERA_SPEED)


    if keys[pygame.K_d] and playerObj.xCor < 1280 - playerObj.hitboxWidth:
        #playerObj.xCor += playerObj.vel
        playerObj.inBlockXCor -= CAMERA_SPEED#playerObj.vel
        map.blockChange(playerObj)
        entityManager.move("x", "negative", CAMERA_SPEED)


    if keys[pygame.K_w] and playerObj.yCor > 0:
        #playerObj.yCor -= playerObj.vel
        playerObj.inBlockYCor += CAMERA_SPEED#playerObj.vel
        map.blockChange(playerObj)
        entityManager.move("y", "positive", CAMERA_SPEED)

    if keys[pygame.K_s] and playerObj.yCor < 720 - playerObj.hitboxHeight:
        #playerObj.yCor += playerObj.vel
        playerObj.inBlockYCor -= CAMERA_SPEED#playerObj.vel
        map.blockChange(playerObj)
        entityManager.move("y", "negative", CAMERA_SPEED)


    #Background render
    win.fill((0, 255, 0))

    map.render1(playerObj, win)
    entityManager.checkRenderedEntities(playerObj, win)
    entityManager.runStructureFunctions(gameTick, playerObj, win)
    entityManager.renderEntities(win)
    #Midground render

    #entity stuff

    #item on ground/ interactable structures
    #need to write code to detect item on ground distance and pick up item into inventory


    #Foreground render
    playerObj.render(win)
    UserInterface.statRender(UserInterface, win)
    UserInterface.hotRender(UserInterface, Inventory, win)
    UserInterface.invRender(UserInterface, Inventory, win)

    #fps counter
    clock.tick()
    UserInterface.draw_text(UserInterface, win, str(int(clock.get_fps())), "white", (10, 0))

    for i in range(24):
        if len(inventory.slot[i]) > 0:
            pass
            #print(inventory.slot[i][0].itemName)

    gameTick += 1
    pygame.display.update()

pygame.quit()




