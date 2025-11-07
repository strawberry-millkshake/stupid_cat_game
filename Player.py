import pygame
import globals
from Charecter import Charecter

class Player(Charecter):

    def __init__(self, level, starting_direction):
        super().__init__(level, 75, 75, globals.SCREEN_WIDTH/2, globals.SCREEN_HEIGHT/2, 0, 0, "sprites/hello_kitty.png", 1.1, 1, 10, 10, starting_direction)
        self.jump_count = 0
    
    def update(self):
        self.charecter_update()
        enemy_hit_list = pygame.sprite.spritecollide(self,self.level.get_enemies(),False)
        item_hit_list = pygame.sprite.spritecollide(self,self.level.get_items(),False)

        for enemy in enemy_hit_list:
            self.hp -= 1
            self.bump(enemy, 20, 20)
        
        for item in item_hit_list:
            if item.type == "cookie":
                self.hp = self.max_hp
                item.kill()
            elif item.type == "flag":
                self.level.complete = True
    
    def reset(self, spawn_x, spawn_y):
        self.hp = self.max_hp
        self.rect.x = spawn_x
        self.rect.y = spawn_y
        self.speed_x = 0
        self.speed_y = 0

    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.get_tiles(), False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= globals.SCREEN_HEIGHT:
            self.speed_y = -15
            self.jump_count += 1
        
        elif self.jump_count == 1:
            self.speed_y = -25
            self.jump_count += 1

        if self.jump_count > 1:
            self.jump_count = 0
    