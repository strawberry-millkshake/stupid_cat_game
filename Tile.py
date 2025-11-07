import pygame
import globals
from Entity import Entity

class Tile(Entity):
    def __init__(self, level, width, height, pos_x, pos_y, speed_x, speed_y, bounce_factor):
        super().__init__(level, width, height, pos_x, pos_y, speed_x, speed_y, None, 0, bounce_factor, 0)
        self.image.fill(globals.BLACK)
    
    def update(self):

        self.entity_update()

        if self.rect.right > globals.SCREEN_WIDTH or self.rect.left < 0:
            self.speed_x *= -1
        
        if self.rect.bottom > globals.SCREEN_HEIGHT or self.rect.top < 0:
            self.speed_y *= -1