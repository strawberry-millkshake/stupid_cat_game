# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SETUP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pygame
import globals
from Player import Player
from Enemy import Enemy
from Tile import Tile
from Cookie import Cookie
from Flag import Flag
from Level import Level

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
clock = pygame.time.Clock()
text_font = pygame.font.SysFont('Arial', 30)
running = True

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MAKE OUR LEVELS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

level_0 = Level(screen,0)
level_0.add_tile(Tile(level_0, 50, globals.SCREEN_HEIGHT, globals.SCREEN_LEFT, globals.SCREEN_TOP, 0, 0, 0))
level_0.add_tile(Tile(level_0, 50, globals.SCREEN_HEIGHT, globals.SCREEN_RIGHT-50, globals.SCREEN_TOP, 0, 0, 0))
level_0.add_tile(Tile(level_0, globals.SCREEN_WIDTH, 50, globals.SCREEN_LEFT, globals.SCREEN_TOP, 0, 0, 0))
level_0.add_item(Flag(level_0, 1400, globals.SCREEN_BOTTOM))
level_0.add_text("Get the flag!", globals.SCREEN_WIDTH/2, globals.SCREEN_HEIGHT/2)

level_1 = Level(screen,1)
level_1.add_tile(Tile(level_1, 50, globals.SCREEN_HEIGHT, globals.SCREEN_LEFT, globals.SCREEN_TOP, 0, 0, 1))
level_1.add_tile(Tile(level_1, 50, globals.SCREEN_HEIGHT, globals.SCREEN_RIGHT-50, globals.SCREEN_TOP, 0, 0, 1))
level_1.add_tile(Tile(level_1, globals.SCREEN_WIDTH, 50, globals.SCREEN_LEFT, globals.SCREEN_TOP, 0, 0, 1))
level_1.add_tile(Tile(level_1, 200, 50, 200, 600, 5, 0, 0))
level_1.add_tile(Tile(level_1, 200, 50, 200, 200, -5, 0, 0))
level_1.add_item(Flag(level_1, 300, 150))
level_1.add_text("This one should be obvious", globals.SCREEN_LEFT + 300, globals.SCREEN_BOTTOM - 50)

level_2 = Level(screen,2)
level_2.add_tile(Tile(level_2, 50, globals.SCREEN_HEIGHT, globals.SCREEN_LEFT, globals.SCREEN_TOP, 0, 0, 1))
level_2.add_tile(Tile(level_2, 50, globals.SCREEN_HEIGHT, globals.SCREEN_RIGHT-50, globals.SCREEN_TOP, 0, 0, 1))
level_2.add_tile(Tile(level_2, globals.SCREEN_WIDTH, 50, globals.SCREEN_LEFT, globals.SCREEN_TOP, 0, 0, 1))
level_2.add_enemy(Enemy(level_2, 300, globals.SCREEN_HEIGHT-100, 2, "sprites/hitler.png"))
level_2.add_item(Cookie(level_2, 200,globals.SCREEN_BOTTOM-50))
level_2.add_item(Flag(level_2, 100, globals.SCREEN_BOTTOM-50))
level_2.add_text("Kill Hitler", globals.SCREEN_WIDTH/2, globals.SCREEN_TOP + 200)

level_3 = Level(screen,3)
level_3.add_tile(Tile(level_3, 50, globals.SCREEN_HEIGHT, 500, globals.SCREEN_TOP, 0, 0, 1))
level_3.add_tile(Tile(level_3, 50, globals.SCREEN_HEIGHT, 1000, globals.SCREEN_TOP, 0, 0, 1))
level_3.add_tile(Tile(level_3, globals.SCREEN_WIDTH, 50, globals.SCREEN_LEFT, globals.SCREEN_TOP, 0, 0, 1))
level_3.add_item(Flag(level_3, 750, 100))
level_3.add_text("This cat is mad bouncy", globals.SCREEN_LEFT+250, globals.SCREEN_HEIGHT/2)

level_4 = Level(screen,4)
level_4.add_text("I gotta add more levels", globals.SCREEN_WIDTH/2, globals.SCREEN_HEIGHT/2)

levels = []
levels.append(level_0)
levels.append(level_1)
levels.append(level_2)
levels.append(level_3)
levels.append(level_4)
current_level = 0

#make the player, give it access to the level
player = Player(levels[current_level], "right")
player_list = pygame.sprite.Group()
player_list.add(player)

#give each level direct access to the player object
for i in range(len(levels)):
    levels[i].add_player(player)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GAME LOOP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while running:

    #Keyboard input section
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
            if event.key == pygame.K_a:
                player.update_speed("left")
            if event.key == pygame.K_d:
                player.update_speed("right")
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player.stop()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for player_from_group in player_list:
                player_from_group.shoot()

    #update all our entites
    player_list.draw(screen)
    player_list.update()
    levels[current_level].update()
    levels[current_level].display_text()

    #move to next level
    if levels[current_level].complete == True:
        screen.fill("white")
        current_level += 1
        #break while true loop if we are at the end of the game
        if current_level == len(levels):
            break
        text = text_font.render('Level Complete!', False, globals.BLACK)
        text_rect = text.get_rect(center=(globals.SCREEN_WIDTH/2, globals.SCREEN_HEIGHT/2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(500)
        player.level = levels[current_level]
        player.reset(globals.SCREEN_WIDTH/2, globals.SCREEN_HEIGHT/2)
    
    #update our game
    pygame.display.flip()
    screen.fill("white")
    clock.tick(60)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ WHEN WE QUIT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pygame.quit()