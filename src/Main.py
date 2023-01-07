import pygame
import Map
import Entity
import Player
import HostileEntity
import Inventory
import Item
import random as random

import UserInterface
import EntityManager

CAMERA_SPEED = 15

# window loading

pygame.init()

win = pygame.display.set_mode((1280,720))

pygame.display.set_caption("Ice Age")
pygame.display.set_icon(pygame.image.load('assets/Logo.png'))

map = Map.Map("create")
entityManager = EntityManager.EntityManager()
userInterface = UserInterface.UserInterface()

# player loading

playerObj = Player.Player(win)
inventory = Inventory.Inventory(entityManager)

# game loop

clock = pygame.time.Clock()
gameTick = 0
run = True

pygame.mixer.init()
pygame.mixer.music.load("audio/Theme1.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play()

while True:
    pygame.time.delay(10)
    if gameTick % 200 == 0 and playerObj.hunger > 0:
        playerObj.hunger -= 1
    entityManager.checkRenderedEntities(win)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            entityManager.playerInteract(playerObj, "m1")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                run = False

            if event.key == pygame.K_e:
                userInterface.toggleInvRender(inventory)

            if event.key == pygame.K_f:
                entityManager.playerInteract(playerObj, "f")

            if event.key == pygame.K_q:
                inventory.use(playerObj)

            # toggle UI rendering

            if event.key == pygame.K_F1:
                userInterface.toggleUI(userInterface)

            if event.key == pygame.K_1:
                inventory.hotbarSlot = 0

            if event.key == pygame.K_2:
                inventory.hotbarSlot = 1

            if event.key == pygame.K_3:
                inventory.hotbarSlot = 2

            if event.key == pygame.K_4:
                inventory.hotbarSlot = 3

            if event.key == pygame.K_5:
                inventory.hotbarSlot = 4

            if event.key == pygame.K_6:
                inventory.hotbarSlot = 5

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and playerObj.mapXCor > (win.get_width()/map.tileWidth)/2 + 1:
        playerObj.inBlockXCor += CAMERA_SPEED
        map.blockChange(playerObj)
        entityManager.move("x", "positive", CAMERA_SPEED)
        if int(random.random()*100) > 98:
            playerObj.hunger -= 1

    if keys[pygame.K_d] and playerObj.mapXCor < map.mapSize - (win.get_width()/map.tileWidth)/2 - 3:
        playerObj.inBlockXCor -= CAMERA_SPEED
        map.blockChange(playerObj)
        entityManager.move("x", "negative", CAMERA_SPEED)
        if int(random.random()*100) > 98:
            playerObj.hunger -= 1

    if keys[pygame.K_w] and playerObj.mapYCor > (win.get_height()/map.tileHeight)/2 + 1:
        playerObj.inBlockYCor += CAMERA_SPEED
        map.blockChange(playerObj)
        entityManager.move("y", "positive", CAMERA_SPEED)
        if int(random.random()*100) > 98:
            playerObj.hunger -= 1

    if keys[pygame.K_s] and playerObj.mapYCor < map.mapSize - (win.get_height()/map.tileHeight)/2 - 4:
        playerObj.inBlockYCor -= CAMERA_SPEED
        map.blockChange(playerObj)
        entityManager.move("y", "negative", CAMERA_SPEED)
        if int(random.random()*100) > 98:
            playerObj.hunger -= 1

    # Background render

    #win.fill((0, 255, 0))

    map.render1(playerObj, win)

    entityManager.runStructureFunctions(gameTick, playerObj, win)
    entityManager.runMobFunctions(playerObj)
    entityManager.runItemFunctions(playerObj, inventory, win)
    entityManager.renderEntities(win)

    # Foreground render

    playerObj.render(win)
    userInterface.statRender(win, playerObj)
    userInterface.hotRender(inventory, win)
    userInterface.invRender(inventory, win)

    # fps counter

    clock.tick()
    userInterface.draw_text(win, str(int(clock.get_fps())), "white", (10, 0))

    gameTick += 1
    pygame.display.update()

pygame.quit()




