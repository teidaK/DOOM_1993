import math

# game settings
RES = WIDTH, HEIGHT = 1600, 900
# RES = WIDTH, HEIGHT = 1920, 1080
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 0

PLAYER_POS = 1.5, 5  # mini_map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002
PLAYER_SIZE_SCALE = 60
PLAYER_MAX_HEALTH = 150

MOUSE_SENSITIVITY = 0.0003
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT

FLOOR_COLOR = (30, 30, 30)

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2
import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player_pos = [400, 300]
aim_angle = 0

def aim_at_mouse():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    rel_x, rel_y = mouse_x - player_pos[0], mouse_y - player_pos[1]
    return math.degrees(math.atan2(rel_y, rel_x))

def draw_aim():
    pygame.draw.circle(screen, (255, 255, 255), (int(player_pos[0] + 30 * math.cos(math.radians(aim_angle))),
                                                 int(player_pos[1] + 30 * math.sin(math.radians(aim_angle)))), 5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    aim_angle = aim_at_mouse()
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(player_pos[0], player_pos[1], 30, 30))
    draw_aim()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
