import pygame
import random

# Initialize Pygame, a library used for creating games and multimedia applications.
pygame.init()

# Setting up the screen dimensions and creating font objects for text display.
# 'None' as the font means Pygame will use a default font.
font = pygame.font.Font(None, 36)  # Font for regular text.
titleFont = pygame.font.Font(None, 72)  # Larger font for titles.
width, height = 800, 600  # Screen dimensions in pixels.
screen = pygame.display.set_mode((width, height))  # Create a window of the specified size.

# Define RGB color values for easy reference throughout the game.
red = (255, 0, 0)
white = (255, 255, 255)
orange = (255, 95, 5)
yellow = (255, 245, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# Initialize the cube's faces with default color values.
# Each face of the cube is represented by a list of 9 elements (3x3 grid).
rFace = [red] * 9  # Right face, initialized to all red.
uFace = [white] * 9  # Up face, initialized to all white.
lFace = [orange] * 9  # Left face, initialized to all orange.
dFace = [yellow] * 9  # Down face, initialized to all yellow.
fFace = [green] * 9  # Front face, initialized to all green.
bFace = [blue] * 9  # Back face, initialized to all blue.
solvedCube = [rFace, uFace, lFace, dFace, fFace, bFace]  # A solved cube state.
cube = solvedCube  # The current state of the cube.

# Function to scramble the cube.
def scramble(cube):
    # List of functions that represent possible moves on the cube.
    move_functions = [right, left, up, down, back, front]

    # Perform 30 random moves to scramble the cube.
    for _ in range(30):
        move = random.choice(move_functions)  # Choose a random move.
        cube = move(cube)  # Apply the move to the cube.

    return cube  # Return the scrambled cube.

def generateArcadeSequence(length=50):
    # Define the base moves for a Rubik's Cube. These are the standard moves.
    base_moves = ['R', 'L', 'U', 'D', 'F', 'B']

    # Initialize the sequence list to store the moves, and variables to track the last two moves.
    sequence = []
    last_move = None
    second_last_move = None

    # Generate a sequence of moves up to the specified length.
    for _ in range(length):
        # Copy the base moves to a new list to modify it without affecting the original list.
        available_moves = base_moves.copy()

        # To make the sequence more challenging, avoid moves that would undo the previous move.
        if last_move:
            # Calculate the inverse of the last move (e.g., 'R' becomes 'R'', and 'R'' becomes 'R').
            inverse_move = last_move[0] + ("'" if last_move[-1] != "'" else "")
            if inverse_move in available_moves:
                available_moves.remove(inverse_move)  # Remove the inverse move from available moves.

            # Avoid sequences that don't change the cube state significantly.
            # For example, avoid repeating the same layer move (like 'R' followed by 'L').
            if second_last_move and (last_move[0] in ['R', 'L'] and second_last_move[0] in ['R', 'L'] or
                                     last_move[0] in ['U', 'D'] and second_last_move[0] in ['U', 'D'] or
                                     last_move[0] in ['F', 'B'] and second_last_move[0] in ['F', 'B']):
                if second_last_move[0] in available_moves:
                    available_moves.remove(second_last_move[0])  # Remove the move to prevent indirect cancellations.

        # Randomly choose a move from the remaining available moves.
        move = random.choice(available_moves)
        # Randomly decide if the move should be prime (counter-clockwise) or not.
        is_prime = random.choice([True, False])
        full_move = move + "'" if is_prime else move

        # Check and correct direct cancellations (e.g., 'R' followed by 'R'').
        if last_move and full_move[0] == last_move[0] and \
           ((full_move[-1] == "'" and last_move[-1] != "'") or (full_move[-1] != "'" and last_move[-1] == "'")):
            full_move = last_move  # Keep the last move to avoid direct cancellation.

        # Update the tracking of the last two moves.
        second_last_move = last_move
        last_move = full_move

        # Add the chosen move to the sequence.
        sequence.append(full_move)

    # Return the complete sequence of moves.
    return sequence

def rotateCubeUp(rCube):
    # Rotates the entire cube upwards, affecting the position and orientation of all faces.

    # The left face becomes the new up face. The elements are rearranged to simulate a 90-degree rotation.
    tempLFace = [rCube[2][2], rCube[2][5], rCube[2][8], rCube[2][1], rCube[2][4],
                 rCube[2][7], rCube[2][0], rCube[2][3], rCube[2][6]]

    # The right face becomes the new down face, rotated 90 degrees.
    tempRFace = [rCube[0][6], rCube[0][3], rCube[0][0], rCube[0][7], rCube[0][4],
                 rCube[0][1], rCube[0][8], rCube[0][5], rCube[0][2]]

    # The back face becomes the new front face, requiring a 180-degree rotation.
    tempBFace = [rCube[1][8], rCube[1][7], rCube[1][6], rCube[1][5], rCube[1][4],
                 rCube[1][3], rCube[1][2], rCube[1][1], rCube[1][0]]

    # The down face becomes the new back face, rotated 180 degrees.
    tempDFace = [rCube[5][8], rCube[5][7], rCube[5][6], rCube[5][5], rCube[5][4],
                 rCube[5][3], rCube[5][2], rCube[5][1], rCube[5][0]]

    # Reassemble the cube with the updated faces.
    tempCube = [tempRFace, rCube[4], tempLFace, tempDFace, rCube[3], tempBFace]

    return tempCube

def rotateCubeRight(rCube):
    # Rotates the entire cube to the right, affecting the position and orientation of all faces.

    # The up face becomes the new right face, rearranged to simulate a 90-degree rotation.
    tempUFace = [rCube[1][2], rCube[1][5], rCube[1][8], rCube[1][1], rCube[1][4],
                 rCube[1][7], rCube[1][0], rCube[1][3], rCube[1][6]]

    # The down face becomes the new left face, rotated 90 degrees.
    tempDFace = [rCube[3][6], rCube[3][3], rCube[3][0], rCube[3][7], rCube[3][4],
                 rCube[3][1], rCube[3][8], rCube[3][5], rCube[3][2]]

    # Reassemble the cube with the updated faces.
    tempCube = [rCube[4], tempUFace, rCube[5], tempDFace, rCube[2], rCube[0]]

    return tempCube

def right(rCube):
    # Perform a right face rotation on the Rubik's Cube
    tempCube = [list(row) for row in rCube]

    # Rotate the right face (index 0) itself by 90 degrees clockwise.
    tempCube[0][0] = rCube[0][6]  # Bottom left to top left
    tempCube[0][1] = rCube[0][3]  # Middle left to top middle
    tempCube[0][2] = rCube[0][0]  # Top left to top right
    tempCube[0][3] = rCube[0][7]  # Bottom middle to middle left
    tempCube[0][5] = rCube[0][1]  # Top middle to middle right
    tempCube[0][6] = rCube[0][8]  # Bottom right to bottom left
    tempCube[0][7] = rCube[0][5]  # Middle right to bottom middle
    tempCube[0][8] = rCube[0][2]  # Top right to bottom right

    # Adjust the adjacent faces to the right face.
    tempCube[4][2] = rCube[3][2]  # Bottom right of Down to top right of Front
    tempCube[4][5] = rCube[3][5]  # Middle right of Down to middle right of Front
    tempCube[4][8] = rCube[3][8]  # Top right of Down to bottom right of Front
    tempCube[3][2] = rCube[5][6]  # Bottom left of Back to bottom right of Down
    tempCube[3][5] = rCube[5][3]  # Middle left of Back to middle right of Down
    tempCube[3][8] = rCube[5][0]  # Top left of Back to top right of Down
    tempCube[5][6] = rCube[1][2]  # Top right of Up to bottom left of Back
    tempCube[5][3] = rCube[1][5]  # Middle right of Up to middle left of Back
    tempCube[5][0] = rCube[1][8]  # Bottom right of Up to top left of Back
    tempCube[1][2] = rCube[4][2]  # Top right of Front to top right of Up
    tempCube[1][5] = rCube[4][5]  # Middle right of Front to middle right of Up
    tempCube[1][8] = rCube[4][8]  # Bottom right of Front to bottom right of Up

    return tempCube

def back(rCube):
    # Rotate the back face of the Rubik's Cube.
    tempCube = [list(row) for row in rCube]

    # Rotate the back face (index 5) itself by 90 degrees clockwise.
    tempCube[5][2] = rCube[5][0]  # Move top left to top right.
    tempCube[5][5] = rCube[5][1]  # Move middle left to middle right.
    tempCube[5][8] = rCube[5][2]  # Move bottom left to bottom right.
    tempCube[5][7] = rCube[5][5]  # Move bottom middle to middle left.
    tempCube[5][6] = rCube[5][8]  # Move bottom right to bottom left.
    tempCube[5][3] = rCube[5][7]  # Move middle right to bottom middle.
    tempCube[5][0] = rCube[5][6]  # Move top right to top left.
    tempCube[5][1] = rCube[5][3]  # Move top middle to middle left.

    # Adjust the adjacent faces to the back face.
    tempCube[0][2] = rCube[3][8]  # Move bottom right of Down face to top right of Right face.
    tempCube[0][5] = rCube[3][7]  # Move bottom middle of Down face to middle right of Right face.
    tempCube[0][8] = rCube[3][6]  # Move bottom left of Down face to bottom right of Right face.
    tempCube[3][6] = rCube[2][0]  # Move top left of Front face to bottom left of Down face.
    tempCube[3][7] = rCube[2][3]  # Move middle left of Front face to bottom middle of Down face.
    tempCube[3][8] = rCube[2][6]  # Move bottom left of Front face to bottom right of Down face.
    tempCube[2][0] = rCube[1][2]  # Move top right of Left face to top left of Front face.
    tempCube[2][3] = rCube[1][1]  # Move top middle of Left face to middle left of Front face.
    tempCube[2][6] = rCube[1][0]  # Move top left of Left face to bottom left of Front face.
    tempCube[1][0] = rCube[0][2]  # Move top right of Right face to top left of Left face.
    tempCube[1][1] = rCube[0][5]  # Move middle right of Right face to top middle of Left face.
    tempCube[1][2] = rCube[0][8]  # Move bottom right of Right face to top right of Left face.

    return tempCube

def down(rCube):
    # Rotate the down face of the Rubik's Cube.
    tempCube = [list(row) for row in rCube]

    # Rotate the down face (index 3) itself by 90 degrees clockwise.
    tempCube[3][0] = rCube[3][6]  # Move bottom left to top left.
    tempCube[3][1] = rCube[3][3]  # Move middle left to top middle.
    tempCube[3][2] = rCube[3][0]  # Move top left to top right.
    tempCube[3][5] = rCube[3][1]  # Move top middle to middle right.
    tempCube[3][8] = rCube[3][2]  # Move top right to bottom right.
    tempCube[3][7] = rCube[3][5]  # Move middle right to bottom middle.
    tempCube[3][6] = rCube[3][8]  # Move bottom right to bottom left.
    tempCube[3][3] = rCube[3][7]  # Move bottom middle to middle left.

    # Adjust the adjacent faces to the down face.
    tempCube[4][6] = rCube[2][6]  # Move bottom left of Front face to bottom left of Right face.
    tempCube[4][7] = rCube[2][7]  # Move bottom middle of Front face to bottom middle of Right face.
    tempCube[4][8] = rCube[2][8]  # Move bottom right of Front face to bottom right of Right face.
    tempCube[0][6] = rCube[4][6]  # Move bottom left of Right face to bottom left of Back face.
    tempCube[0][7] = rCube[4][7]  # Move bottom middle of Right face to bottom middle of Back face.
    tempCube[0][8] = rCube[4][8]  # Move bottom right of Right face to bottom right of Back face.
    tempCube[5][6] = rCube[0][6]  # Move bottom left of Back face to bottom left of Left face.
    tempCube[5][7] = rCube[0][7]  # Move bottom middle of Back face to bottom middle of Left face.
    tempCube[5][8] = rCube[0][8]  # Move bottom right of Back face to bottom right of Left face.
    tempCube[2][6] = rCube[5][6]  # Move bottom left of Left face to bottom left of Front face.
    tempCube[2][7] = rCube[5][7]  # Move bottom middle of Left face to bottom middle of Front face.
    tempCube[2][8] = rCube[5][8]  # Move bottom right of Left face to bottom right of Front face.

    return tempCube

def left(rCube):
    # Rotate the left face of the Rubik's Cube.
    tempCube = [list(row) for row in rCube]

    # Adjust the adjacent faces to the left face.
    tempCube[4][0] = rCube[1][0]  # Move top left of Up face to top left of Front face.
    tempCube[4][3] = rCube[1][3]  # Move middle left of Up face to middle left of Front face.
    tempCube[4][6] = rCube[1][6]  # Move bottom left of Up face to bottom left of Front face.
    tempCube[3][0] = rCube[4][0]  # Move top left of Front face to top left of Down face.
    tempCube[3][3] = rCube[4][3]  # Move middle left of Front face to middle left of Down face.
    tempCube[3][6] = rCube[4][6]  # Move bottom left of Front face to bottom left of Down face.
    tempCube[1][0] = rCube[5][8]  # Move bottom right of Back face to top left of Up face.
    tempCube[1][3] = rCube[5][5]  # Move middle right of Back face to middle left of Up face.
    tempCube[1][6] = rCube[5][2]  # Move top right of Back face to bottom left of Up face.
    tempCube[5][2] = rCube[3][6]  # Move bottom left of Down face to top right of Back face.
    tempCube[5][5] = rCube[3][3]  # Move middle left of Down face to middle right of Back face.
    tempCube[5][8] = rCube[3][0]  # Move top left of Down face to bottom right of Back face.

    # Rotate the left face (index 2) itself by 90 degrees clockwise.
    tempCube[2][2] = rCube[2][0]  # Move top left to top right.
    tempCube[2][5] = rCube[2][1]  # Move middle left to middle right.
    tempCube[2][8] = rCube[2][2]  # Move bottom left to bottom right.
    tempCube[2][7] = rCube[2][5]  # Move bottom middle to middle left.
    tempCube[2][6] = rCube[2][8]  # Move bottom right to bottom left.
    tempCube[2][3] = rCube[2][7]  # Move middle right to bottom middle.
    tempCube[2][0] = rCube[2][6]  # Move top right to top left.
    tempCube[2][1] = rCube[2][3]  # Move top middle to middle left.

    return tempCube

def up(rCube):
    # Rotate the up face of the Rubik's Cube.
    tempCube = [list(row) for row in rCube]

    # Adjust the adjacent faces to the up face.
    tempCube[2][0] = rCube[4][0]  # Move top left of Front face to top left of Left face.
    tempCube[2][1] = rCube[4][1]  # Move top middle of Front face to top middle of Left face.
    tempCube[2][2] = rCube[4][2]  # Move top right of Front face to top right of Left face.
    tempCube[4][0] = rCube[0][0]  # Move top left of Right face to top left of Front face.
    tempCube[4][1] = rCube[0][1]  # Move top middle of Right face to top middle of Front face.
    tempCube[4][2] = rCube[0][2]  # Move top right of Right face to top right of Front face.
    tempCube[0][0] = rCube[5][0]  # Move top left of Back face to top left of Right face.
    tempCube[0][1] = rCube[5][1]  # Move top middle of Back face to top middle of Right face.
    tempCube[0][2] = rCube[5][2]  # Move top right of Back face to top right of Right face.
    tempCube[5][0] = rCube[2][0]  # Move top left of Left face to top left of Back face.
    tempCube[5][1] = rCube[2][1]  # Move top middle of Left face to top middle of Back face.
    tempCube[5][2] = rCube[2][2]  # Move top right of Left face to top right of Back face.

    # Rotate the up face (index 1) itself by 90 degrees clockwise.
    tempCube[1][0] = rCube[1][6]  # Move bottom left to top left.
    tempCube[1][1] = rCube[1][3]  # Move middle left to top middle.
    tempCube[1][2] = rCube[1][0]  # Move top left to top right.
    tempCube[1][5] = rCube[1][1]  # Move top middle to middle right.
    tempCube[1][8] = rCube[1][2]  # Move top right to bottom right.
    tempCube[1][7] = rCube[1][5]  # Move middle right to bottom middle.
    tempCube[1][6] = rCube[1][8]  # Move bottom right to bottom left.
    tempCube[1][3] = rCube[1][7]  # Move bottom middle to middle left.

    return tempCube

def front(rCube):
    # Rotate the front face of the Rubik's Cube.
    tempCube = [list(row) for row in rCube]

    # Adjust the adjacent faces to the front face.
    tempCube[1][6] = rCube[2][8]  # Move bottom right of Left face to bottom left of Up face.
    tempCube[1][7] = rCube[2][5]  # Move middle right of Left face to bottom middle of Up face.
    tempCube[1][8] = rCube[2][2]  # Move top right of Left face to bottom right of Up face.
    tempCube[0][0] = rCube[1][6]  # Move bottom left of Up face to top left of Right face.
    tempCube[0][3] = rCube[1][7]  # Move bottom middle of Up face to middle left of Right face.
    tempCube[0][6] = rCube[1][8]  # Move bottom right of Up face to bottom left of Right face.
    tempCube[3][2] = rCube[0][0]  # Move top left of Right face to top right of Down face.
    tempCube[3][1] = rCube[0][3]  # Move middle left of Right face to top middle of Down face.
    tempCube[3][0] = rCube[0][6]  # Move bottom left of Right face to top left of Down face.
    tempCube[2][8] = rCube[3][2]  # Move top right of Down face to bottom right of Left face.
    tempCube[2][5] = rCube[3][1]  # Move top middle of Down face to middle right of Left face.
    tempCube[2][2] = rCube[3][0]  # Move top left of Down face to top right of Left face.

    # Rotate the front face (index 4) itself by 90 degrees clockwise.
    tempCube[4][0] = rCube[4][6]  # Move bottom left to top left.
    tempCube[4][1] = rCube[4][3]  # Move middle left to top middle.
    tempCube[4][2] = rCube[4][0]  # Move top left to top right.
    tempCube[4][5] = rCube[4][1]  # Move top middle to middle right.
    tempCube[4][8] = rCube[4][2]  # Move top right to bottom right.
    tempCube[4][7] = rCube[4][5]  # Move middle right to bottom middle.
    tempCube[4][6] = rCube[4][8]  # Move bottom right to bottom left.
    tempCube[4][3] = rCube[4][7]  # Move bottom middle to middle left.

    return tempCube

# Define pygame.Rect objects for each square of the Rubik's Cube.
# These objects are used to draw the squares on the screen.
cube40 = pygame.Rect((300, 250, 50, 50))  # Define a square for the first position on the front face.
cube41 = pygame.Rect((355, 250, 50, 50))  # Define a square for the second position on the front face.
cube42 = pygame.Rect((410, 250, 50, 50))  # Define a square for the third position on the front face.
# Similar definitions for other squares on the front face
cube43 = pygame.Rect((300, 305, 50, 50))
cube44 = pygame.Rect((355, 305, 50, 50))
cube45 = pygame.Rect((410, 305, 50, 50))
cube46 = pygame.Rect((300, 360, 50, 50))
cube47 = pygame.Rect((355, 360, 50, 50))
cube48 = pygame.Rect((410, 360, 50, 50))

# Define pygame.Rect objects for each square of the right face of the Rubik's Cube.
cube00 = pygame.Rect((300, 250, 50, 50))  # First position on the right face.
cube01 = pygame.Rect((360, 250, 50, 50))  # Second position on the right face.
cube02 = pygame.Rect((420, 250, 50, 50))  # Third position on the right face.
# Similar definitions for other squares on the right face
cube03 = pygame.Rect((300, 310, 50, 50))
cube04 = pygame.Rect((360, 310, 50, 50))
cube05 = pygame.Rect((420, 310, 50, 50))
cube06 = pygame.Rect((300, 370, 50, 50))
cube07 = pygame.Rect((360, 370, 50, 50))
cube08 = pygame.Rect((420, 370, 50, 50))

# Functions to define points for drawing the polygons of the right and upper faces of the Rubik's Cube.
def rfacecube(x, y):
    # Returns the points to draw a polygon representing a square on the right face.
    return [(x, y), (x + 11, y - 22), (x + 11, y + 25), (x, y + 50)]

def ufacecube(x, y):
    # Returns the points to draw a polygon representing a square on the upper face.
    return [(x, y), (x + 12, y - 26), (x + 61, y - 26), (x + 49, y)]

# Variables to control the state of the game.
in_start_screen = True  # Indicates if the game is currently showing the start screen.
in_solver = False       # Indicates if the solver functionality is active.
game_running = True     # Controls the main game loop, set to False to exit the game.

def drawCube():
    # Draw the front face of the Rubik's Cube.
    # pygame.draw.rect is used to draw rectangles representing each square of the cube's face.
    pygame.draw.rect(screen, cube[4][0], cube40)  # Draw the first square of the front face.
    pygame.draw.rect(screen, cube[4][1], cube41)  # Draw the second square of the front face.
    pygame.draw.rect(screen, cube[4][2], cube42)  # Draw the third square of the front face.
    # Similar drawing calls for other squares on the front face
    pygame.draw.rect(screen, cube[4][3], cube43)
    pygame.draw.rect(screen, cube[4][4], cube44)
    pygame.draw.rect(screen, cube[4][5], cube45)
    pygame.draw.rect(screen, cube[4][6], cube46)
    pygame.draw.rect(screen, cube[4][7], cube47)
    pygame.draw.rect(screen, cube[4][8], cube48)

    # Draw the right face of the Rubik's Cube.
    # pygame.draw.polygon is used here because the right face is shown in perspective.
    pygame.draw.polygon(screen, cube[0][0], rfacecube(460, 250))  # Draw the first square of the right face.
    pygame.draw.polygon(screen, cube[0][1], rfacecube(475, 218))  # Draw the second square of the right face.
    pygame.draw.polygon(screen, cube[0][2], rfacecube(490, 186))  # Draw the third square of the right face.
    # Similar drawing calls for other squares on the right face
    pygame.draw.polygon(screen, cube[0][3], rfacecube(460, 304))
    pygame.draw.polygon(screen, cube[0][4], rfacecube(475, 218+54))
    pygame.draw.polygon(screen, cube[0][5], rfacecube(490, 186+54))
    pygame.draw.polygon(screen, cube[0][6], rfacecube(460, 250+108))
    pygame.draw.polygon(screen, cube[0][7], rfacecube(475, 218+108))
    pygame.draw.polygon(screen, cube[0][8], rfacecube(490, 186+108))

    # Draw the upper face of the Rubik's Cube.
    # The upper face is also shown in perspective and requires polygons.
    pygame.draw.polygon(screen, cube[1][6], ufacecube(300,250))  # Draw the first square of the upper face.
    pygame.draw.polygon(screen, cube[1][7], ufacecube(355,250))  # Draw the second square of the upper face.
    pygame.draw.polygon(screen, cube[1][8], ufacecube(410, 250))  # Draw the third square of the upper face.
    # Similar drawing calls for other squares on the upper face
    pygame.draw.polygon(screen, cube[1][3], ufacecube(314, 250-30))
    pygame.draw.polygon(screen, cube[1][4], ufacecube(369, 250-30))
    pygame.draw.polygon(screen, cube[1][5], ufacecube(424, 250-30))
    pygame.draw.polygon(screen, cube[1][0], ufacecube(328, 250-60))
    pygame.draw.polygon(screen, cube[1][1], ufacecube(383, 250-60))
    pygame.draw.polygon(screen, cube[1][2], ufacecube(438, 250-60))

    return None


def orientCube(c):
    # This function orients the cube so that the white center is on the Up (U) face
    # and the green center is on the Front (F) face.

    # Check if the Up or Down face does not have the white center.
    if (c[1][4] != white and c[3][4] != white):
        # Rotate the entire cube right until the white center is on the Up face.
        while c[4][4] != white:
            c = rotateCubeRight(c)
        # Rotate the cube up once to bring the white center to the Up face.
        c = rotateCubeUp(c)
    # If the white center is already on the Down face.
    elif c[3][4] == white:
        # Rotate the cube up twice to bring the white center to the Up face.
        c = rotateCubeUp(rotateCubeUp(c))
    # Rotate the entire cube right until the green center is on the Front face.
    while c[4][4] != green:
        c = rotateCubeRight(c)
    return c


def draw_controls(screen, font_size=24):
    # Initialize a font for rendering text.
    font = pygame.font.Font(None, font_size)

    # Text for the left column of the instructions screen.
    left_column_text = [
        "Welcome to Cube Town!",
        # Control instructions for rotating cube faces.
        "Rotate Cube Faces:",
        "  Right: 'R' (Counter-Clockwise: Shift + 'R')",
        "  Left: 'L' (Counter-Clockwise: Shift + 'L')",
        "  Up: 'U' (Counter-Clockwise: Shift + 'U')",
        "  Down: 'D' (Counter-Clockwise: Shift + 'D')",
        "  Front: 'F' (Counter-Clockwise: Shift + 'F')",
        "  Back: 'B' (Counter-Clockwise: Shift + 'B')",
        # Additional control instructions.
        "Additional Controls:",
        "  Scramble: 'S', Reset: Shift + 'S'",
        "  Rotate Up: 'Y' (Counter-Clockwise: Shift + 'Y')",
        "  Rotate Right: 'X' (Counter-Clockwise: Shift + 'X')"
    ]

    # Text for the right column of the instructions screen.
    right_column_text = [
        "Arcade Mode:",
        "  - Progressive challenge rounds.",
        "  - Each round with a new scramble.",
        "  - Solve to progress to next round.",
        "  - Difficulty increases each round.",
        # General instructions.
        "General:",
        "  Quit: Escape key or window close",
        "  Return to Menu: Any key",
        "Enjoy Cube Town!"
    ]

    # Set up positions and spacing for the text.
    column_width = screen.get_width() / 2
    line_spacing = font_size * 1.2  # Spacing slightly larger than font size.

    # Display the text in the left column.
    y_offset = 20
    for line in left_column_text:
        text_surface = font.render(line, True, (255, 255, 255))  # White color for text.
        screen.blit(text_surface, (20, y_offset))  # Position each line of text.
        y_offset += line_spacing

    # Display the text in the right column.
    y_offset = 20
    for line in right_column_text:
        text_surface = font.render(line, True, (255, 255, 255))  # White color for text.
        screen.blit(text_surface, (column_width, y_offset))  # Position each line of text.
        y_offset += line_spacing

def start_screen():
    # This function displays the start screen and handles user input for navigation.

    while True:
        # Process all events from the event queue.
        for event in pygame.event.get():
            # Check if the Quit event is triggered.
            if event.type == pygame.QUIT:
                return 'quit'  # Exit the start screen with a 'quit' signal.
            # Check for key presses.
            elif event.type == pygame.KEYDOWN:
                # Start the game if the Enter key is pressed.
                if event.key == pygame.K_RETURN:
                    return 'game'  # Exit the start screen with a 'game' signal to start the game.
                # Open instructions if the 'I' key is pressed.
                elif event.key == pygame.K_i:
                    return 'instructions'  # Exit with 'instructions' signal to show instructions.
                # Enter arcade mode if the 'A' key is pressed.
                elif event.key == pygame.K_a:
                    return 'arcade'  # Exit with 'arcade' signal to start the arcade mode.

        # Fill the screen with a black background.
        screen.fill(black)

        # Draw the start screen elements.
        # Render the game title.
        title = titleFont.render('Cube Town', True, white)
        title_rect = title.get_rect(center=(width / 2, height / 4))
        # Render the prompt to start the game.
        startPrompt = font.render('Press "Enter" to Start', True, white)
        startPrompt_rect = startPrompt.get_rect(center=(width / 2, height / 3))
        # Render the prompt for instructions.
        instructionsPrompt = font.render('Press "I" for Instructions', True, white)
        instructionsPrompt_rect = instructionsPrompt.get_rect(center=(width / 2, (height / 3) + 50))
        # Render the prompt for arcade mode.
        arcadePrompt = font.render('Press "A" for Arcade', True, white)
        arcadePrompt_rect = arcadePrompt.get_rect(center=(width / 2, (height / 3) + 100))

        # Display the rendered text on the screen.
        screen.blit(title, title_rect)
        screen.blit(startPrompt, startPrompt_rect)
        screen.blit(instructionsPrompt, instructionsPrompt_rect)
        screen.blit(arcadePrompt, arcadePrompt_rect)

        # Update the display to show the new frame.
        pygame.display.update()

def draw_text(text, position, font, color=(255, 255, 255)):
    # This function renders and draws text onto the screen.
    # text: The string of text to be rendered.
    # position: A tuple (x, y) specifying where on the screen to draw the text.
    # font: The pygame font object used to render the text.
    # color: The color of the text. Default is white.

    # Render the text using the specified font and color.
    text_surface = font.render(text, True, color)
    # Draw the rendered text onto the screen at the specified position.
    screen.blit(text_surface, position)

def execute_move(cube, move):
    # This function executes a specified move on the Rubik's Cube.
    # cube: The current state of the Rubik's Cube.
    # move: A string representing the move to be executed.

    # Define a dictionary mapping move strings to corresponding functions.
    # Each key is a move notation, and its value is the function that executes the move.
    # For counter-clockwise moves (denoted by an apostrophe), the function is called three times.
    move_functions = {
        'R': right, 'R\'': lambda c: right(right(right(c))),  # Right face rotations.
        'L': left, 'L\'': lambda c: left(left(left(c))),      # Left face rotations.
        'U': up, 'U\'': lambda c: up(up(up(c))),              # Up face rotations.
        'D': down, 'D\'': lambda c: down(down(down(c))),      # Down face rotations.
        'F': front, 'F\'': lambda c: front(front(front(c))),  # Front face rotations.
        'B': back, 'B\'': lambda c: back(back(back(c)))       # Back face rotations.
    }

    # Execute the specified move on the cube and return the new cube state.
    return move_functions[move](cube)

# Main game loop
while game_running:
    # Check if the game is currently on the start screen.
    if in_start_screen:
        # Display the start screen and get the user's choice.
        result = start_screen()

        # Determine the next action based on the user's choice.
        if result == 'quit':
            break  # Exit the game loop, effectively quitting the game.
        elif result == 'game':
            # Start the main game.
            in_start_screen = False  # Leave the start screen.
            in_solver = True        # Enter the solver mode.
            in_arcade = False       # Ensure arcade mode is not active.
        elif result == 'instructions':
            # Display the instructions screen.
            screen.fill(black)  # Fill the screen with black.
            draw_controls(screen, 25)  # Draw the controls instructions.
            pygame.display.update()  # Update the display to show the instructions.

            # Wait for any key press to return to the start screen.
            pygame.event.clear()  # Clear the event queue.
            waiting_for_key = True
            while waiting_for_key:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                        waiting_for_key = False  # Exit the waiting loop on key press or quit event.
            in_start_screen = True  # Return to the start screen.
            in_arcade = False       # Ensure arcade mode is not active.
        elif result == 'arcade':
            # Start the arcade mode.
            roundStart = True   # Flag to indicate the start of a new round.
            round = 1           # Initialize the round counter.
            in_arcade = True    # Enter arcade mode.
            in_start_screen = False  # Leave the start screen.

    if in_solver:
        # Clear the screen and prepare to draw the cube's current state.
        screen.fill(black)  # Fill the screen with black to clear it.
        drawCube()  # Draw the Rubik's Cube on the screen.

        # Process user input events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Stop the game if the quit event is triggered.
                game_running = False
            elif event.type == pygame.KEYDOWN:
                # Handle key events for interacting with the cube.

                # Exit the solver mode and return to the start screen.
                if event.key == pygame.K_ESCAPE:
                    cube = [row[:] for row in solvedCube]  # Reset the cube to its solved state.
                    in_solver = False  # Exit solver mode.
                    in_start_screen = True  # Return to the start screen.

                # Check if any modifier keys are pressed (like Shift).
                mods = pygame.key.get_mods()

                # Rotate the Rubik's Cube based on the key pressed.
                if event.key == pygame.K_r:
                    cube = right(cube) if not (mods & pygame.KMOD_SHIFT) else right(right(right(cube)))
                elif event.key == pygame.K_l:
                    cube = left(cube) if not (mods & pygame.KMOD_SHIFT) else left(left(left(cube)))
                elif event.key == pygame.K_d:
                    cube = down(cube) if not (mods & pygame.KMOD_SHIFT) else down(down(down(cube)))
                elif event.key == pygame.K_f:
                    cube = front(cube) if not (mods & pygame.KMOD_SHIFT) else front(front(front(cube)))
                elif event.key == pygame.K_u:
                    cube = up(cube) if not (mods & pygame.KMOD_SHIFT) else up(up(up(cube)))
                elif event.key == pygame.K_b:
                    cube = back(cube) if not (mods & pygame.KMOD_SHIFT) else back(back(back(cube)))

                # Rotate the entire cube up or right, based on the key pressed.
                elif event.key == pygame.K_y:
                    cube = rotateCubeUp(cube) if not (mods & pygame.KMOD_SHIFT) else rotateCubeUp(
                        rotateCubeUp(rotateCubeUp(cube)))
                elif event.key == pygame.K_x:
                    cube = rotateCubeRight(cube) if not (mods & pygame.KMOD_SHIFT) else rotateCubeRight(
                        rotateCubeRight(rotateCubeRight(cube)))

                # Scramble the cube or reset it to the solved state.
                elif event.key == pygame.K_s:
                    cube = scramble(cube) if not (mods & pygame.KMOD_SHIFT) else solvedCube

        pygame.display.update()

    if in_arcade:
        # Clear the screen and prepare to draw the cube's current state in arcade mode.
        screen.fill(black)  # Fill the screen with black to clear it.
        drawCube()  # Draw the Rubik's Cube on the screen.

        # Display the current round number.
        round_text = f"Round: {round}"
        draw_text(round_text, (10, 10), font)  # Draw the round number at the top-left of the screen.

        # Check if a new round has started.
        if roundStart:
            # Initialize the arcade sequence for the first round.
            if round == 1:
                arcade_sequence = generateArcadeSequence(50)  # Generate a sequence of moves.
                cube = solvedCube  # Start with a solved cube.
            # Reset the cube to its solved state before applying the moves for the current round.
            cube = [row[:] for row in solvedCube]
            # Execute the sequence of moves up to the current round.
            for move in arcade_sequence[:round]:
                cube = execute_move(cube, move)
            # Mark the start of the round as complete.
            roundStart = False

        # Check if the cube is solved to advance to the next round.
        if orientCube(cube) == solvedCube:
            round += 1  # Increment the round number.
            roundStart = True  # Flag the start of a new round.

        # Process user input events in arcade mode.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Stop the game if the quit event is triggered.
                game_running = False
            elif event.type == pygame.KEYDOWN:
                # Handle key events for interacting with the cube.

                # Exit the arcade mode and return to the start screen.
                if event.key == pygame.K_ESCAPE:
                    cube = [row[:] for row in solvedCube]  # Reset the cube to its solved state.
                    in_arcade = False  # Exit arcade mode.
                    in_start_screen = True  # Return to the start screen.

                # Check if any modifier keys are pressed (like Shift).
                mods = pygame.key.get_mods()

                # Rotate the Rubik's Cube based on the key pressed.
                # Similar key handling as in the solver mode.
                if event.key == pygame.K_r:
                    cube = right(cube) if not (mods & pygame.KMOD_SHIFT) else right(right(right(cube)))
                elif event.key == pygame.K_l:
                    cube = left(cube) if not (mods & pygame.KMOD_SHIFT) else left(left(left(cube)))
                elif event.key == pygame.K_u:
                    cube = up(cube) if not (mods & pygame.KMOD_SHIFT) else up(up(up(cube)))
                elif event.key == pygame.K_d:
                    cube = down(cube) if not (mods & pygame.KMOD_SHIFT) else down(down(down(cube)))
                elif event.key == pygame.K_f:
                    cube = front(cube) if not (mods & pygame.KMOD_SHIFT) else front(front(front(cube)))
                elif event.key == pygame.K_b:
                    cube = back(cube) if not (mods & pygame.KMOD_SHIFT) else back(back(back(cube)))
        # Update the display to show the new frame.
        pygame.display.update()

    # Quit Pygame when the game loop ends.
pygame.quit()
