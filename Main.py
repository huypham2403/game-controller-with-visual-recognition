import pygame
from pygame.locals import *
from games import snake
from Setting_Initialize import*
from games.Bomberman.bombermanmain import*
from radio import*
from Preprocess_Image import*
from Keycap_Simulation import*
import threading, queue,time
def load_and_play_song(index):
    global music_pos
    pygame.mixer.music.load(songs[index])
    music_pos = 0
    if music_play_button_clicked:
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.stop()
music_pos = 0

label_queue = queue.Queue()
def keyboard_input():
    global running
    while running:
        label = label_queue.get()
        if label is not None:
            PressKey(key_dict[label])
            time.sleep(1) 
            ReleaseKey(key_dict[label])
        label_queue.task_done()

# Create a thread for the keyboard input and start it
keyboard_thread = threading.Thread(target=keyboard_input)
keyboard_thread.start()

def draw_letter(letter):
    image, rect = buttons[letter]
    screen.blit(image, rect)
    box_rect = rect.inflate(10, 10) 
    pygame.draw.rect(screen, (192,192,192), box_rect) 
    screen.blit(image, rect)
    

#Snake Setup
screen_return_rect = snake.screen_return.get_rect(topleft = (DISPLAY_WIDTH - 1000 + 10 , DISPLAY_HEIGHT - 600 + 15))
capture = cv2.VideoCapture(0)
rect_update = RectUpdate(SCREEN_WIDTH, SCREEN_HEIGHT)
cam_pos = (480,30)

