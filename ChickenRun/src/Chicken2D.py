import pygame
import os


class Chicken2D(pygame.sprite.Sprite):

    def __init__(self, position = None):
        super().__init__()

        self.step = 6

        self.image = pygame.image.load(
            os.path.join("ChickenRun", "assets", "chicken",
                         "chicken", "chickenprofilewalkx4.gif"))\
            .convert_alpha()
        
        self.rect = self.image.get_rect(center = (50, 50))

    def spawn(self, pos):
        # Problem: chicken already shown...
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

    def move(self, pygame_keys):
        if pygame_keys[pygame.K_LEFT] or pygame_keys[pygame.K_a]:
            self.rect.centerx -= self.step
        if pygame_keys[pygame.K_RIGHT] or pygame_keys[pygame.K_d]:
            self.rect.centerx += self.step
        if pygame_keys[pygame.K_UP] or pygame_keys[pygame.K_w]:
            self.rect.centery -= self.step
        if pygame_keys[pygame.K_DOWN] or pygame_keys[pygame.K_s]:
            self.rect.centery += self.step
    
    def interact(self, pygame_keys, interactable):
        if pygame_keys[pygame.K_e]:
    	    if pygame.sprite.spritecollide(self, interactable, False):
                print(interactable.sprites)
                print('interaction triggered')

    def update(self, interactable = None):
        keys = pygame.key.get_pressed()
        self.move(keys)
        if interactable:
            self.interact(keys, interactable)
