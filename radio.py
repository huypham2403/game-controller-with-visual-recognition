from Setting_Initialize import*


#Take Songs
current_song = 0
songs_folder = os.path.join(cwd, "songs")
songs = [os.path.join(songs_folder, song) for song in os.listdir(songs_folder) if song.endswith(".mp3")]
pygame.mixer.music.load(songs[current_song])
music_length = [pygame.mixer.Sound(songs[song_index]).get_length() * 1000 for song_index in range(len(songs))] 

music_play_button_clicked = False
speed = 0

#Position of radio
class RectUpdate():
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, song_index = 0):
        self.assign_rect(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.assign_song_name(song_index)
        self.procress_bar(2)

    def assign_rect(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.full_bar_rect = pygame.Rect(SCREEN_WIDTH - 450, SCREEN_HEIGHT - 150, 400, 20) 
        self.music_play_rect = images_dict['play'].get_rect(center = (self.full_bar_rect.centerx, self.full_bar_rect.bottom + 40))
        self.prev_rect = images_dict['prev'].get_rect(center=(self.music_play_rect.left - 30, self.music_play_rect.centery))
        self.next_rect = images_dict['next'].get_rect(center=(self.music_play_rect.right + 30, self.music_play_rect.centery))
        self.music_time_count_rect = pygame.Rect(self.full_bar_rect.left - 10, self.full_bar_rect.bottom + 10, 100, 50)
        self.music_length_rect = pygame.Rect(self.full_bar_rect.right - 20, self.full_bar_rect.bottom + 10, 100, 50)

    def assign_song_name(self, song_index):
        self.song_index = song_index
        self.name_songs_gui = my_font(12).render(f"{os.path.splitext(os.path.basename(songs[song_index]))[0]}", True, WHITE)
        self.name_songs_rect = self.name_songs_gui.get_rect(topleft = (self.full_bar_rect.left + 5, self.full_bar_rect.bottom - 15))
        self.song_length = music_length[song_index]
    
    def moving_world(self, speed):
        self.name_songs_rect.move_ip(speed, 0)
        if self.name_songs_rect.right >= self.full_bar_rect.right:
            self.name_songs_rect.left = self.full_bar_rect.left

    def update_rect(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.assign_rect(SCREEN_WIDTH, SCREEN_HEIGHT)

    def update_song_name(self, new_song, music_pos = 0):
        self.assign_song_name(new_song)
        self.procress_bar(music_pos)

    def procress_bar(self, music_pos =0,border_width =2):
        self.bar_rect = pygame.Rect(self.full_bar_rect.left +  border_width, self.full_bar_rect.top + border_width ,(400 - border_width**2) * (music_pos / self.song_length), 20 - border_width**2)

#Music Time Count Format
def music_format(length):
    music_min = int(length // 60000)
    music_sec = int(length % 60000 // 1000)
    return my_font(12).render(f"{music_min}:{music_sec:02}", True, WHITE)

