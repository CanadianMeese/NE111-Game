# Code written by Xander Linzel

import pygame  # Import the pygame library for creating games
import math  # Import math module for mathematical operation
from pygame.locals import *  # Import constants from pygame
import time  # Import time module for time-related tasks
import random  # Import random module for random number generation
import rubikscubemain  # Import a custom module for a Rubik's Cube game
import snakegamemain  # Import a custom module for a Snake game
import minefieldgamemain  # Import a custom module for a Minefield game

# Initialize pygame
pygame.init()

# Create a font for the text
font = pygame.font.Font(None, 36)

# Create a class for the arcade machine
class arcademachine:
    x, y = 0, 0
    tag = ""

# Game Variables
# Marty's Game
gameone = arcademachine()
# Set the x and y coordinates of the arcade machine
gameone.x, gameone.y = 0, 0
# Set the tag of the arcade machine, True means we just exited the game
gameonejustin = False
#Initialize pngs
gameoneimage = pygame.image.load("Snake (Generated with Dalle3).png")

# Aarons Game
gametwo = arcademachine()
gametwo.x, gametwo.y = 0, 0
gametwojustin = False
gametwoimage = pygame.image.load("Rubiks (Generated with Dalle3).png")


# Ben
gamethree = arcademachine()
gamethree.x, gamethree.y = 0, 0
gamethreejustin = False
gamethreeimage = pygame.image.load("Minefield (Generated with Dalle3).png")

# Constants
WIDTH, HEIGHT = 800, 600
FOV = math.pi / 3 # Field of view
HALF_FOV = FOV / 2 # Half of the field of view
NUM_RAYS = 100 # Number of rays to cast
FPS = 60 # Frames per second
RAY_ANGLE = FOV / NUM_RAYS # Angle between each ray
DIST_TO_PROJ = WIDTH // 2 / math.tan(HALF_FOV) # Distance to the projection plane
WHITE = (255, 255, 255) # White color
BLACK = (0, 0, 0)  # Black color
SPEED = 6  # Movement speed
TURN_SPEED = 0.05 # Turning speed
VIEW_DIST = 300 # Maximum view distance

delta_time = 1

# Map settings
TILE_SIZE = 100 # Size of each tile in the map

map_grid_arcade = [ #### Start is at (1,1)
    [1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,1,1,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,1,1,1,1,1],
    [1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1]
]

# Positions of the arcade machines
gameone_arcade_pos = [5.5, 1.5]
gametwo_arcade_pos = [5.5, 3.5]
gamethree_arcade_pos = [5.5, 5.5]

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

# Positions of the arcade machines
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

# Positions of the arcade machines
gameone_hard_pos = [44.5, 29.5]
gametwo_hard_pos = [14.5, 27.5]
gamethree_hard_pos = [42, 3.5]

# Creating the empty map grid for future use
map_grid = []

# Player settings
player_pos = [1 * TILE_SIZE, 1 * TILE_SIZE] # Player position
player_angle = 0 # Player angle

def GameOne():
    '''Run the code to launch the first game'''
    snakegamemain.snakegame() # Call the main function from the snakegamemain module
    gameonejustin = True # Set the gameonejustin variable to True
    
def GameTwo():
    '''Run the code to launch the second game'''
    rubikscubemain.rubiksgame() # Call the main function from the rubikscubemain module
    gametwojustin = True

def GameThree():
    '''Run the code to launch the third game'''
    pygame.mouse.set_visible(True)
    minefieldgamemain.minefieldgame() # Call the main function from the rubikscubemain module
    pygame.mouse.set_visible(False)
    gametwojustin = True

