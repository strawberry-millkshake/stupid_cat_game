import pygame
import globals
from Charecter import Charecter

class Enemy(Charecter):
    def __init__(self, level, pos_x, pos_y, speed_x, enemy_file_name):
        super().__init__(level, 100,100, pos_x, pos_y, speed_x, 0, enemy_file_name, 0, 1, 2, 5, "right")

    def update(self):
        self.entity_update()
        is_colliding = self.charecter_update()

        if is_colliding and self.cur_dir == "left":
            self.stop()
            self.update_speed("right")
        elif is_colliding and self.cur_dir == "right":
            self.stop()
            self.update_speed("left")

        self.bullet_collide()