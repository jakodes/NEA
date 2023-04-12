import pygame
from settings import *
import math
from weapon import *


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.placement = 0
        self.last_y = 0
        self.last_yy = 0
        self.shot = False
        self.weapon_name = "shotgun"
        self.weapon_number = 0
        self.health = 100
        self.heal_cooldown = True
        self.heal_cooldown_event = pygame.USEREVENT + 4
        self.hit_cooldown = False
        self.hit_cooldown_event = pygame.USEREVENT + 5
        self.begin_healing = False
        self.timer_cd = False
        self.timer_cd_event = pygame.USEREVENT + 1
        self.foot_cd = False
        self.foot_cd_event = pygame.USEREVENT + 2
        self.run_cd = False
        self.run_cd_event = pygame.USEREVENT + 3

    def single_fire_event(self, event):
        if not self.game.right_orient:
            if self.game.weapon.weapon_name == "shotgun":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3 and not self.shot and not self.game.weapon.reloading:
                        self.game.sound.shotgun.play()
                        self.shot = True
                        self.game.weapon.reloading = True
            elif self.game.weapon.weapon_name == "assault":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3 and not self.shot and not self.game.weapon.reloading:
                        self.game.sound.assault.play()
                        self.shot = True
                        self.game.assault.reloading = True
            elif self.game.weapon.weapon_name == "pistol":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3 and not self.shot and not self.game.weapon.reloading:
                        self.game.sound.pistol.play()
                        self.shot = True
                        self.game.pistol.reloading = True
            elif self.game.weapon.weapon_name == "sniper":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3 and not self.shot and not self.game.weapon.reloading:
                        self.game.sound.sniper.play()
                        self.shot = True
                        self.game.weapon.reloading = True
            elif self.game.weapon.weapon_name == "secret":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3 and not self.shot and not self.game.weapon.reloading:
                        self.game.sound.secret.play()
                        self.shot = True
                        self.game.weapon.reloading = True
        elif self.game.right_orient:
            if self.game.weapon.weapon_name == "shotgun":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and not self.shot and not self.game.weapon.reloading:
                        self.game.sound.shotgun.play()
                        self.shot = True
                        self.game.weapon.reloading = True
            elif self.game.weapon.weapon_name == "assault":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and not self.shot and not self.game.weapon.reloading:
                        self.game.sound.assault.play()
                        self.shot = True
                        self.game.assault.reloading = True
            elif self.game.weapon.weapon_name == "pistol":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and not self.shot and not self.game.weapon.reloading:
                        self.game.sound.pistol.play()
                        self.shot = True
                        self.game.pistol.reloading = True
            elif self.game.weapon.weapon_name == "sniper":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and not self.shot and not self.game.weapon.reloading:
                        self.game.sound.sniper.play()
                        self.shot = True
                        self.game.sniper.reloading = True
            elif self.game.weapon.weapon_name == "secret":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and not self.shot and not self.game.weapon.reloading:
                        self.game.sound.secret.play()
                        self.shot = True
                        self.game.secret.reloading = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 5:
                self.weapon_number += 1
                if self.weapon_number > 3:
                    self.weapon_number %= 4
            if event.button == 4:
                self.weapon_number -= 1
                if self.weapon_number < 0:
                    self.weapon_number %= 4


    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        # uses sin and cosine of angle between where player is looking
        # and pos to calculate speed through gradient
        # dx and dy are corresponding speeds
        dx, dy = 0, 0
        # delta time is time between each frame so used to change
        # speed of player irrespective of fps
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a


        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dx += speed_cos
            dy += speed_sin
            if self.foot_cd == False:
                self.foot_cd = True
                pygame.mixer.Channel(1).set_volume(0, 0.3)
                pygame.mixer.Channel(1).play(self.game.sound.footstep)
                pygame.time.set_timer(self.foot_cd_event, 700)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx += -speed_sin
            dy += speed_cos

        if self.game.right_orient:
            if keys[pygame.K_w] and keys[pygame.K_LSHIFT]:
                dx += speed_cos * 1.4
                dy += speed_sin * 1.4
                if self.run_cd == False:
                    self.run_cd = True
                    pygame.mixer.Channel(1).set_volume(0, 0.3)
                    pygame.mixer.Channel(1).play(self.game.sound.footstep)
                    pygame.time.set_timer(self.run_cd_event, 300)
            if keys[pygame.K_s] and keys[pygame.K_LSHIFT]:
                dx += -speed_cos * 1.4
                dy += -speed_sin * 1.4
            if keys[pygame.K_a] and keys[pygame.K_LSHIFT]:
                dx += speed_sin * 1.2
                dy += -speed_cos * 1.2
            if keys[pygame.K_d] and keys[pygame.K_LSHIFT]:
                dx += -speed_sin * 1.2
                dy += speed_cos * 1.2
        else:
            if keys[pygame.K_UP] and keys[pygame.K_RSHIFT]:
                dx += speed_cos * 1.4
                dy += speed_sin * 1.4
            if keys[pygame.K_DOWN] and keys[pygame.K_RSHIFT]:
                dx += -speed_cos * 1.4
                dy += -speed_sin * 1.4
            if keys[pygame.K_LEFT] and keys[pygame.K_RSHIFT]:
                dx += speed_sin * 1.2
                dy += -speed_cos * 1.2
            if keys[pygame.K_RIGHT] and keys[pygame.K_RSHIFT]:
                dx += -speed_sin * 1.2
                dy += speed_cos * 1.2

        if keys[pygame.K_n] or self.weapon_number == 1:  # ar
            self.weapon_number = 1
            self.game.weapon.weapon_name = weapons[self.weapon_number]
        if keys[pygame.K_m] or self.weapon_number == 0:  # shotgun
            self.weapon_number = 0
            self.game.weapon.weapon_name = weapons[self.weapon_number]
        if keys[pygame.K_b] or self.weapon_number == 2:  # pistol
            self.weapon_number = 2
            self.game.weapon.weapon_name = weapons[self.weapon_number]
        if keys[pygame.K_v] or self.weapon_number == 3:  # sniper
            self.weapon_number = 3
            self.game.weapon.weapon_name = weapons[self.weapon_number]
        if keys[pygame.K_LCTRL] and keys[pygame.K_LSHIFT] and keys[pygame.K_p]:  # secret
            self.weapon_number = 4
            self.game.weapon.weapon_name = weapons[self.weapon_number]


        if keys[pygame.K_r]:
            self.x, self.y = 1.5, 5
            self.angle = 0

        if keys[pygame.K_k]:
            if self.hit_cooldown == False:
                self.health -= 10
                self.game.screen.fill('Yellow')
                self.hit_cooldown = True
                self.heal_cooldown = True
                if self.health > 0 and self.health < 100:
                    self.game.sound.pain.play()
                pygame.time.set_timer(self.hit_cooldown_event, 750)
                if self.health == 0:
                    self.game.menu()
                    self.game.game_running = False
                if self.health < 100:
                    self.begin_healing = True
                    self.heal_cooldown = False

        if self.begin_healing:
            if self.hit_cooldown == False:
                if self.heal_cooldown == False:
                    self.heal_cooldown = True
                    self.health += 5
                    pygame.time.set_timer(self.heal_cooldown_event, 3000)
                    if self.health > 100:
                        self.heal_cooldown = True
                        self.health = 100

        if self.timer_cd == False:
            self.timer_cd = True
            self.game.object_renderer.timer -= 1
            pygame.time.set_timer(self.timer_cd_event, 1000)
            if self.game.object_renderer.timer < 1:
                self.game.object_renderer.timer = 0
                self.game.menu()
                self.game.game_running = False


        self.check_collision(dx, dy)

        # if keys[pygame.K_LEFT]:
        #    self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        # elif keys[pygame.K_RIGHT]:
        #    self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        # self.angle %= math.tau

        # mx, my = pygame.mouse.get_pos()
        # mx, my = (mx - HALF_WIDTH) / 50, (my - HALF_HEIGHT) / 50
        # self.placement = my * 120
        # if pygame.mouse.get_focused():
        #    last_x = mx * PLAYER_ROT_SPEED
        #    self.angle = math.atan(last_x) * 120
        #    self.angle %= math.tau
        #   self.last_y = -self.placement


    def check_wall(self, x, y):
        return(x, y) not in self.game.map.world_map

    def check_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self):
        # pygame.draw.line(self.game.screen, 'darkgray', (self.x * 10, self.y * 10),
        #                  (self.x * 10 + WIDTH * math.cos(self.angle),
        #                  self.y * 10 + WIDTH * math.sin(self.angle)), 2)
        pygame.draw.circle(self.game.screen, 'red', (self.x * 20, self.y * 20), 5)


    def mouse_control(self):
        mx, my = pygame.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pygame.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        if my < MOUSE_BORDER_LEFT or my > MOUSE_BORDER_DOWN:
            pygame.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])

        self.rel = pygame.mouse.get_rel()
        self.rely = self.rel[1]
        self.last_y -= self.rely * MOUSE_SENSITIVITY_Y * self.game.delta_time
        if self.last_y > 135:
            self.last_y = 135
        elif self.last_y < -385:
            self.last_y = -385

        self.relx = self.rel[0]
        self.relx = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.relx))
        self.angle += self.relx * MOUSE_SENSITIVITY_X * self.game.delta_time
        self.angle %= math.tau

        # my = (my - HALF_HEIGHT) // 50
        # self.placement = my * 133333 * MOUSE_SENSITIVITY_Y
        # self.last_yy = -self.placement
        # if self.last_yy > 100:
        #    self.last_yy = 100
        #    pygame.mouse.set_pos(mx, 240)
        # elif self.last_yy < -159:
        #    pygame.mouse.set_pos(mx, 585)





    def update(self):
        self.movement()
        self.mouse_control()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