def RenderGameOne():
    ##Game One Rendering
    ########################################
    dx = gameone.x - player_pos[0] / TILE_SIZE # Calculate the difference in x coordinates between the player and the arcade machine
    dy = gameone.y - player_pos[1] / TILE_SIZE # Calculate the difference in y coordinates between the player and the arcade machine
    distance = math.sqrt(dx ** 2 + dy ** 2) # Calculate the distance between the player and the arcade machine

    gameoneangle = math.atan2(dy, dx) # Calculate the angle between the player and the arcade machine
    rel_angle = gameoneangle - player_angle # Calculate the relative angle between the player and the arcade machine

    # Normalize the relative angle within the FOV
    while rel_angle > math.pi: # If the relative angle is greater than pi
        rel_angle -= 2 * math.pi    # Subtract 2pi from the relative angle
    while rel_angle < -math.pi: # If the relative angle is less than -pi
        rel_angle += 2 * math.pi   # Add 2pi to the relative angle

    # If the distance between the player and the arcade machine is less than the distance between the player and the wall
    if cast_ray(player_pos[0], player_pos[1], gameoneangle)[0] / TILE_SIZE > distance:
        # Normalize the relative angle within the FOV
        relative_angle_within_fov = (rel_angle + FOV / 2) / FOV # Calculate the relative angle within the FOV

        screen_x = relative_angle_within_fov * WIDTH # Calculate the x coordinate of the arcade machine on the screen

        # If the x coordinate of the arcade machine is within the screen
        if 0 <= screen_x <= WIDTH: 
            # Draw the png to the screen
            scaled_width = gameoneimage.get_rect().width * 1.1 / distance
            scaled_height = gameoneimage.get_rect().height * 1.1 / distance
            scaled_image = pygame.transform.scale(gameoneimage, (int(scaled_width), int(scaled_height)))

            # Draw the image onto the screen at the updated rect position
            screen.blit(scaled_image, (screen_x - scaled_width / 2, HEIGHT // 2 - scaled_height / 2,
                              scaled_width / distance, scaled_height / distance))

def RenderGameTwo():
    ##Game Two Rendering
    ########################################
    dx = gametwo.x - player_pos[0] / TILE_SIZE # Calculate the difference in x coordinates between the player and the arcade machine
    dy = gametwo.y - player_pos[1] / TILE_SIZE # Calculate the difference in y coordinates between the player and the arcade machine
    distance = math.sqrt(dx ** 2 + dy ** 2) # Calculate the distance between the player and the arcade machine

    gametwoangle = math.atan2(dy, dx) # Calculate the angle between the player and the arcade machine
    rel_angle = gametwoangle - player_angle # Calculate the relative angle between the player and the arcade machine

    # Normalize the relative angle within the FOV
    while rel_angle > math.pi: # If the relative angle is greater than pi
        rel_angle -= 2 * math.pi   # Subtract 2pi from the relative angle
    while rel_angle < -math.pi: # If the relative angle is less than -pi
        rel_angle += 2 * math.pi  # Add 2pi to the relative angle

    # If the distance between the player and the arcade machine is less than the distance between the player and the wall
    if cast_ray(player_pos[0], player_pos[1], gametwoangle)[0] / TILE_SIZE > distance:
        # Normalize the relative angle within the FOV
        relative_angle_within_fov = (rel_angle + FOV / 2) / FOV

        screen_x = relative_angle_within_fov * WIDTH # Calculate the x coordinate of the arcade machine on the screen

        # If the x coordinate of the arcade machine is within the screen
        if 0 <= screen_x <= WIDTH:
            # Draw the png to the screen
            scaled_width = gametwoimage.get_rect().width  / distance
            scaled_height = gametwoimage.get_rect().height  / distance
            scaled_image = pygame.transform.scale(gametwoimage, (int(scaled_width), int(scaled_height)))

            # Draw the image onto the screen at the updated rect position
            screen.blit(scaled_image, (screen_x - scaled_width / 2, HEIGHT // 2 - scaled_height / 2,
                                       scaled_width / distance, scaled_height / distance))
def RenderGameThree():
    ##Game Three Rendering
    ########################################
    dx = gamethree.x - player_pos[0] / TILE_SIZE # Calculate the difference in x coordinates between the player and the arcade machine
    dy = gamethree.y - player_pos[1] / TILE_SIZE # Calculate the difference in y coordinates between the player and the arcade machine
    distance = math.sqrt(dx ** 2 + dy ** 2) # Calculate the distance between the player and the arcade machine

    gamethreeangle = math.atan2(dy, dx) # Calculate the angle between the player and the arcade machine
    rel_angle = gamethreeangle - player_angle # Calculate the relative angle between the player and the arcade machine

    # Normalize the relative angle within the FOV
    while rel_angle > math.pi: # If the relative angle is greater than pi
        rel_angle -= 2 * math.pi  # Subtract 2pi from the relative angle
    while rel_angle < -math.pi: # If the relative angle is less than -pi
        rel_angle += 2 * math.pi # Add 2pi to the relative angle

    # If the distance between the player and the arcade machine is less than the distance between the player and the wall
    if cast_ray(player_pos[0], player_pos[1], gamethreeangle)[0] / TILE_SIZE > distance:
        # Normalize the relative angle within the FOV
        relative_angle_within_fov = (rel_angle + FOV / 2) / FOV

        screen_x = relative_angle_within_fov * WIDTH # Calculate the x coordinate of the arcade machine on the screen

        # If the x coordinate of the arcade machine is within the screen
        if 0 <= screen_x <= WIDTH:
            # Draw the png to the screen
            scaled_width = gamethreeimage.get_rect().width  / distance
            scaled_height = gamethreeimage.get_rect().height  / distance
            scaled_image = pygame.transform.scale(gamethreeimage, (int(scaled_width), int(scaled_height)))

            # Draw the image onto the screen at the updated rect position
            screen.blit(scaled_image, (screen_x - scaled_width / 2, HEIGHT // 2 - scaled_height / 2,
                                       scaled_width / distance, scaled_height / distance))
    #########################################

