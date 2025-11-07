import pygame

class Hp_Bar(pygame.sprite.Sprite):
    def __init__(self, charecter_width, charecter_x, charecter_y, max_hp):
        super().__init__()

        self.size_x = charecter_width
        self.size_y = 20
        self.image = pygame.Surface([self.size_x, self.size_y])
        self.rect = self.image.get_rect()
        self.rect.x = charecter_x + (charecter_x/2)
        self.rect.y = charecter_y - 20
        self.image.fill((0,0,0))
        self.max_hp = max_hp
        self.scaled_max_hp = 255/self.max_hp
    
    # just do out the math if you need to understand this code. Hopefully you will never need to change this
    def update(self, charecter_size_x, charecter_x, charecter_y, current_hp):
        self.rect.x = charecter_x + (charecter_size_x/2) - (self.size_x/2)
        self.rect.y = charecter_y - 50
        self.image.fill((0,0,0))
        self.image.fill((255-(current_hp*self.scaled_max_hp),
                         current_hp*self.scaled_max_hp,
                         0), self.image.get_rect().inflate(-((self.size_x+5)-(current_hp * (self.size_x/self.max_hp))),-5))


