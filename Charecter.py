import pygame
import globals
from Entity import Entity
from Bullet import Bullet
from Hp_Bar import Hp_Bar

class Charecter(Entity):
    def __init__(self, level, width, height, pos_x, pos_y, speed_x, speed_y, sprite, friction_factor, bounce_factor, charecter_speed, hp, starting_direction):
        super().__init__(level, width, height, pos_x, pos_y, speed_x, speed_y, sprite, friction_factor, bounce_factor, 1)

        self.cur_dir = starting_direction
        self.charecter_speed = charecter_speed
        if self.cur_dir == "right":
            self.image.fill(globals.TRANSPARENT)
            self.image.blit(pygame.transform.flip(self.rescaled_image, True, False), (0,0))
        if self.cur_dir == "left":
            self.image.fill(globals.TRANSPARENT)
            self.image.blit(self.rescaled_image, (0,0))
        self.max_hp = hp
        self.hp = hp
        self.hp_bar = Hp_Bar(self.width, self.rect.x, self.rect.y, hp)
        self.hp_bar_group = pygame.sprite.Group(self.hp_bar)
        

    def charecter_update(self):
        self.entity_update()
        is_colliding = self.collision_physics()
        if self.hp <= 0:
            self.level.event_handler.throw_event("charecter killed")
            self.hp_bar.kill()
            self.kill()
        self.hp_bar.update(self.width, self.rect.x, self.rect.y, self.hp)
        self.hp_bar_group.draw(self.level.screen)

        return is_colliding

    def update_speed(self, direction):
        self.is_friction_on = False
        self.image.fill(globals.TRANSPARENT)
        if direction == "left":
            self.speed_x = -self.charecter_speed
            self.image.blit(self.rescaled_image, (0,0))
            self.cur_dir = "left"
        elif direction == "right":
            self.speed_x = self.charecter_speed
            self.image.blit(pygame.transform.flip(self.rescaled_image, True, False), (0,0))
            self.cur_dir = "right"

    # instead of setting speed to zero we just turn friction on so the charecters slide around a bit
    def stop(self):
        self.is_friction_on = True

    # TODO: make differnt kinds of guns
    def shoot(self):
        if self.cur_dir == "left":
            self.level.add_bullet(Bullet(self.level, self.rect.x, self.rect.y + self.height/2, -20))
        elif self.cur_dir == "right":
            self.level.add_bullet(Bullet(self.level, self.rect.x + self.width, self.rect.y + self.height/2, 20))

    def bullet_collide(self):
        bullet_hit_list = pygame.sprite.spritecollide(self, self.level.get_bullets(), False)
        if len(bullet_hit_list) > 0:
            self.hp -= 1
        for bullet in bullet_hit_list:
            bullet.kill()