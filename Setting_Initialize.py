import pygame
import os
import cv2
from win32api import GetSystemMetrics
pygame.init()
#RBG Color
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)
MINT_CREAM = pygame.Color(245,255,250)

#Import Font
def my_font(size):
    return pygame.font.Font("SuperLegendBoy.ttf", size)

#System Screen
WIDTH = GetSystemMetrics(0) 
HEIGHT = GetSystemMetrics(1) 

#Information Setup
clock = pygame.time.Clock()
display_info = pygame.display.Info()
DISPLAY_WIDTH = display_info.current_w
DISPLAY_HEIGHT = display_info.current_h

#Initial Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Camera Setup
capture = cv2.VideoCapture(0)
cam_pos = (480,30)

#App GUI Setup
pygame.display.set_caption('ASL')
font = pygame.font.SysFont("Arial", 24)
bg = pygame.image.load("image\wallpaper.jpg")
bg = pygame.transform.smoothscale(bg,(SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pygame.image.load("image\icon.ico")
pygame.display.set_icon(icon)

#Image Handle
cwd = os.getcwd()
image_folder = os.path.join(cwd, "image")
images = [os.path.join(image_folder, images) for images in os.listdir(image_folder) if images.endswith(".png") or images.endswith(".jpg")]
images_dict = {}
for image in images:
    name = os.path.splitext(os.path.basename(image))[0]
    images_dict[name] = pygame.image.load(image)
    

selected_menu_rect = pygame.Rect(DISPLAY_WIDTH - 1000, DISPLAY_HEIGHT-600, 600, 400) 
game_select_button_rect = images_dict['game'].get_rect(center=(SCREEN_WIDTH - 700, SCREEN_HEIGHT - 100))
Instruction = images_dict['Instruction'].get_rect(topleft = (game_select_button_rect.left, SCREEN_HEIGHT - 10))

W_rect = images_dict['w'].get_rect(center=(200, 100))
Q_rect = images_dict['q'].get_rect(center=(W_rect.centerx - 100, W_rect.centery))
E_rect = images_dict['e'].get_rect(center=(W_rect.centerx + 100, W_rect.centery))
A_rect = images_dict['A'].get_rect(center=(W_rect.centerx - 100, W_rect.centery + 100)) 
S_rect = images_dict['s'].get_rect(center=(W_rect.centerx, W_rect.centery + 100)) 
D_rect = images_dict['d'].get_rect(center=(W_rect.centerx + 100, W_rect.centery + 100)) 

A_instruct = pygame.image.load(r"train_data\A\1.jpg")
S_instruct = pygame.image.load(r"train_data\S\1.jpg")
D_instruct = pygame.image.load(r"train_data\D\1.jpg")
W_instruct = pygame.image.load(r"train_data\W\1.jpg")
Q_instruct = pygame.image.load(r"train_data\Q\1.jpg")
E_instruct = pygame.image.load(r"train_data\E\1.jpg")

A_instruct_rect =  A_instruct.get_rect(center=(selected_menu_rect.centerx + 130, selected_menu_rect.bottom - 150)) 
S_instruct_rect =  S_instruct.get_rect(center=(selected_menu_rect.centerx, selected_menu_rect.bottom - 150)) 
D_instruct_rect =  D_instruct.get_rect(center=(selected_menu_rect.centerx - 130, selected_menu_rect.bottom - 150)) 
Q_instruct_rect =  Q_instruct.get_rect(center=(selected_menu_rect.centerx + 130, selected_menu_rect.bottom - 300)) 
W_instruct_rect =  W_instruct.get_rect(center=(selected_menu_rect.centerx, selected_menu_rect.bottom - 300)) 
E_instruct_rect =  E_instruct.get_rect(center=(selected_menu_rect.centerx -130, selected_menu_rect.bottom - 300)) 

A_instruct_text = my_font(13).render("A", True, WHITE)
S_instruct_text = my_font(13).render("S", True, WHITE)
D_instruct_text = my_font(13).render("D", True, WHITE)
Q_instruct_text = my_font(13).render("Q", True, WHITE)
W_instruct_text = my_font(13).render("W", True, WHITE)
E_instruct_text = my_font(13).render("E", True, WHITE)

A_instruct_text_rect = A_instruct_text.get_rect(center = (A_instruct_rect.centerx, A_instruct_rect.bottom + 20))
S_instruct_text_rect = S_instruct_text.get_rect(center = (S_instruct_rect.centerx, S_instruct_rect.bottom + 20))
D_instruct_text_rect = D_instruct_text.get_rect(center = (D_instruct_rect.centerx, D_instruct_rect.bottom + 20))
Q_instruct_text_rect = Q_instruct_text.get_rect(center = (Q_instruct_rect.centerx, Q_instruct_rect.bottom + 20))
W_instruct_text_rect = W_instruct_text.get_rect(center = (W_instruct_rect.centerx, W_instruct_rect.bottom + 20))
E_instruct_text_rect = E_instruct_text.get_rect(center = (E_instruct_rect.centerx, E_instruct_rect.bottom + 20))

snake_text = my_font(32).render("Snake", True, WHITE)
bomberman_text = my_font(32).render("Bomberman", True, WHITE)
bomberman_rect = bomberman_text.get_rect(center=(selected_menu_rect.centerx, selected_menu_rect.centery - 40)) 
snake_rect = snake_text.get_rect(center=(selected_menu_rect.centerx, selected_menu_rect.centery + 80)) 

#Switching Affect Setup
game_select_button = False
Instruction_button = False
bomberman_state = False
snake_state = False
running = True

