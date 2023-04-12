import math

# game settings
RES = WIDTH, HEIGHT = 1368, 768
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 30

PLAYER_POS = 1.5, 5
PLAYER_ANGLE = 0
PLAYER_ANGLEV = 0
PLAYER_SPEED = 0.003
PLAYER_ROT_SPEED = 0.003
PLAYER_SIZE_SCALE = 100

MOUSE_SENSITIVITY_X = 0.0002
MOUSE_SENSITIVITY_Y = 0.06
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT
MOUSE_BORDER_DOWN = HEIGHT - MOUSE_BORDER_LEFT


FLOOR_COLOUR = '#10e749'

FOV = math.pi / 3  # field of view
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2  # number of "light" rays
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS  # angle between each ray
MAX_DEPTH = 20  # max distance between player and walls

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2



weapons = ["shotgun", "assault", "pistol", "sniper", "secret"]