while running:
    dt = clock.tick(FPS)
    _, camera_image = capture.read()
    camera_image = cv2.flip(camera_image, 1)
    camera_image = cv2.resize(camera_image, (300, 300))
    cv2.rectangle(camera_image, (160, 160), (290,290), (25, 25, 25), 2)
    camera_surf = pygame.image.frombuffer(camera_image.tobytes(), (camera_image.shape[1::-1]), "BGR")
    label = detect(camera_image)
    screen.blit(bg, (0, 0))  
    screen.blit(camera_surf,cam_pos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False      
        elif event.type == snake.SNAKE_UPDATE:
            if snake_state:
                snake.snake_easter(snake.change_to) 
                if snake.is_dead():
                    snake.game_over()
            else: 
                snake.reset()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if game_select_button_rect.collidepoint(mouse_x, mouse_y):
                snake_state = not snake_state if snake_state else snake_state
                bomberman_state = not bomberman_state if bomberman_state else bomberman_state
                game_select_button = not game_select_button
                if game_select_button:                 
                    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), FULLSCREEN)
                    bg = pygame.transform.smoothscale(bg,(DISPLAY_WIDTH, DISPLAY_HEIGHT))
                    SCREEN_WIDTH = DISPLAY_WIDTH
                    SCREEN_HEIGHT = DISPLAY_HEIGHT
                    rect_update.update_rect(selected_menu_rect.left + 450 + 100, selected_menu_rect.bottom + 170)
                    cam_pos = (SCREEN_WIDTH - 350,30)
                    rect_update.update_song_name(current_song)
                else:
                    SCREEN_WIDTH = 800
                    SCREEN_HEIGHT = 600
                    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), RESIZABLE)
                    rect_update.update_rect(SCREEN_WIDTH, SCREEN_HEIGHT)
                    cam_pos = (480,30)
                    rect_update.update_song_name(current_song)
            if Instruction.collidepoint(mouse_x, mouse_y):
                Instruction_button = not Instruction_button
            if snake_rect.collidepoint(mouse_x, mouse_y) and snake_state == False:
                snake_state = True
            if bomberman_rect.collidepoint(mouse_x, mouse_y) and bomberman_state == False:
                bomberman_state = True
            if screen_return_rect.collidepoint(mouse_x, mouse_y):
                if snake.is_dead() or bomberman_is_dead():
                    snake_state = False
                    bomberman_state = False
            if  rect_update.music_play_rect.collidepoint(mouse_x, mouse_y):
                music_play_button_clicked = not music_play_button_clicked
                if music_play_button_clicked:
                    images_dict['play'] = images_dict['pause']
                    speed = 1
                    pygame.mixer.music.play(start=music_pos/1000)
                else: 
                    speed = 0
                    images_dict['play'] = pygame.image.load('image\play.png')
                    pygame.mixer.music.pause()
                    music_pos += pygame.mixer.music.get_pos()
            if rect_update.prev_rect.collidepoint(mouse_x, mouse_y):
                rect_update.update_song_name((rect_update.song_index - 1) % len(songs))
                load_and_play_song(rect_update.song_index)
            if rect_update.next_rect.collidepoint(mouse_x, mouse_y):
                rect_update.update_song_name((rect_update.song_index + 1) % len(songs))
                load_and_play_song(rect_update.song_index)    
    if pygame.mixer.music.get_busy():
        music_pos += dt
        music_pos = min(max(music_pos, 0), rect_update.song_length)
        if music_pos == rect_update.song_length:
            music_pos = 0
            pygame.mixer.music.stop()
            music_play_button_clicked = False
            images_dict['play'] = pygame.image.load("image\play.png")
        rect_update.procress_bar(music_pos)
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:
            try:
                if rect_update.full_bar_rect.left <= mouse_x <= rect_update.full_bar_rect.left+400 and \
                rect_update.full_bar_rect.top <= mouse_y <= rect_update.full_bar_rect.top+20:
                    new_music_ratio = (mouse_x - rect_update.full_bar_rect.left) / 400
                    music_pos = new_music_ratio * rect_update.song_length
                    if music_play_button_clicked:
                        pygame.mixer.music.set_pos(new_music_ratio * rect_update.song_length / 1000)        
            except:
                continue
    border_width = 2 
    pygame.draw.rect(screen, BLACK, rect_update.full_bar_rect, border_width)
    pygame.draw.rect(screen, BLUE,rect_update.bar_rect)
    music_time_count_gui = music_format(music_pos)
    music_length_gui = music_format(rect_update.song_length)
    
    rect_update.moving_world(speed)
    buttons = {"W": (images_dict['w'], W_rect),
               "Q": (images_dict['q'], Q_rect),
               "E":(images_dict['e'], E_rect),
               "A":(images_dict['A'], A_rect),
               "S":(images_dict['s'], S_rect),
               "D":(images_dict['d'], D_rect),
               "music_play":(images_dict['play'], rect_update.music_play_rect),
               "prev":(images_dict['prev'], rect_update.prev_rect),
               "next":(images_dict['next'], rect_update.next_rect),
               "game_selected_button":(images_dict['game'], game_select_button_rect),
               "song_name":(rect_update.name_songs_gui, rect_update.name_songs_rect),
               "song_length":(music_length_gui, rect_update.music_length_rect),
               "music_time_count":(music_time_count_gui, rect_update.music_time_count_rect)}
    
    for _, value in buttons.items():
        image, rect = value
        screen.blit(image, rect)    
    if game_select_button == True:
        pygame.draw.rect(screen, BLACK, selected_menu_rect)
        screen.blit(snake_text, snake_rect)
        screen.blit(bomberman_text, bomberman_rect)
        screen.blit(images_dict['Instruction'], Instruction)
        if snake_state:
            snake.keyboard()
            screen.blit(snake.snake_window,(selected_menu_rect.left,selected_menu_rect.top))
            pygame.display.flip()      
        if bomberman_state:
            update_bombs(grid, dt)
            handle_input()  
            screen.blit(bomb_window, (selected_menu_rect.left,selected_menu_rect.top))    
        if Instruction_button:
            pygame.draw.rect(screen, BLACK, selected_menu_rect)
            instruct_guide = {"A":(A_instruct, A_instruct_rect),
                              "S":(S_instruct, S_instruct_rect),
                              "D":(D_instruct, D_instruct_rect),
                              "W":(W_instruct, W_instruct_rect),
                              "Q":(Q_instruct, Q_instruct_rect),
                              "E":(E_instruct, E_instruct_rect),
                              "A_text":(A_instruct_text, A_instruct_text_rect),
                              "S_text":(S_instruct_text, S_instruct_text_rect),
                              "D_text":(D_instruct_text, D_instruct_text_rect),
                              "Q_text":(Q_instruct_text, Q_instruct_text_rect),
                              "W_text":(W_instruct_text, W_instruct_text_rect),
                              "E_text":(E_instruct_text, E_instruct_text_rect)}
            for _, value in instruct_guide.items():
                image, rect = value
                screen.blit(image, rect)    
    if label != None:
        draw_letter(label)
        label_queue.put(label)
    pygame.display.flip()
pygame.quit()
keyboard_thread.join()