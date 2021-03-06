BOARD_WIDTH = 1000
BOARD_HEIGHT = 1000

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

ANTIALIASING = True

AI_VISIBLE_RADIUS = 13 # multiple of current radius
MOUSE_SENSITIVE_RADIUS = 48

FORCE_DRAG = 0.95
BOUNCE_STRENGTH = 1
BOUNCE_BASE_VALUE = 10
BASE_SPEED = 300

BLOB_WEIGHT_RATIO_TO_EAT = 0.85
BLOB_INIT_WEIGHT = 16
BLOB_GRAVITATION = 0.015
BLOB_REPEL_STRENGTH = 0.1
BLOB_REPEL_BASE_STRENGTH = 0.01
BLOB_EXPLOSION_SHRINK = 0.8
BLOB_SHOOT_STRENGTH = 160
BLOB_DIVIDE_STRENGTH = 80
BLOB_EXPLOSION_SHOOT_CHANCE = 1 # meaning the chance is 1:N
BLOB_MERGE_INIT_TIME = 20
BLOB_MERGE_TIME_MULTIPLIER = 0.2
BLOB_MINIMAL_WEIGHT_TO_EXPLODE = 250
BLOB_MAX_NUM = 16
BLOB_WEIGHT_LOSE_PER_SECOND = 0.002

BULLET_WEIGHT = 14
BULLET_EAT_RATIO = 0.8 # how much weight is added to blob that ate it
BULLET_PELLET_STRENGTH = 1.0
BULLET_BLOB_STRENGTH = 0.1

LARGE_PELLET_NUM = 6
LARGE_PELLET_WEIGHT = 80
LARGE_PELLET_RADIUS = 10

SMALL_PELLET_NUM = 200
SMALL_PELLET_RADIUS = 2

VIEW_BACKGROUND_COLOR = (0,0,0)
VIEW_BORDER_COLOR = (128,128,128)
VIEW_LARGE_PELLET_COLOR = (128,128,128)
VIEW_SMALL_PELLET_COLOR = (96,96,96)