# Pygame settings
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Set the screen size
pygame.display.set_caption("3D Arcade") # Set the caption of the window
clock = pygame.time.Clock() # Create a clock object

# Function to cast a ray
def cast_ray(x, y, angle):
    while True: # Infinite loop
        x += math.cos(angle) # Increment x by cos(angle)
        y += math.sin(angle) # Increment y by sin(angle)

        # If the ray hits a wall, where the wall is an index in the map grid greater than 0
        if 0 <= x // TILE_SIZE < len(map_grid[0]) and 0 <= y // TILE_SIZE < len(map_grid):
            if map_grid[int(y) // TILE_SIZE][int(x) // TILE_SIZE] > 0:
                dist = math.sqrt((x - player_pos[0]) ** 2 + (y - player_pos[1]) ** 2)
                dist *= math.cos(player_angle - angle)
                return [dist, map_grid[int(y) // TILE_SIZE][int(x) // TILE_SIZE]] # Return the distance and the wall index
        else:
            return float('inf') # Return infinity if the ray does not hit a wall

# Function to check if a wall is at a given position
def is_wall(x, y):
    # If the position is within the map grid
    if 0 <= x // TILE_SIZE < len(map_grid[0]) and 0 <= y // TILE_SIZE < len(map_grid):
        return map_grid[int(y) // TILE_SIZE][int(x) // TILE_SIZE] == 1 # Return True if the wall index is 1 and false otherwise
    return True

# Function to render the game
def render():
    # Loop through each ray, cast the ray, and draw the wall
    for ray in range(NUM_RAYS):
        ray_angle = player_angle - HALF_FOV + RAY_ANGLE * ray # Calculate the angle of the ray
        cast_ray_dat = cast_ray(player_pos[0], player_pos[1], ray_angle) # Cast the ray
        dist = cast_ray_dat[0] # Get the distance from the cast_ray function
        height = cast_ray_dat[1] # Get the wall index from the cast_ray function

        if VIEW_DIST / dist >= 0 and VIEW_DIST / dist <= 1: # If the distance is within the view distance
            if dist != float('inf'): # If the distance is not infinity
                wall_height = TILE_SIZE * DIST_TO_PROJ / dist # Calculate the height of the wall
                # Draw a rectangle on the screen
                pygame.draw.rect(screen, 
                                 [int(255 * VIEW_DIST / dist), int(255 * VIEW_DIST / dist), # The color of the rectangle is calculated based on the distance
                                        int(255 * VIEW_DIST / dist)], (
                                     ray * WIDTH // NUM_RAYS,
                                     HEIGHT // 2 - (wall_height // 2) - (height // 2 * wall_height), # The y coordinate of the rectangle is calculated based on the height of the wall
                                     WIDTH // NUM_RAYS + 1, wall_height * height)) 
        else: # If the distance is not within the view distance
            if dist != float('inf'): # If the distance is not infinity
                wall_height = TILE_SIZE * DIST_TO_PROJ / dist  # Calculate the height of the wall
                pygame.draw.rect(screen,
                                 [255, 255, 255], (
                                     ray * WIDTH // NUM_RAYS,
                                     HEIGHT // 2 - (wall_height // 2) - (height // 2 * wall_height),
                                     WIDTH // NUM_RAYS + 1, wall_height * height)) # Draw a white rectangle on the screen with the following parameters: (screen, color, (x, y, width, height))

    dx1 = gameone.x - player_pos[0] / TILE_SIZE # Calculate the difference in x coordinates between the player and the arcade machine
    dy1 = gameone.y - player_pos[1] / TILE_SIZE # Calculate the difference in y coordinates between the player and the arcade machine
    distance1 = math.sqrt(dx1 ** 2 + dy1 ** 2) # Calculate the distance between the player and the arcade machine

    dx2 = gametwo.x - player_pos[0] / TILE_SIZE # Calculate the difference in x coordinates between the player and the arcade machine
    dy2 = gametwo.y - player_pos[1] / TILE_SIZE # Calculate the difference in y coordinates between the player and the arcade machine
    distance2 = math.sqrt(dx2 ** 2 + dy2 ** 2) # Calculate the distance between the player and the arcade machine

    dx3 = gamethree.x - player_pos[0] / TILE_SIZE # Calculate the difference in x coordinates between the player and the arcade machine
    dy3 = gamethree.y - player_pos[1] / TILE_SIZE # Calculate the difference in y coordinates between the player and the arcade machine
    distance3 = math.sqrt(dx3 ** 2 + dy3 ** 2) # Calculate the distance between the player and the arcade machine

    if distance1 > distance2 > distance3: # If the distance between the player and the arcade machine is greater than the distance between the player and the wall
        RenderGameOne() # Render the first arcade machine
        RenderGameTwo() # Render the second arcade machine
        RenderGameThree() # Render the third arcade machine
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

running = True # Variable to check if the game is running
maze_running = False # Variable to check if the maze is running

pygame.mouse.set_visible(False) # Hide the mouse cursor

while running: # Main game loop
    pygame.display.set_caption(f'{clock.get_fps() : .1f}') # Set the caption of the window to the FPS
    delta_time = clock.tick(FPS) / 25

    for event in pygame.event.get(): # Loop through each event
        if event.type == pygame.QUIT: # If the event is a quit event
            running = False # Set running to False

    keys = pygame.key.get_pressed() # Get the keys that are pressed

    # If the player presses h
    if keys[pygame.K_h]:
        map_grid = map_grid_challenge # Set the map grid to the challenge map grid
        gameone.x = gameone_hard_pos[0] # Set the x coordinate of the first arcade machine to the x coordinate of the first arcade machine in the challenge map
        gameone.y = gameone_hard_pos[1]  # Set the y coordinate of the first arcade machine to the y coordinate of the first arcade machine in the challenge map
        gametwo.x = gametwo_hard_pos[0] # Set the x coordinate of the second arcade machine to the x coordinate of the second arcade machine in the challenge map
        gametwo.y = gametwo_hard_pos[1] # Set the y coordinate of the second arcade machine to the y coordinate of the second arcade machine in the challenge map
        gamethree.x = gamethree_hard_pos[0] # Set the x coordinate of the third arcade machine to the x coordinate of the third arcade machine in the challenge map
        gamethree.y = gamethree_hard_pos[1] # Set the y coordinate of the third arcade machine to the y coordinate of the third arcade machine in the challenge map
        maze_running = True
    if keys[pygame.K_e]: # If the player presses e
        map_grid = map_grid_easy # Set the map grid to the easy map grid
        gameone.x = gameone_easy_pos[0]
        gameone.y = gameone_easy_pos[1]
        gametwo.x = gametwo_easy_pos[0]
        gametwo.y = gametwo_easy_pos[1]
        gamethree.x = gamethree_easy_pos[0]
        gamethree.y = gamethree_easy_pos[1]
        maze_running = True
    if keys[pygame.K_a]: # If the player presses a
        map_grid = map_grid_arcade # Set the map grid to the easy map grid
        gameone.x = gameone_arcade_pos[0]
        gameone.y = gameone_arcade_pos[1]
        gametwo.x = gametwo_arcade_pos[0]
        gametwo.y = gametwo_arcade_pos[1]
        gamethree.x = gamethree_arcade_pos[0]
        gamethree.y = gamethree_arcade_pos[1]
        maze_running = True

    # Maze game loop
    while maze_running:
        pygame.display.set_caption(f'{clock.get_fps() : .1f}') # Set the caption of the window to the FPS
        delta_time = clock.tick(FPS) / 25

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If the event is a quit event, set running to False, and maze_running to False
                running = False
                maze_running = False

        keys = pygame.key.get_pressed()

        # Player movement, and collision detection
        new_x = player_pos[0] + math.cos(player_angle) * SPEED * delta_time * (keys[pygame.K_w] - keys[pygame.K_s]) # Calculate the new x coordinate of the player
        new_y = player_pos[1] 
        if not is_wall(new_x, new_y):
            player_pos[0] = new_x # Set the x coordinate of the player to the new x coordinate

        new_x = player_pos[0] 
        new_y = player_pos[1] + math.sin(player_angle) * SPEED * delta_time * (keys[pygame.K_w] - keys[pygame.K_s]) # Calculate the new y coordinate of the player
        if not is_wall(new_x, new_y):
            player_pos[1] = new_y # Set the y coordinate of the player to the new y coordinate

        if keys[pygame.K_a]: # If the player presses a
            player_angle -= TURN_SPEED * delta_time # Decrement the player angle by the turn speed
        if keys[pygame.K_d]: # If the player presses d
            player_angle += TURN_SPEED * delta_time # Increment the player angle by the turn speed

        # If the player presses escape
        if keys[pygame.K_ESCAPE] and gameonejustin == False and gametwojustin == False and gamethreejustin == False:
            # Reset Player
            player_pos = [1 * TILE_SIZE, 1 * TILE_SIZE] # Set the player position to the starting position
            player_angle = 0 # Set the player angle to 0
            maze_running = False # Set maze_running to False
        elif keys[pygame.K_ESCAPE] == False:
            # Reset because this means we just exited one of the arcade games adn there is an overlapping escape press event
            gameonejustin = False
            gametwojustin = False
            gamethreejustin = False

        # Update game state and render
        screen.fill(BLACK)
        render()

        dx1 = gameone.x - player_pos[0] / TILE_SIZE # Calculate the difference in x coordinates between the player and the arcade machine
        dy1 = gameone.y - player_pos[1] / TILE_SIZE # Calculate the difference in y coordinates between the player and the arcade machine
        distance1 = math.sqrt(dx1 ** 2 + dy1 ** 2) # Calculate the distance between the player and the arcade machine

        if (distance1 < 1): # If the distance between the player and the arcade machine is less than 1
            # Prompt the player to enter the game with rendered text
            pygame.draw.rect(screen, "white", (WIDTH // 2 - 210, HEIGHT // 2 - 15, 420, 30))
            text_surface = font.render("Press F To Enter The Snake Game", True, "black")
            text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            screen.blit(text_surface, text_rect)
            if keys[pygame.K_f]: # If the player presses f
                GameOne() # Run Game One

        dx2 = gametwo.x - player_pos[0] / TILE_SIZE # Calculate the difference in x coordinates between the player and the arcade machine
        dy2 = gametwo.y - player_pos[1] / TILE_SIZE # Calculate the difference in y coordinates between the player and the arcade machine
        distance2 = math.sqrt(dx2 ** 2 + dy2 ** 2) # Calculate the distance between the player and the arcade machine

        if (distance2 < 1): # If the distance between the player and the arcade machine is less than 1
            # Prompt the player to enter the game with rendered text
            pygame.draw.rect(screen, "white", (WIDTH // 2 - 250, HEIGHT // 2 - 15, 500, 30))
            text_surface = font.render("Press F To Enter The Rubiks Cube Game", True, "black")
            text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            screen.blit(text_surface, text_rect)
            if keys[pygame.K_f]: # If the player presses f
                GameTwo() # Run Game Two

        dx3 = gamethree.x - player_pos[0] / TILE_SIZE # Calculate the difference in x coordinates between the player and the arcade machine
        dy3 = gamethree.y - player_pos[1] / TILE_SIZE # Calculate the difference in y coordinates between the player and the arcade machine
        distance3 = math.sqrt(dx3 ** 2 + dy3 ** 2) # Calculate the distance between the player and the arcade machine

        if (distance3 < 1): # If the distance between the player and the arcade machine is less than 1
            # Prompt the player to enter the game with rendered text
            pygame.draw.rect(screen, "white", (WIDTH // 2 - 250, HEIGHT // 2 - 15, 500, 30))
            text_surface = font.render("Press F To Enter The Minefield Game", True, "black")
            text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            screen.blit(text_surface, text_rect)
            if keys[pygame.K_f]: # If the player presses f
                GameThree() # Run Game Three

        pygame.draw.rect(screen, "white", (0,0,350,30))
        text_surface = font.render("Press ESC To Exit The Maze", True, "black") # Render text to prompt the player to exit the maze
        screen.blit(text_surface, (3,3))

        pygame.display.flip() # Update the display

    screen.fill(BLACK) # Fill the screen with black

    # Render text to prompt the player to enter the challenging maze
    text_surface = font.render("Press H To Enter The Challenge Maze", True, "white")
    text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 50))
    screen.blit(text_surface, text_rect)
    
    # Render text to prompt the player to enter the easy maze
    text_surface = font.render("Press E To Enter The Easy Maze", True, "white")
    text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    screen.blit(text_surface, text_rect)

    # Render text to prompt the player to enter the easy maze
    text_surface = font.render("Press A To Enter The Arcade", True, "white")
    text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))
    screen.blit(text_surface, text_rect)

    pygame.display.flip() # Update the display

pygame.quit() # Quit pygame
