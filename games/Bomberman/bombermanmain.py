import pygame
import random

from games.Bomberman.enums.power_up_type import PowerUpType
from games.Bomberman.player import Player
from games.Bomberman.explosion import Explosion
from games.Bomberman.enemy import Enemy
from games.Bomberman.enums.algorithm import Algorithm
from games.Bomberman.power_up import PowerUp
from Setting_Initialize import my_font, HEIGHT

scale = int(HEIGHT* 0.035 + 2.5)

enemy_list = []
ene_blocks = []
bombs = []
explosions = []
power_ups = []

GRID_BASE = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
             [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1], 
             [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

font = None
player = None

bomb_window = pygame.Surface((600,400))
screen_return = my_font(12).render("Return", False, (153, 153, 255))
screen_return_rect = screen_return.get_rect(topleft = (20 , 10))

player_alg = Algorithm.PLAYER
en1_alg = Algorithm.DIJKSTRA
en2_alg = Algorithm.DFS
en3_alg = Algorithm.DIJKSTRA

player = Player()

en1 = Enemy(19, 1, en1_alg)
en1.load_animations('1', scale)
enemy_list.append(en1)
ene_blocks.append(en1)

en2 = Enemy(1, 12, en2_alg)
en2.load_animations('2', scale)
enemy_list.append(en2)
ene_blocks.append(en2)

en3 = Enemy(19, 12, en3_alg)
en3.load_animations('3', scale)
enemy_list.append(en3)
ene_blocks.append(en3)

if player_alg is Algorithm.PLAYER:
    player.load_animations(scale)
    ene_blocks.append(player)
elif player_alg is not Algorithm.NONE:
    en0 = Enemy(1, 1, player_alg)
    en0.load_animations('', scale)
    enemy_list.append(en0)
    ene_blocks.append(en0)
    player.life = False
else:
    player.life = False

grass_img = pygame.image.load(r'games\Bomberman\images\terrain\grass.png')
grass_img = pygame.transform.scale(grass_img, (scale, scale))

block_img = pygame.image.load(r'games\Bomberman\images\terrain\block.png')
block_img = pygame.transform.scale(block_img, (scale, scale))

box_img = pygame.image.load(r'games\Bomberman\images\terrain\box.png')
box_img = pygame.transform.scale(box_img, (scale, scale))

bomb1_img = pygame.image.load(r'games\Bomberman\images\bomb\1.png')
bomb1_img = pygame.transform.scale(bomb1_img, (scale, scale))

bomb2_img = pygame.image.load(r'games\Bomberman\images\bomb\2.png')
bomb2_img = pygame.transform.scale(bomb2_img, (scale, scale))

bomb3_img = pygame.image.load(r'games\Bomberman\images\bomb\3.png')
bomb3_img = pygame.transform.scale(bomb3_img, (scale, scale))

explosion1_img = pygame.image.load(r'games\Bomberman\images\explosion\1.png')
explosion1_img = pygame.transform.scale(explosion1_img, (scale, scale))

explosion2_img = pygame.image.load(r'games\Bomberman\images\explosion\2.png')
explosion2_img = pygame.transform.scale(explosion2_img, (scale, scale))

explosion3_img = pygame.image.load(r'games\Bomberman\images\explosion\3.png')
explosion3_img = pygame.transform.scale(explosion3_img, (scale, scale))

terrain_images = [grass_img, block_img, box_img, grass_img]
bomb_images = [bomb1_img, bomb2_img, bomb3_img]
explosion_images = [explosion1_img, explosion2_img, explosion3_img]

power_up_bomb_img = pygame.image.load(r'games\Bomberman\images\power_up\bomb.png')
power_up_bomb_img = pygame.transform.scale(power_up_bomb_img, (scale, scale))

power_up_fire_img = pygame.image.load(r'games\Bomberman\images\power_up\fire.png')
power_up_fire_img = pygame.transform.scale(power_up_fire_img, (scale, scale))

power_ups_images = [power_up_bomb_img, power_up_fire_img]


def generate_map(grid):
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] != 0:
                continue
            elif (i < 3 or i > len(grid) - 4) and (j < 3 or j > len(grid[i]) - 4):
                continue
            if random.randint(0, 9) < 7:
                grid[i][j] = 2
    return

def update_bombs(grid, dt):
    for b in bombs:
        b.update(dt)
        if b.time < 1:
            b.bomber.bomb_limit += 1
            grid[b.pos_x][b.pos_y] = 0
            exp_temp = Explosion(b.pos_x, b.pos_y, b.range)
            exp_temp.explode(grid, bombs, b, power_ups)
            exp_temp.clear_sectors(grid, random, power_ups)
            explosions.append(exp_temp)
    if player not in enemy_list:
        player.check_death(explosions)
    for en in enemy_list:
        en.check_death(explosions)
    for e in explosions:
        e.update(dt)
        if e.time < 1:
            explosions.remove(e)


