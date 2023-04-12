import pygame
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('Extra Files/sky.png', (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0
        self.digit_size = 90
        self.digit_images = [self.get_texture(f'Sprites/digits/{i}.png', [self.digit_size] * 2)
                             for i in range(11)]
        self.digits = dict(zip(map(str, range(11)), self.digit_images))
        self.timer = 120

    def draw(self):
        self.draw_background()
        self.render_game_objects()
        self.draw_player_health()
        self.draw_timer()

    def draw_player_health(self):
        health = str(self.game.player.health)
        for i, char in enumerate(health):
            self.screen.blit(self.digits[char], (i * self.digit_size, HEIGHT - self.digits[char].get_height()))
        self.screen.blit(self.digits['10'], ((i + 1) * self.digit_size, HEIGHT - self.digits[char].get_height()))

    def draw_timer(self):
        timer = str(self.timer)
        for i, char in enumerate(timer):
            self.screen.blit(self.digits[char], (i * self.digit_size + HALF_WIDTH - 90, self.digits[char].get_height() // 2))

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.relx) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        pygame.draw.rect(self.screen, FLOOR_COLOUR, (0, self.game.player.last_y +  HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)

    def load_wall_textures(self):
        return{
            1: self.get_texture('Extra Files/wood.png'),
            2: self.get_texture('Extra Files/finalflag.png'),
            3: self.get_texture('Extra Files/bricks.png'),
            4: self.get_texture('Extra Files/purpur.png'),
            5: self.get_texture('Extra Files/glass2.png'),
            6: self.get_texture('Extra Files/secretflag.png')
        }
