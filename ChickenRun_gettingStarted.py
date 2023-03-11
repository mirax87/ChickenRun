import os
import pygame
import pytmx
import sys


from ChickenRun.src.Chicken2D import Chicken2D
from ChickenRun.src.LoadLevelCommand import LoadLevelCommand


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)

def collision_sprite(chicken, obstacles):
	if pygame.sprite.spritecollide(chicken, obstacles, False):
		return True
	else: 
		return False

from ChickenRun.src.Rooms import Room

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

screen = pygame.display.set_mode((256*2, 256*2))
clock = pygame.time.Clock()

# Maps: store multiple paths, load on demand.
map_path = os.path.join('ChickenRun', 'Maps', 'Test_map1.tmx')
tmx_data = pytmx.util_pygame.load_pygame(map_path)

tiledim = [tmx_data.tilewidth, tmx_data.tileheight]


groundTiles = pygame.sprite.Group()

for x, y, surf in tmx_data.get_layer_by_name('ground').tiles():
    pos = x * tiledim[0], y * tiledim[1]
    Tile(pos, surf, groundTiles)


exitTiles = pygame.sprite.Group()

for x, y, surf in tmx_data.get_layer_by_name('exits').tiles():
    pos = x * tiledim[0], y * tiledim[1]
    Tile(pos, surf, exitTiles)

chicken2d_sprite = Chicken2D()
chicken2d_sprite.spawn((100, 100))
chicken = pygame.sprite.GroupSingle(chicken2d_sprite)

running = True
while running:
    # global event loop
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                break

    # Create the World
    groundTiles.draw(screen)
    exitTiles.draw(screen)

    # create Chicken
    if collision_sprite(chicken.sprite, exitTiles):
        chicken.update(exitTiles)
    else:
        chicken.update()

    chicken.draw(screen)

    # chicken.colliderect(exitTiles)
    pygame.display.update()

    
         

    clock.tick(60)
    
pygame.quit()
