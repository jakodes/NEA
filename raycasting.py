import pygame
import math
from settings import *


class Raycasting:
    def __init__(self,game):
        self.game = game
        self.ray_casting_result = []
        self.objects_to_render = []
        self.textures = self.game.object_renderer.wall_textures

    def get_objects_to_render(self):
        self.objects_to_render = []
        for ray, values in enumerate(self.ray_casting_result):
            depth, proj_height, texture, offset = values

            if texture == 5:
                wall_column2 = self.textures[4].subsurface(
                offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE
            )
                wall_column2 = pygame.transform.scale(wall_column2, (SCALE, proj_height))


            wall_column = self.textures[texture].subsurface(
                offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE
            )
            wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
            wall_pos = (ray * SCALE, self.game.player.last_y + HALF_HEIGHT - proj_height // 2)
            wall2_pos = (ray * SCALE, self.game.player.last_y - proj_height + HALF_HEIGHT - proj_height // 2)

            self.objects_to_render.append((depth, wall_column, wall_pos))
            self.objects_to_render.append((depth, wall_column, wall2_pos))
            if texture == 5:
                self.objects_to_render.append((depth, wall_column2, wall_pos))

    def ray_cast(self):
        self.ray_casting_result = []
        ox, oy = self.game.player.pos  # player position
        x_map, y_map = self.game.player.map_pos  # tile position

        texture_vert, texture_hori = 1, 1


        ray_angle = self.game.player.angle - HALF_FOV + 1e-6
        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            #horizontals
            y_hori, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

            depth_hori = (y_hori - oy) / sin_a
            x_hori = ox + depth_hori * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_hori = int(x_hori), int(y_hori)
                if tile_hori in self.game.map.world_map:
                    texture_hori = self.game.map.world_map[tile_hori]
                    break
                x_hori += dx
                y_hori += dy
                depth_hori += delta_depth

            #verticals
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

            depth_vert = (x_vert-ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    texture_vert = self.game.map.world_map[tile_vert]
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            # finds the shortest distance between player and tiles
            if depth_vert < depth_hori:
                depth, texture = depth_vert, texture_vert
                y_vert %= 1
                offset = y_vert if cos_a > 0 else (1 - y_vert)
            else:
                depth, texture = depth_hori, texture_hori
                x_hori %= 1
                offset = (1 - x_hori) if sin_a > 0 else x_hori

            # remove fish eye effect
            depth *= math.cos(self.game.player.angle - ray_angle)

            # projecting it onto 3d plane
            proj_height = SCREEN_DIST / (depth + 0.0001)

            # ray casting result
            self.ray_casting_result.append((depth, proj_height, texture, offset))


            pygame.draw.line(self.game.screen, 'darkgray', (20 * ox, 20 * oy),
                             (20 * ox + 20 * depth * cos_a, 20 * oy + 20 * depth * sin_a))
            ray_angle += DELTA_ANGLE

    def update(self):
        self.ray_cast()
        self.get_objects_to_render()

