import os
import pygame
import time

from ChickenRun.src.Chicken2D import Chicken
from ChickenRun.src.Rooms import Room


chickenTexture = pygame.image.load("ChickenRun\\assets\\chicken\\chicken\\chickenprofilewalkx4.gif")

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

window = pygame.display.set_mode((256*2,256*2))
clock = pygame.time.Clock()

room = Room(16, 24, 24)

x0 = 120
y0 = 120
chicken = Chicken((x0, y0),(120,150), chickenTexture)

window.fill((0,0,0))
room.draw((50,50), window)
    
running = True
while running:
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                break
            chicken.move(event)

    room.draw((50,50), window)
    window.blit(chicken.texture, chicken.position, room)
    
    # pygame.draw.rect(window,(0, 140, 140),
    #     (chicken.x,chicken.y,chicken.width,chicken.height))
    
    pygame.display.update()

    # clock.tick(60)
    # time.sleep(1)

pygame.quit()
