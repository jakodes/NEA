import pygame
import random
import settings

class Sound:
    def __init__(self, game):
        self.game = game
        pygame.mixer.init()
        self.path = 'Sounds + Music/'
        self.shotgun = pygame.mixer.Sound(self.path + 'shotgun.wav')
        self.assault = pygame.mixer.Sound(self.path + 'assault.wav')
        self.pistol = pygame.mixer.Sound(self.path + 'pistol.wav')
        self.sniper = pygame.mixer.Sound(self.path + 'sniper.wav')
        self.secret = pygame.mixer.Sound(self.path + 'secret.wav')
        self.background = pygame.mixer.Sound(self.path + 'Background Music.mp3')
        self.footstep = pygame.mixer.Sound(self.path + 'footstep.mp3')
        self.pain = pygame.mixer.Sound(self.path + 'pain sound effect.mp3')

        self.music_list = ["Da Rant - Morray.mp3", "Out the Way - Yeat.mp3",
                           "Spirit of X2C - Lancey Foux.mp3", "Dream in Color - Cordae.mp3",
                           "Blicky - Fresh x Reckless.mp3", "Feel Alive - Hardrock.mp3",
                           "If Looks Could Kill - Destroy Lonely.mp3", "All I Wanted - Paramore.mp3", "Hell Yeah - tana.mp3"]
        self.m_choice = 0
        self.music_played = []

    def play_music(self):
        music_choice = random.randint(0, len(self.music_list) - 1)
        self.m_choice = music_choice
        song = self.path + self.music_list[music_choice]
        if song not in self.music_played:
            self.music_played.append(song)
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
        else:
            music_choice = random.randint(0, len(self.music_list) - 1)
            self.m_choice = music_choice
            if len(self.music_played) == len(self.music_list):
                self.music_played = []



