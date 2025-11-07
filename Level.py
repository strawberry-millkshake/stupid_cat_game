import pygame
import globals
from Event_Handler import Event_Handler

class Level():
    def __init__(self, screen, number):
        self.screen = screen
        self.event_handler = Event_Handler(self)
        self.number = number
        self.complete = False
        self.player = None
        self.tile_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.item_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.text_font = pygame.font.SysFont('Arial', 30)
        self.text_array = []
        self.current_text = 0

    def update(self):
        self.tile_group.update()
        self.enemy_group.update()
        self.item_group.update()
        self.bullet_group.update()
        self.event_handler.update()
        self.tile_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.item_group.draw(self.screen)
        self.bullet_group.draw(self.screen)

    def display_text(self):
            text_to_display = self.text_array[self.current_text] 
            text = self.text_font.render(text_to_display[0], False, globals.BLACK)
            text_rect = text.get_rect(center=(text_to_display[1], text_to_display[2]))
            self.screen.blit(text, text_rect)
    
    def add_tile(self, tile):
        self.tile_group.add(tile)
    
    def add_enemy(self, enemy):
        self.enemy_group.add(enemy)

    def add_item(self, item):
        self.item_group.add(item)

    def add_bullet(self, bullet):
        self.bullet_group.add(bullet)

    def add_text(self, text, text_x, text_y):
        self.text_array.append([text, text_x, text_y])
    
    def add_player(self, player):
        self.player = player

    def get_tiles(self):
        return self.tile_group
    
    def get_enemies(self):
        return self.enemy_group
    
    def get_items(self):
        return self.item_group
    
    def get_bullets(self):
        return self.bullet_group