def bomberman_is_dead():
    if not player.life:
        return True
    for en in enemy_list:
        if en.life:
            return False
    return True

grid = [row[:] for row in GRID_BASE]
generate_map(grid)

running = True
game_ended = False

def display_message():
    global game_ended 
    if game_ended:
        tf = my_font(12).render("Press E to Restart", False, (153, 153, 255))
        bomb_window.blit(tf, (20, 40))
        bomb_window.blit(screen_return, screen_return_rect)  
    if not game_ended:
        game_ended = bomberman_is_dead()

def reset_game():
    global en1_alg, en2_alg, en3_alg, game_ended
    game_ended = False
    generate_map(grid)
    player.pos_x = 4
    player.pos_y = 4
    player.life = True
    player.bomb_limit = 1
    player.range = 3
    player.direction = 0

    for en in enemy_list:
        en.life = True
    enemy_list.clear()
    ene_blocks.clear()
    en1_alg = Algorithm.DIJKSTRA
    en2_alg = Algorithm.DFS
    en3_alg = Algorithm.DIJKSTRA

    en1 = Enemy(19, 1, en1_alg)
    
    en2 = Enemy(1, 12, en2_alg)


    en3 = Enemy(19, 12, en3_alg)

    en1.load_animations('1', scale)
    en2.load_animations('2', scale)
    en3.load_animations('3', scale)

    enemy_list.append(en1)
    enemy_list.append(en2)
    enemy_list.append(en3)
    ene_blocks.append(en1)
    ene_blocks.append(en2)
    ene_blocks.append(en3)
    bombs.clear()
    explosions.clear()
    # clear the power ups list and generate new ones randomly
    power_ups.clear()
    for i in range(3):
        power_ups.append(PowerUp(random.randint(1, len(grid) - 1), random.randint(1, len(grid[0]) - 1), random.choice(list(PowerUpType))))
    
    # create a dummy explosion object with zero range and zero time
    dummy_explosion = Explosion(0, 0, 0)
    dummy_explosion.time = 0
    
    # call the clear_sectors function of the dummy explosion object to break the blocks in the grid
    dummy_explosion.clear_sectors(grid, random, power_ups)


def handle_input():
    for en in enemy_list:
        en.make_move(grid, bombs, explosions, ene_blocks)
    keys = pygame.key.get_pressed()
    temp = player.direction
    if player.life:
        movement = False
        if keys[pygame.K_s]:
            temp = 0
            player.move(0, 1, grid, ene_blocks, power_ups)
            movement = True
        elif keys[pygame.K_d]:
            temp = 1
            player.move(1, 0, grid, ene_blocks, power_ups)
            movement = True
        elif keys[pygame.K_w]:
            temp = 2
            player.move(0, -1, grid, ene_blocks, power_ups)
            movement = True
        elif keys[pygame.K_a]:
            temp = 3
            player.move(-1, 0, grid, ene_blocks, power_ups)
            movement = True
        if keys[pygame.K_q]:
            if player.bomb_limit == 0 or not player.life:
                return 
            temp_bomb = player.plant_bomb(grid)
            bombs.append(temp_bomb)
            grid[temp_bomb.pos_x][temp_bomb.pos_y] = 3
            player.bomb_limit -= 1

        if temp != player.direction:
            player.frame = 0
            player.direction = temp
        if movement:
            if player.frame == 2:
                player.frame = 0
            else:
                player.frame += 1
    else:
        if keys[pygame.K_e]:
            reset_game()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            bomb_window.blit(terrain_images[grid[i][j]], (i * scale, j * scale, scale, scale))

    for pu in power_ups:
        bomb_window.blit(power_ups_images[pu.type.value], (pu.pos_x * scale, pu.pos_y * scale, scale, scale))

    for x in bombs:
        bomb_window.blit(bomb_images[x.frame], (x.pos_x * scale, x.pos_y * scale, scale, scale))

    for y in explosions:
        for x in y.sectors:
            bomb_window.blit(explosion_images[y.frame], (x[0] * scale, x[1] * scale, scale, scale))
    if player.life:
        bomb_window.blit(player.animation[player.direction][player.frame],
               (player.pos_x * (scale / 4), player.pos_y * (scale / 4), scale, scale))
    for en in enemy_list:
        if en.life:
            bomb_window.blit(en.animation[en.direction][en.frame],
                   (en.pos_x * (scale / 4), en.pos_y * (scale / 4), scale, scale))
    
    display_message()



