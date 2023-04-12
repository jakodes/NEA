import pygame
import random


_ = False
# noinspection PyTypeChecker
mini_map = [
    [[1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 4, 4, 4, 4, 4, 4],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4],
    [1, _, _, 3, 2, 2, 3, _, _, _, 4, 4, 4, _, _, 4],
    [1, _, _, _, _, _, 2, _, _, _, _, _, 4, _, _, 4],
    [1, _, _, _, _, _, 6, _, _, _, _, _, 4, _, _, 4],
    [1, _, _, 3, 2, 2, 3, _, _, _, _, _, _, _, _, 4],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4],
    [1, _, _, 1, _, _, _, 3, _, _, _, _, _, _, _, 4],
    [1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 4, 4, 4, 5, 4, 4]],


    [[4, 4, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4],
    [4, _, _, 3, 2, 2, 3, _, _, _, 4, 4, 4, _, _, 4],
    [4, _, _, _, _, _, 6, _, _, _, _, _, 4, _, _, 4],
    [4, _, _, _, _, _, 2, _, _, _, _, _, 4, _, _, 4],
    [4, _, _, 3, 2, 2, 3, _, _, _, _, _, _, _, _, 4],
    [4, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4],
    [4, _, _, 4, _, _, _, 3, _, _, _, _, _, _, _, 4],
    [4, 4, 5, 5, 5, 4, 4, 3, 3, 3, 4, 4, 4, 4, 4, 4]



    ]
]



class Map:
    def __init__(self, game):
        x = random.randint(0, 1)
        self.game = game
        self.mini_map = mini_map[x]
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                        if value:
                            self.world_map[i, j] = value

    def draw(self):
        [pygame.draw.rect(self.game.screen, 'yellow', (pos[0] * 20, pos[1] * 20, 20, 20), 2)
         for pos in self.world_map]
