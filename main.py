import sys

from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from menu import Button


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.game_running = False
        self.music_playing = True
        self.puton_display = False
        self.delta_time = 1
        self.BG = pygame.image.load('Extra files/background.jpg')
        self.BG = pygame.transform.scale(self.BG, (int(self.BG.get_width() * 5), int(self.BG.get_height() * 5)))
        self.CENTERW = HALF_WIDTH
        #left/right hand mode
        self.right_orient = True
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = Raycasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.assault = Assault(self)
        self.pistol = Pistol(self)
        self.sniper = Sniper(self)
        self.secret = Secret(self)
        self.sound = Sound(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        if self.weapon.weapon_name == "shotgun":
            self.weapon.update()
        elif self.weapon.weapon_name == "assault":
            self.assault.update()
        elif self.weapon.weapon_name == "pistol":
            self.pistol.update()
        elif self.weapon.weapon_name == "sniper":
            self.sniper.update()
        elif self.weapon.weapon_name == "secret":
            self.secret.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption("FPS: " + f'{self.clock.get_fps() :.1f}')

    def draw(self):
        # self.screen.fill('Black')
        self.object_renderer.draw()
        if self.weapon.weapon_name == "shotgun":
            self.weapon.draw()
        elif self.weapon.weapon_name == "assault":
            self.assault.draw()
        elif self.weapon.weapon_name == "pistol":
            self.pistol.draw()
        elif self.weapon.weapon_name == "sniper":
            self.sniper.draw()
        elif self.weapon.weapon_name == "secret":
            self.secret.draw()
        pygame.draw.rect(self.screen, 'Black', (0, 0, 320, 180), 0)
        self.map.draw()
        self.player.draw()

    def check_events(self):
        for event in pygame.event.get():
            self.player.single_fire_event(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game_running = False
                self.music_playing = False
                self.menu()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                self.controls()
            if event.type == self.player.heal_cooldown_event:
                self.player.heal_cooldown = False
                pygame.time.set_timer(self.player.heal_cooldown_event, 0)
            if event.type == self.player.hit_cooldown_event:
                self.player.hit_cooldown = False
                pygame.time.set_timer(self.player.hit_cooldown_event, 0)
            if event.type == self.player.timer_cd_event:
                self.player.timer_cd = False
                pygame.time.set_timer(self.player.timer_cd_event, 0)
            if event.type == self.player.foot_cd_event:
                self.player.foot_cd = False
                pygame.time.set_timer(self.player.foot_cd_event, 0)
            if event.type == self.player.run_cd_event:
                self.player.run_cd = False
                pygame.time.set_timer(self.player.run_cd_event, 0)

    def run(self):
        self.game_running = True
        pygame.mouse.set_visible(False)
        pygame.mixer.music.stop()
        pygame.mixer.Channel(2).play(self.sound.background)
        while self.game_running:
            self.check_events()
            self.update()
            self.draw()


    def get_font(self, size):
        return pygame.font.Font("Extra files/OXYGENE1.TTF", size)

    def get_font2(self, size):
        return pygame.font.Font("Extra files/wheaton capitals.otf", size)

    def get_font3(self, size):
        return pygame.font.SysFont("Arial", size)

    def get_font4(self, size):
        return pygame.font.SysFont('Extra Files/italic bomb.ttf', size)

    def display_text(self, surface, text, pos, font, colour):
        collection = [word.split(' ') for word in text.splitlines()]
        space = font.size(' ')[0]
        x, y = pos
        for lines in collection:
            for words in lines:
                word_surface = font.render(words, True, colour)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= 1350:
                    x = pos[0]
                    y += word_height
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]
            y += word_height

    def menu(self):
        pygame.mouse.set_visible(True)
        self.sound.background.stop()
        self.game_running = False
        while not self.game_running:
            if not pygame.mixer.music.get_busy():
                self.sound.play_music()
            self.screen.blit(self.BG, (0, 0))
            music_display = self.sound.music_list[self.sound.m_choice].replace('.mp3', '')
            self.display_text(self.screen, music_display, (1100, 700), self.get_font4(40), "Red")



            MENU_MOUSE_POS = pygame.mouse.get_pos()

            TITLE = pygame.image.load('Extra files/Title.png')
            TITLE = pygame.transform.scale(TITLE, (int(TITLE.get_width()), int(TITLE.get_height() * 1.25)))
            TITLE_RECT = TITLE.get_rect(center=(self.CENTERW, 100))
            self.screen.blit(TITLE, TITLE_RECT)

            PLAY_BUTTON = Button(pygame.image.load("Extra files/brect red.png"),
                                 (self.CENTERW, 768 / 11 * 4),
                                 "PLAY", self.get_font(75), "#d7fcd4", "Yellow")
            LORE_BUTTON = Button(pygame.image.load("Extra files/brect red.png"),
                                 (self.CENTERW, 768 / 11 * 6),
                                 "LORE", self.get_font(75), "#d7fcd4", "Green")
            CONTROLS_BUTTON = Button(pygame.image.load("Extra files/brect red.png"),
                                     (self.CENTERW, 768 / 11 * 8),
                                     "CONTROLS", self.get_font(75), "#d7fcd4", "Red")
            QUIT_BUTTON = Button(pygame.image.load("Extra files/brect red.png"),
                                 (self.CENTERW, 768 / 11 * 10),
                                 "QUIT", self.get_font(75), "#d7fcd4", "Black")

            for button in [PLAY_BUTTON, CONTROLS_BUTTON, LORE_BUTTON, QUIT_BUTTON]:
                button.changeColour(MENU_MOUSE_POS)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.player.x, self.player.y, self.player.angle, self.player.health = 1.5, 4.5, 0, 100
                        self.object_renderer.timer = 120
                        self.game_running = True
                        self.run()
                    if CONTROLS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.controls()
                    if LORE_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.lore()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    def controls(self):
        pygame.mouse.set_visible(True)
        while True:
            CONTROLS_MOUSE_POS = pygame.mouse.get_pos()
            self.screen.fill("#32abce")

            CONTROLS_TEXT = self.get_font(150).render("CONTROLS", True, "#dbe101")
            CONTROLS_RECT = CONTROLS_TEXT.get_rect(center=(self.CENTERW, 100))
            self.screen.blit(CONTROLS_TEXT, CONTROLS_RECT)

            CONTROLS_BACK = Button(pygame.image.load('Extra files/back button.png'), (100, 100),
                                   "", self.get_font(75), "Black", "Black")
            CONTROLS_BACK.update(self.screen)

            if self.game_running:
                self.display_text(self.screen, """
                W / UP = Forwards
                S / DOWN = Backwards
                A / LEFT = Strafe Left
                D / Right = Strafe Right
                Shift = Sprint
                M = Shotgun
                N = Assault Rifle
                B = Pistol
                V = Sniper
                Left (->) / Right (<-) Click = Shoot
                G = Left Hand Mode
                H = Right Hand Mode
                R = Reset Position (if stuck)
                """, (10, 140), self.get_font2(36), "Yellow")
            else:
                self.display_text(self.screen, """
                                W / UP = Forwards
                                S / DOWN = Backwards
                                A / LEFT = Strafe Left
                                D / Right = Strafe Right
                                Shift = Sprint
                                C = Controls
                                M = Shotgun
                                N = Assault Rifle
                                B = Pistol
                                V = Sniper
                                Left (->) / Right (<-) Click = Shoot
                                G = Left Hand Mode
                                H = Right Hand Mode
                                R = Reset Position (if stuck)
                                """, (10, 140), self.get_font2(34), "Yellow")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.game_running:
                            self.run()
                        elif not self.game_running:
                            self.menu()
                    if event.key == pygame.K_c:
                        if self.game_running:
                            self.run()
                    if event.key == pygame.K_g:
                        self.right_orient = False
                    if event.key == pygame.K_h:
                        self.right_orient = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if CONTROLS_BACK.checkForInput(CONTROLS_MOUSE_POS):
                        if self.game_running:
                            self.run()
                        elif not self.game_running:
                            self.menu()

            pygame.display.update()

    def lore(self):
        while True:
            LORE_MOUSE_POS = pygame.mouse.get_pos()
            self.screen.fill("#205038")

            LORE_TEXT = self.get_font(150).render("LORE", True, "#e10bd1")
            LORE_RECT = LORE_TEXT.get_rect(center=(self.CENTERW, 100))
            self.screen.blit(LORE_TEXT, LORE_RECT)

            LORE_BACK = Button(pygame.image.load('Extra files/back button.png'), (100, 100),
                               "", self.get_font(75), "Black", "Black")

            CHAR1_BUTTON = Button(pygame.image.load("Extra files/brect green.png"),
                                  (292.5, 768 / 11 * 4 - 30),
                                  "JACKAL", self.get_font2(75), "Black", "Black")
            CHAR2_BUTTON = Button(pygame.image.load("Extra files/brect green.png"),
                                  (292.5, 768 / 11 * 4 + 79),
                                  "STEALTH", self.get_font2(75), "Black", "Black")
            CHAR3_BUTTON = Button(pygame.image.load("Extra files/brect green.png"),
                                  (292.5, 768 / 11 * 4 + 188),
                                  "DRAKE", self.get_font2(75), "Black", "Black")
            CHAR4_BUTTON = Button(pygame.image.load("Extra files/brect green.png"),
                                  (292.5, 768 / 11 * 4 + 297),
                                  "NIGGON", self.get_font2(75), "Black", "Black")
            CHAR5_BUTTON = Button(pygame.image.load("Extra files/brect green.png"),
                                  (292.5, 768 / 11 * 4 + 406),
                                  "VALLAT", self.get_font2(75), "Black", "Black")

            for button in [LORE_BACK, CHAR1_BUTTON, CHAR2_BUTTON, CHAR3_BUTTON, CHAR4_BUTTON, CHAR5_BUTTON]:
                button.update(self.screen)

            if CHAR1_BUTTON.checkForInput(LORE_MOUSE_POS):
                CHAR1_BUTTON = Button(pygame.image.load("Extra files/brect green2.png"),
                                      (292.5, 768 / 11 * 4 - 30),
                                      "JACKAL", self.get_font2(75), "Black", "Black")
                CHAR1_BUTTON.update(self.screen)
                text_file = open("Extra files/loretext.txt", "r")
                text = text_file.readlines()
                text_file.close()
                textToWrite = text[0]
                pygame.draw.rect(self.screen, "#40a8a3", pygame.Rect((602, 768 / 11 * 3), (750, 515)))
                self.display_text(self.screen, textToWrite, (609, 768 / 11 * 3), self.get_font3(36), "Black")
            elif CHAR2_BUTTON.checkForInput(LORE_MOUSE_POS):
                CHAR2_BUTTON = Button(pygame.image.load("Extra files/brect green2.png"),
                                      (292.5, 768 / 11 * 4 + 79),
                                      "STEALTH", self.get_font2(75), "Black", "Black")
                CHAR2_BUTTON.update(self.screen)
                text_file = open("Extra files/loretext.txt", "r")
                text = text_file.readlines()
                text_file.close()
                textToWrite = text[1]
                pygame.draw.rect(self.screen, "#40a8a3", pygame.Rect((602, 768 / 11 * 3), (750, 515)))
                self.display_text(self.screen, textToWrite, (609, 768 / 11 * 3), self.get_font3(30), "Black")
            elif CHAR3_BUTTON.checkForInput(LORE_MOUSE_POS):
                CHAR3_BUTTON = Button(pygame.image.load("Extra files/brect green2.png"),
                                      (292.5, 768 / 11 * 4 + 188),
                                      "DRAKE", self.get_font2(75), "Black", "Black")
                CHAR3_BUTTON.update(self.screen)
                text_file = open("Extra files/loretext.txt", "r")
                text = text_file.readlines()
                text_file.close()
                textToWrite = text[2]
                pygame.draw.rect(self.screen, "#40a8a3", pygame.Rect((602, 768 / 11 * 3), (750, 515)))
                self.display_text(self.screen, textToWrite, (609, 768 / 11 * 3), self.get_font3(30), "Black")
            elif CHAR4_BUTTON.checkForInput(LORE_MOUSE_POS):
                CHAR4_BUTTON = Button(pygame.image.load("Extra files/brect green2.png"),
                                      (292.5, 768 / 11 * 4 + 297),
                                      "NIGGON", self.get_font2(75), "Black", "Black")
                CHAR4_BUTTON.update(self.screen)
                text_file = open("Extra files/loretext.txt", "r")
                text = text_file.readlines()
                text_file.close()
                textToWrite = text[3]
                pygame.draw.rect(self.screen, "#40a8a3", pygame.Rect((602, 768 / 11 * 3), (750, 515)))
                self.display_text(self.screen, textToWrite, (609, 768 / 11 * 3), self.get_font3(30), "Black")
            elif CHAR5_BUTTON.checkForInput(LORE_MOUSE_POS):
                CHAR5_BUTTON = Button(pygame.image.load("Extra files/brect green2.png"),
                                      (292.5, 768 / 11 * 4 + 406),
                                      "VALLAT", self.get_font2(75), "Black", "Black")
                CHAR5_BUTTON.update(self.screen)
                text_file = open("Extra files/loretext.txt", "r")
                text = text_file.readlines()
                text_file.close()
                textToWrite = text[4]
                pygame.draw.rect(self.screen, "#40a8a3", pygame.Rect((602, 768 / 11 * 3), (750, 515)))
                self.display_text(self.screen, textToWrite, (609, 768 / 11 * 3), self.get_font3(30), "Black")
            else:
                pygame.draw.rect(self.screen, "#40a8a3", pygame.Rect((602, 768 / 11 * 3), (750, 515)))
                textToWrite = self.get_font3(80).render("SELECT CHARACTER", True, "Black")
                text_rect = textToWrite.get_rect(center=(977, 768 / 2 + 70))
                self.screen.blit(textToWrite, text_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if LORE_BACK.checkForInput(LORE_MOUSE_POS):
                        self.menu()

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.menu()

