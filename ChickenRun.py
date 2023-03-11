import pygame
import sys
from ChickenRun.src.Chicken2D import Chicken2D
from ChickenRun.src.LoadLevelCommand import LoadLevelCommand

WIDTH= 1280
HEIGHT= 740
FPS = 60
TILESIZE = 64

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chicken Run")
        self.clock = pygame.time.Clock()

    def run(self):
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
            clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()