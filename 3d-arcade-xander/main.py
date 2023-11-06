import pygame
import math

# Initialize pygame
pygame.init()

# Game Variables
enemies = []

# Constants
WIDTH, HEIGHT = 800, 600
FOV = math.pi / 2
HALF_FOV = FOV / 2
NUM_RAYS = int(input(
    "How many rays would you like to cast, the more rays the higher the resolution. (I recomend no more than 300)\n"))
RAY_ANGLE = FOV / NUM_RAYS
DIST_TO_PROJ = WIDTH // 2 / math.tan(HALF_FOV)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SPEED = 10
TURN_SPEED = 0.05
VIEW_DIST = 300

# Player settings
player_pos = [WIDTH // 2, HEIGHT // 2]
player_angle = 0

# Map settings
TILE_SIZE = 100
map_grid = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 0, 0, 0, 0, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 0, 0, 0, 0, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Pygame settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Raycaster with Controls")
clock = pygame.time.Clock()


def cast_ray(x, y, angle):
    while True:
        x += math.cos(angle)
        y += math.sin(angle)

        if 0 <= x // TILE_SIZE < len(map_grid[0]) and 0 <= y // TILE_SIZE < len(map_grid):
            if map_grid[int(y) // TILE_SIZE][int(x) // TILE_SIZE] > 0:
                dist = math.sqrt((x - player_pos[0]) ** 2 + (y - player_pos[1]) ** 2)
                dist *= math.cos(player_angle - angle)
                return [dist, map_grid[int(y) // TILE_SIZE][int(x) // TILE_SIZE]]
        else:
            return float('inf')


def is_wall(x, y):
    if 0 <= x // TILE_SIZE < len(map_grid[0]) and 0 <= y // TILE_SIZE < len(map_grid):
        return map_grid[int(y) // TILE_SIZE][int(x) // TILE_SIZE] == 1
    return True


def render():
    for ray in range(NUM_RAYS):
        ray_angle = player_angle - HALF_FOV + RAY_ANGLE * ray
        cast_ray_dat = cast_ray(player_pos[0], player_pos[1], ray_angle)
        dist = cast_ray_dat[0]
        height = cast_ray_dat[1]

        if VIEW_DIST / dist >= 0 and VIEW_DIST / dist <= 1:
            if dist != float('inf'):
                wall_height = TILE_SIZE * DIST_TO_PROJ / dist
                pygame.draw.rect(screen,
                                 [int(255 * VIEW_DIST / dist), int(255 * VIEW_DIST / dist),
                                  int(255 * VIEW_DIST / dist)], (
                                     ray * WIDTH // NUM_RAYS,
                                     HEIGHT // 2 - (wall_height // 2) - (height // 2 * wall_height),
                                     WIDTH // NUM_RAYS + 1, wall_height * height))
        else:
            if dist != float('inf'):
                wall_height = TILE_SIZE * DIST_TO_PROJ / dist
                pygame.draw.rect(screen,
                                 [255, 255, 255], (
                                     ray * WIDTH // NUM_RAYS,
                                     HEIGHT // 2 - (wall_height // 2) - (height // 2 * wall_height),
                                     WIDTH // NUM_RAYS + 1, wall_height * height))


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    new_x = player_pos[0] + math.cos(player_angle) * SPEED * (keys[pygame.K_w] - keys[pygame.K_s])
    new_y = player_pos[1]
    if not is_wall(new_x, new_y):
        player_pos[0] = new_x

    new_x = player_pos[0]
    new_y = player_pos[1] + math.sin(player_angle) * SPEED * (keys[pygame.K_w] - keys[pygame.K_s])
    if not is_wall(new_x, new_y):
        player_pos[1] = new_y

    if keys[pygame.K_a]:
        player_angle -= TURN_SPEED
    if keys[pygame.K_d]:
        player_angle += TURN_SPEED

    screen.fill(BLACK)
    render()

    # Enemies rendering

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
