import pygame

class Room(pygame.Rect):
    def __init__(self, sqHeight, n_width, n_height):
        self.width = sqHeight * n_width
        self.height = sqHeight * n_height
        self.bg_rgb = (64,12,12)
    
    # Add Obstacles (and sprites)
    def create(self):
        pass

    def draw(self, position, window):
        pygame.draw.rect(window, self.bg_rgb, (position[0],position[1],self.width,self.height))


    