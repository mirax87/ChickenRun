import pygame
import pytmx


class Room:

    def __init__(self, map_path):
        super().__init__()
        self.curMap = pytmx.util_pygame.load_pygame(map_path)

    def get_layer_tiles(self, layer):
        try:
            return self.curMap.get_layer_by_name(layer).tiles()
        except:
            raise "Layer not found"
        
    def update(self):
        pass