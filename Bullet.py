import pygame
import globals
from Entity import Entity

class Bullet(Entity):
    def __init__(self, level, pos_x, pos_y, speed):
        super().__init__(level, 20, 10, pos_x, pos_y, speed, 0, None, 0, 0, 1)
        self.image.fill(globals.BLACK)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed