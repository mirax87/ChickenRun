import pygame

from ChickenRun.src.Character import Character

class Chicken(Character):

    def move(self, pygame_keyevent):
        if pygame_keyevent.key in [pygame.K_LEFT, pygame.K_a]:
            self.x-=self.step
        elif pygame_keyevent.key in [pygame.K_RIGHT, pygame.K_d]:
            self.x+=self.step
        elif pygame_keyevent.key in [pygame.K_UP, pygame.K_w]:
            self.y-=self.step
        elif pygame_keyevent.key in [pygame.K_DOWN, pygame.K_s]:
            self.y+=self.step
        self.position = (self.x, self.y)