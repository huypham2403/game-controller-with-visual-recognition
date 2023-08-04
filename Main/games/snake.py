import pygame, random
from Setting_Initialize import* 
pygame.init()

# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_pos = [random.randrange(1, (600//10)) * 10, random.randrange(1, (400//10)) * 10]
food_spawn = True

score = 0


snake_window = pygame.Surface((600, 400))

restart = my_font(32).render("Press E to restart", True, (255, 255, 255))
lose = my_font(32).render("Lose", True, (255, 255, 255))
screen_return = my_font(23).render("Return", True, (255, 255, 255))
selected_menu_rect = pygame.Rect(0,0, 600, 400) 
screen_return_rect = screen_return.get_rect(topleft = (20 , 10))

def game_over():
    pygame.draw.rect(snake_window, BLACK, selected_menu_rect)
    snake_window.blit(restart, (80,200))
    snake_window.blit(lose, (250,100))
    snake_window.blit(screen_return, screen_return_rect)
    show_score(0, RED)

# Score
def show_score(choice, color):
    score_surface = my_font(size = 18).render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (600/10, 15)
    else:
        score_rect.midtop = (600/2, 400/1.25)
    snake_window.blit(score_surface, score_rect)

def is_dead():
    if snake_pos[0] < 0 or snake_pos[0] > 600-10:
        return True
    if snake_pos[1] < 0 or snake_pos[1] > 400-10:
        return True
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            return True
    return False

def snake_easter(change_to): 
    global direction, food_pos, food_spawn, score 
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()
    if not food_spawn:
        food_pos = [random.randrange(1, (600//10)) * 10, random.randrange(1, (400//10)) * 10]
    food_spawn = True
    snake_window.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(snake_window, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(snake_window, WHITE, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    show_score(1, WHITE)

def reset():
    global snake_pos, snake_body, food_pos, food_spawn, score, change_to
    snake_pos = [100, 50]
    snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
    food_pos = [random.randrange(1, (600//10)) * 10, random.randrange(1, (400//10)) * 10]
    food_spawn = True
    direction = 'RIGHT'
    change_to = direction
    score = 0

direction = 'RIGHT'
change_to = direction
SNAKE_UPDATE = pygame.USEREVENT + 1
pygame.time.set_timer(SNAKE_UPDATE, 200)

def keyboard():
    global change_to
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        change_to = 'DOWN'
    if keys[pygame.K_d]:
        change_to = 'RIGHT'
    if keys[pygame.K_w]:
        change_to = 'UP'
    if keys[pygame.K_a]:
        change_to = 'LEFT'          
    if keys[pygame.K_e] and is_dead():
        reset()
