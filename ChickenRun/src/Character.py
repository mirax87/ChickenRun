import pygame

class Character():
    # pos: (x, y) - coordinates in pixel
    # size: (x, y) - rectangular size in pixel
    def __init__(self, pos, size, texture = None):
        self.step = 8
        self.x = pos[0]
        self.y = pos[1]
        self.position = pygame.math.Vector2(self.x, self.y)

        self.width = size[0]
        self.height = size[1]
        self.texture = texture