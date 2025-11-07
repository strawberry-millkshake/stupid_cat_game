import globals
import pygame
import numpy as np

class Entity(pygame.sprite.Sprite):
    def __init__(self, level, width, height, pos_x, pos_y, speed_x, speed_y, sprite, friction_factor, bounce_factor, mass):
        super().__init__()

        self.level = level
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        # current_friction is different from friction_factor so that we can
        # reduce friction temporarily (such as in bounce) and then return it to its normal level
        self.friction_factor = friction_factor
        self.current_friction = self.friction_factor
        self.bounce_factor = bounce_factor
        self.is_bumped = False
        self.is_friction_on = True
        self.mass = mass

        if sprite != None:
            picture_from_the_internet = pygame.image.load(sprite)
            self.rescaled_image = pygame.transform.scale(picture_from_the_internet, (self.width,self.height))
            self.image.set_colorkey(globals.BLACK)
            self.image.blit(self.rescaled_image, (0,0))

    def entity_update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.current_friction < self.friction_factor:
            self.current_friction += (self.friction_factor-self.current_friction)/8

    def collision_physics(self):
        self.rect.y += 1
        block_hit_list = pygame.sprite.spritecollide(self, self.level.get_tiles(), False)
        self.rect.y -= 1
        if len(block_hit_list) > 0:
            #call friction if we're colliding with a Tile
            self.friction()

            #Figure out exactly where we are on the block
            for block in block_hit_list:
                
                collide_x_center = False
                collide_y_top = False
                collide_y_bottom = False
                
                if self.rect.center[0] > block.rect.left and self.rect.center[0] < block.rect.right:
                    collide_x_center = True
                if self.rect.bottom >= block.rect.top and self.rect.bottom <= block.rect.bottom:
                    collide_y_top = True
                if self.rect.top >= block.rect.top and self.rect.top <= block.rect.bottom:
                    collide_y_bottom = True

                # If our x position isn't in the bounds of the tile, just bounce us. Used for walls.
                if not collide_x_center:
                    self.speed_bump(block,1.1,-1.1)
                    self.gravity()

                #if we're on top of the block, add friction, turn off gravity, and set our y speed to 0
                elif collide_y_top:
                    self.rect.bottom = block.rect.top + 1
                    self.speed_y = 0
                    self.friction()
                    self.rect.x += block.speed_x
                
                #if we're on the bottom of the block set y speed to 0 and apply gravity
                elif collide_y_bottom:
                    self.rect.top = block.rect.bottom
                    self.speed_y = 0
                    self.gravity()

                #just to deal with any weird cases where everything else fails. Should never get to this else statment.
                else:
                    self.gravity()

            # returns true if we're colliding with a block, used by some charecters to react to a collision (see Enemy code)
            return True

        elif self.rect.bottom >= globals.SCREEN_HEIGHT:
            self.friction()
            self.speed_y = 0
            self.rect.bottom = globals.SCREEN_HEIGHT
            return False
        else:
            self.gravity()
            return False

    def gravity(self):
        if self.speed_y == 0:
            self.speed_y = 1 * self.mass
        else:
            self.speed_y += 0.7 * self.mass

        if self.rect.y >= globals.SCREEN_HEIGHT - self.rect.height and self.speed_y >= 0:
            self.speed_y = 0
            self.rect.y = globals.SCREEN_HEIGHT - self.rect.height

    def friction(self):
        if self.is_friction_on and self.current_friction != 0:
            self.speed_x /= self.current_friction
    
    # bump sets the speed to:
    # the normal of the distance between the two objects times the bump ammount times the two entites bounce factors
    def bump(self, colided_entity, bump_ammount_x, bump_ammount_y):
        self.current_friction = 1 + ((self.friction_factor-1)/8)
        self.speed_x = np.sign(self.rect.x - colided_entity.rect.x) * bump_ammount_x * (colided_entity.bounce_factor * self.bounce_factor)
        self.speed_y = np.sign(self.rect.y - colided_entity.rect.y) * bump_ammount_y * (colided_entity.bounce_factor * self.bounce_factor)
    
    # same as bump but multiplies bump ammount by speed. This is used for walls where you can build momentum
    def speed_bump(self, colided_entity, bump_ammount_x, bump_ammount_y):
        self.current_friction = 1 + ((self.friction_factor-1)/8)
        self.speed_x = np.sign(self.rect.x - colided_entity.rect.x) * bump_ammount_x * (1+abs(self.speed_x)) * (colided_entity.bounce_factor * self.bounce_factor)
        self.speed_y = np.sign(self.rect.y - colided_entity.rect.y) * bump_ammount_y * (1+abs(self.speed_y)) * (colided_entity.bounce_factor * self.bounce_factor)