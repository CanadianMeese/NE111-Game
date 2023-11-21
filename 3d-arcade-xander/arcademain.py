import pygame
import math

# Initialize pygame
pygame.init()

font = pygame.font.Font(None, 36)

class arcademachine:
    x, y = 0, 0
    tag = ""

# Game Variables
# Marty's Game
gameone = arcademachine()
gameone.x, gameone.y = 0, 0
# Aarons Game
gametwo = arcademachine()
gametwo.x, gametwo.y = 0, 0
# Ben
gamethree = arcademachine()
gamethree.x, gamethree.y = 0, 0

# Constants
WIDTH, HEIGHT = 800, 600
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 60
    #int(input("How many rays would you like to cast, the more rays the higher the resolution. (I recomend no more than 300)\n")))
RAY_ANGLE = FOV / NUM_RAYS
DIST_TO_PROJ = WIDTH // 2 / math.tan(HALF_FOV)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SPEED = 6
TURN_SPEED = 0.05
VIEW_DIST = 300


# Map settings
TILE_SIZE = 100
map_grid_easy = [ #### Start is at (1,1)
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1],
    [1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1],
    [1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1],
    [1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

gameone_easy_pos = [14.5, 9.5]
gametwo_easy_pos = [2, 5.5]
gamethree_easy_pos = [8, 4.5]

map_grid_challenge = [ ######Start is (1,1)
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1],
    [1,0,0,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1],
    [1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1],
    [1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1],
    [1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1],
    [1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1],
    [1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1],
    [1,0,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1],
    [1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1], ##### The end is (44,29)
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

gameone_hard_pos = [44.5, 29.5]
gametwo_hard_pos = [14.5, 27.5]
gamethree_hard_pos = [42, 3.5]

map_grid = []

# Player settings
player_pos = [1 * TILE_SIZE, 1 * TILE_SIZE]
player_angle = 0

def GameOne():
    var = 1
def GameTwo():
    var = 1

def GameThree():
    var = 1

def RenderGameOne():
    ##Game One Rendering
    ########################################
    dx = gameone.x - player_pos[0] / TILE_SIZE
    dy = gameone.y - player_pos[1] / TILE_SIZE
    distance = math.sqrt(dx ** 2 + dy ** 2)

    gameoneangle = math.atan2(dy, dx)
    rel_angle = gameoneangle - player_angle

    while rel_angle > math.pi:
        rel_angle -= 2 * math.pi
    while rel_angle < -math.pi:
        rel_angle += 2 * math.pi

    if cast_ray(player_pos[0], player_pos[1], gameoneangle)[0] / TILE_SIZE > distance:
        # Normalize the relative angle within the FOV
        relative_angle_within_fov = (rel_angle + FOV / 2) / FOV

        screen_x = relative_angle_within_fov * WIDTH

        if 0 <= screen_x <= WIDTH:
            pygame.draw.rect(screen, "green",
                             (screen_x - 200 / distance, HEIGHT // 2 - 350 / distance,
                              400 / distance, 700 / distance))

def RenderGameTwo():
    ##Game Two Rendering
    ########################################
    dx = gametwo.x - player_pos[0] / TILE_SIZE
    dy = gametwo.y - player_pos[1] / TILE_SIZE
    distance = math.sqrt(dx ** 2 + dy ** 2)

    gametwoangle = math.atan2(dy, dx)
    rel_angle = gametwoangle - player_angle

    while rel_angle > math.pi:
        rel_angle -= 2 * math.pi
    while rel_angle < -math.pi:
        rel_angle += 2 * math.pi

    if cast_ray(player_pos[0], player_pos[1], gametwoangle)[0] / TILE_SIZE > distance:
        # Normalize the relative angle within the FOV
        relative_angle_within_fov = (rel_angle + FOV / 2) / FOV

        screen_x = relative_angle_within_fov * WIDTH

        if 0 <= screen_x <= WIDTH:
            pygame.draw.rect(screen, "red",
                             (screen_x - 200 / distance, HEIGHT // 2 - 350 / distance,
                              400 / distance, 700 / distance))

def RenderGameThree():
    ##Game Three Rendering
    ########################################
    dx = gamethree.x - player_pos[0] / TILE_SIZE
    dy = gamethree.y - player_pos[1] / TILE_SIZE
    distance = math.sqrt(dx ** 2 + dy ** 2)

    gamethreeangle = math.atan2(dy, dx)
    rel_angle = gamethreeangle - player_angle

    while rel_angle > math.pi:
        rel_angle -= 2 * math.pi
    while rel_angle < -math.pi:
        rel_angle += 2 * math.pi

    if cast_ray(player_pos[0], player_pos[1], gamethreeangle)[0] / TILE_SIZE > distance:
        # Normalize the relative angle within the FOV
        relative_angle_within_fov = (rel_angle + FOV / 2) / FOV

        screen_x = relative_angle_within_fov * WIDTH

        if 0 <= screen_x <= WIDTH:
            pygame.draw.rect(screen, "blue",
                             (screen_x - 200 / distance, HEIGHT // 2 - 350 / distance,
                              400 / distance, 700 / distance))

    #########################################

# Pygame settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Arcade")
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

    dx1 = gameone.x - player_pos[0] / TILE_SIZE
    dy1 = gameone.y - player_pos[1] / TILE_SIZE
    distance1 = math.sqrt(dx1 ** 2 + dy1 ** 2)

    dx2 = gametwo.x - player_pos[0] / TILE_SIZE
    dy2 = gametwo.y - player_pos[1] / TILE_SIZE
    distance2 = math.sqrt(dx2 ** 2 + dy2 ** 2)

    dx3 = gamethree.x - player_pos[0] / TILE_SIZE
    dy3 = gamethree.y - player_pos[1] / TILE_SIZE
    distance3 = math.sqrt(dx3 ** 2 + dy3 ** 2)

    if distance1 > distance2 > distance3:
        RenderGameOne()
        RenderGameTwo()
        RenderGameThree()
    elif distance2 > distance1 > distance3:
        RenderGameTwo()
        RenderGameOne()
        RenderGameThree()
    elif distance3 > distance1 > distance2:
        RenderGameThree()
        RenderGameOne()
        RenderGameTwo()
    elif distance1 > distance3 > distance2:
        RenderGameOne()
        RenderGameThree()
        RenderGameTwo()
    elif distance3 > distance2 > distance1:
        RenderGameThree()
        RenderGameTwo()
        RenderGameOne()
    elif distance2 > distance3 > distance1:
        RenderGameTwo()
        RenderGameThree()
        RenderGameOne()

running = True
maze_running = False

pygame.mouse.set_visible(False)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_h]:
        map_grid = map_grid_challenge
        gameone.x = gameone_hard_pos[0]
        gameone.y = gameone_hard_pos[1]
        gametwo.x = gametwo_hard_pos[0]
        gametwo.y = gametwo_hard_pos[1]
        gamethree.x = gamethree_hard_pos[0]
        gamethree.y = gamethree_hard_pos[1]
        maze_running = True
    if keys[pygame.K_e]:
        map_grid = map_grid_easy
        gameone.x = gameone_easy_pos[0]
        gameone.y = gameone_easy_pos[1]
        gametwo.x = gametwo_easy_pos[0]
        gametwo.y = gametwo_easy_pos[1]
        gamethree.x = gamethree_easy_pos[0]
        gamethree.y = gamethree_easy_pos[1]
        maze_running = True


    while maze_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                maze_running = False

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

        if keys[pygame.K_ESCAPE]:
            # Reset Player
            player_pos = [1 * TILE_SIZE, 1 * TILE_SIZE]
            player_angle = 0
            maze_running = False

        # Update game state and render
        screen.fill(BLACK)
        render()

        dx1 = gameone.x - player_pos[0] / TILE_SIZE
        dy1 = gameone.y - player_pos[1] / TILE_SIZE
        distance1 = math.sqrt(dx1 ** 2 + dy1 ** 2)

        if (distance1 < 1):
            text_surface = font.render("Press F To Enter", True, "black")
            text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            screen.blit(text_surface, text_rect)
            if keys[pygame.K_f]:
                GameOne()

        dx2 = gametwo.x - player_pos[0] / TILE_SIZE
        dy2 = gametwo.y - player_pos[1] / TILE_SIZE
        distance2 = math.sqrt(dx2 ** 2 + dy2 ** 2)

        if (distance2 < 1):
            text_surface = font.render("Press F To Enter", True, "black")
            text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            screen.blit(text_surface, text_rect)
            if keys[pygame.K_f]:
                GameTwo()

        dx3 = gamethree.x - player_pos[0] / TILE_SIZE
        dy3 = gamethree.y - player_pos[1] / TILE_SIZE
        distance3 = math.sqrt(dx3 ** 2 + dy3 ** 2)

        if (distance3 < 1):
            text_surface = font.render("Press F To Enter", True, "black")
            text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            screen.blit(text_surface, text_rect)
            if keys[pygame.K_f]:
                GameThree()

        text_surface = font.render("Press ESC To Exit The Maze", True, "white")
        screen.blit(text_surface, (3,3))

        pygame.display.flip()
        clock.tick(60)

    screen.fill(BLACK)

    text_surface = font.render("Press H To Enter The Challenge Maze", True, "white")
    text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 30))
    screen.blit(text_surface, text_rect)

    text_surface = font.render("Press E To Enter The Easy Maze", True, "white")
    text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 30))
    screen.blit(text_surface, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
