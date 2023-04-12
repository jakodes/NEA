import pygame
from settings import *
import os
from collections import deque


class SpriteObject:
    def __init__(self, game, path='Sprites/static sprites/candlebra.png', pos=(10.5, 3.5), scale=0):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pygame.image.load(path).convert_alpha()
        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.image.get_width() // 2
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1
        self.sprite_half_width = 0

    def get_sprite_projection(self):
        proj = SCREEN_DIST / self.norm_dist
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj

        image = pygame.transform.scale(self.image, (proj_width, proj_height))

        self.sprite_half_width = proj_width // 2
        pos = self.screen_x - self.sprite_half_width, self.game.player.last_y + HALF_HEIGHT - proj_height // 2

        self.game.raycasting.objects_to_render.append((self.norm_dist, image, pos))


    def get_sprite(self):
        dx = self.x - self.player.x  # forward distance
        dy = self.y - self.player.y  # side distance
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)  # angle between player and sprite

        delta = self.theta - self.player.angle  # angle between player direction and player position's angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        delta_rays = delta / DELTA_ANGLE
        self.screen_x = (HALF_NUM_RAYS + delta_rays) * SCALE

        self.dist = math.hypot(dx, dy)  # hypotenuse (diagonal dist.)
        self.norm_dist = self.dist * math.cos(delta)
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            self.get_sprite_projection()




    def update(self):
        self.get_sprite()

class AnimatedSprite(SpriteObject):
    def __init__(self, game, path='Sprites/animated sprites/red_light/0.png',
                 pos=(11.5, 3.5), scale=0, animation_time=120):
        super().__init__(game, path, pos)
        self.animation_time = animation_time
        self.path = path.rsplit('/', 1)[0]
        self.images = self.get_images(self.path)
        self.animation_time_prev = pygame.time.get_ticks()
        self.animation_trigger = False

    def update(self):
        super().update()
        self.check_animation_time()
        self.animate(self.images)

    def animate(self, images):
        if self.animation_trigger:
            images.rotate(-1)
            self.image = images[0]

    def check_animation_time(self):
        self.animation_trigger = False
        time_now = pygame.time.get_ticks()
        if time_now - self.animation_time_prev > self.animation_time:
            self.animation_time_prev = time_now
            self.animation_trigger = True

    def get_images (self, path):
        images = deque()
        for file_name in os.listdir(path):
            if os.path.isfile(os.path.join(path, file_name)):
                img = pygame.image.load(path + '/' + file_name).convert_alpha()
                if self.game.right_orient:
                    img = pygame.transform.flip(img, True, False)
                images.append(img)
        return images
