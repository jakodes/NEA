from sprite_object import *


class Weapon(AnimatedSprite):
    def __init__(self, game, path='Sprites/weapons/shotgun/0.png', scale=0.45, animation_time=90):
        self.weapon_name = "shotgun"
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        self.images=deque(
            [pygame.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.weap_sprite = pygame.image.load('Extra Files/shotgun_sprite.png').convert_alpha()
        self.weap_sprite = pygame.transform.smoothscale(self.weap_sprite, (
        self.weap_sprite.get_width() * 4, self.weap_sprite.get_height() * 4))
        self.weap_spos = (WIDTH - self.weap_sprite.get_width(), HEIGHT // 3)
        self.reticle = pygame.image.load('Extra Files/reticle.png').convert_alpha()
        self.reticle = pygame.transform.smoothscale(self.reticle, (
            self.reticle.get_width() * 2, self.reticle.get_height() * 2))
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 45

    def animate_shot(self):
        if self.reloading:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0


    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)
        self.game.screen.blit(self.weap_sprite, self.weap_spos)
        self.game.screen.blit(self.reticle, (HALF_WIDTH - 20, HALF_HEIGHT - 20))


    def update(self):
        self.check_animation_time()
        self.animate_shot()


class Assault(Weapon):
    def __init__(self, game, path='Sprites/weapons/ar/0.png', scale=3.25, animation_time=60):
        self.path_used = path
        self.weapon_name = "assault"
        super().__init__(game=game, path=self.path_used, scale=scale, animation_time=animation_time)
        self.images = deque(
            [pygame.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.weap_sprite = pygame.image.load('Extra Files/assault_sprite.png').convert_alpha()
        self.weap_sprite = pygame.transform.smoothscale(self.weap_sprite, (
        self.weap_sprite.get_width() * 2, self.weap_sprite.get_height() * 2))
        self.weap_spos = (WIDTH - self.weap_sprite.get_width(), HEIGHT // 3 + 24)
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 25

    def animate_shot(self):
        super().animate_shot()

    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)
        self.game.screen.blit(self.weap_sprite, self.weap_spos)
        pygame.draw.rect(self.game.screen, 'white', (HALF_WIDTH - 1, HALF_HEIGHT - 13, 3, 10), 2)
        pygame.draw.rect(self.game.screen, 'white', (HALF_WIDTH - 1, HALF_HEIGHT + 3, 3, 10), 2)
        pygame.draw.rect(self.game.screen, 'white', (HALF_WIDTH - 11.5, HALF_HEIGHT - 1.5, 10, 3), 2)
        pygame.draw.rect(self.game.screen, 'white', (HALF_WIDTH + 3, HALF_HEIGHT - 1.5, 10, 3), 2)


    def update(self):
        super().update()


class Pistol(Weapon):
    def __init__(self, game, path='Sprites/weapons/pistol/0.png', scale=5, animation_time=15):
        self.path_used = path
        self.weapon_name = "pistol"
        super().__init__(game=game, path=self.path_used, scale=scale, animation_time=animation_time)
        self.images = deque(
            [pygame.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.weap_sprite = pygame.image.load('Extra Files/pistol_sprite.png').convert_alpha()
        self.weap_sprite = pygame.transform.smoothscale(self.weap_sprite, (
        self.weap_sprite.get_width() * 2.5, self.weap_sprite.get_height() * 2.5))
        self.weap_spos = (WIDTH - self.weap_sprite.get_width(), HEIGHT // 3 + 54)
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 10

    def animate_shot(self):
        super().animate_shot()

    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)
        self.game.screen.blit(self.weap_sprite, self.weap_spos)
        pygame.draw.rect(self.game.screen, 'white', (HALF_WIDTH - 1, HALF_HEIGHT - 13, 3, 10), 2)
        pygame.draw.rect(self.game.screen, 'white', (HALF_WIDTH - 1, HALF_HEIGHT + 3, 3, 10), 2)
        pygame.draw.rect(self.game.screen, 'white', (HALF_WIDTH - 11.5, HALF_HEIGHT - 1.5, 10, 3), 2)
        pygame.draw.rect(self.game.screen, 'white', (HALF_WIDTH + 3, HALF_HEIGHT - 1.5, 10, 3), 2)

    def update(self):
        super().update()


class Sniper(Weapon):
    def __init__(self, game, path='Sprites/weapons/sniper/0.png', scale=3.5, animation_time=90):
        self.path_used = path
        self.weapon_name = "sniper"
        super().__init__(game=game, path=self.path_used, scale=scale, animation_time=animation_time)
        self.images = deque(
            [pygame.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.weap_sprite = pygame.image.load('Extra Files/sniper_sprite.png').convert_alpha()
        self.weap_sprite = pygame.transform.smoothscale(self.weap_sprite, (
        self.weap_sprite.get_width() * 1.5, self.weap_sprite.get_height() * 1.5))
        self.weap_spos = (WIDTH - self.weap_sprite.get_width(), HEIGHT // 3 + 89)
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 80

    def animate_shot(self):
        super().animate_shot()

    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)
        self.game.screen.blit(self.weap_sprite, self.weap_spos)
        pygame.draw.circle(self.game.screen, 'white', (HALF_WIDTH, HALF_HEIGHT), 5)

    def update(self):
        super().update()


class Secret(Weapon):
    def __init__(self, game, path='Sprites/weapons/secret/0.png', scale=3.25, animation_time=120):
        self.path_used = path
        self.weapon_name = "secret"
        super().__init__(game=game, path=self.path_used, scale=scale, animation_time=animation_time)
        self.images = deque(
            [pygame.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.weap_sprite = pygame.image.load('Extra Files/secret_sprite.png').convert_alpha()
        self.weap_sprite = pygame.transform.smoothscale(self.weap_sprite, (
        self.weap_sprite.get_width() * 2, self.weap_sprite.get_height() * 2))
        self.weap_spos = (WIDTH - self.weap_sprite.get_width(), 0)
        self.reticle = pygame.image.load('Extra Files/secret_reticle.png').convert_alpha()
        self.reticle = pygame.transform.smoothscale(self.reticle, (
            self.reticle.get_width() * 2.8, self.reticle.get_height() * 2.8))
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 150

    def animate_shot(self):
        super().animate_shot()

    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)
        self.game.screen.blit(self.weap_sprite, self.weap_spos)
        self.game.screen.blit(self.reticle, (HALF_WIDTH - 20, HALF_HEIGHT - 20))

    def update(self):
        super().update()

