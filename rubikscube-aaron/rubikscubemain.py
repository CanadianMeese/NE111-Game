import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup and font
font = pygame.font.Font(None, 36)
titleFont = pygame.font.Font(None, 72)
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Colors (red, green, blue)
red = (255, 0, 0)
white = (255, 255, 255)
orange = (255, 95, 5)
yellow = (255, 245, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# Cube faces setup
rFace = [red] * 9
uFace = [white] * 9
lFace = [orange] * 9
dFace = [yellow] * 9
fFace = [green] * 9
bFace = [blue] * 9
solvedCube = [rFace, uFace, lFace, dFace, fFace, bFace]
cube = solvedCube
def scramble(cube):
    move_functions = [right, left, up, down, back, front]

    for _ in range(30):
        move = random.choice(move_functions)
        cube = move(cube)

    return cube
def generateArcadeSequence(length=50):
    base_moves = ['R', 'L', 'U', 'D', 'F', 'B']
    sequence = []
    last_move = None
    second_last_move = None

    for _ in range(length):
        available_moves = base_moves.copy()

        # Remove inverse of last move to avoid direct cancellation
        if last_move:
            inverse_move = last_move[0] + ("'" if last_move[-1] != "'" else "")
            if inverse_move in available_moves:
                available_moves.remove(inverse_move)

            # Remove moves that would cause indirect cancellation without layer interaction
            if second_last_move and (last_move[0] in ['R', 'L'] and second_last_move[0] in ['R', 'L'] or
                                     last_move[0] in ['U', 'D'] and second_last_move[0] in ['U', 'D'] or
                                     last_move[0] in ['F', 'B'] and second_last_move[0] in ['F', 'B']):
                if second_last_move[0] in available_moves:
                    available_moves.remove(second_last_move[0])

        move = random.choice(available_moves)
        is_prime = random.choice([True, False])
        full_move = move + "'" if is_prime else move

        # Correct direct cancellations
        if last_move and full_move[0] == last_move[0] and \
           ((full_move[-1] == "'" and last_move[-1] != "'") or (full_move[-1] != "'" and last_move[-1] == "'")):
            full_move = last_move  # Duplicate the last move to avoid direct cancellation

        # Update last moves
        second_last_move = last_move
        last_move = full_move

        sequence.append(full_move)

    return sequence
def rotateCubeUp(rCube):
    tempLFace =[rCube[2][2],rCube[2][5],rCube[2][8],rCube[2][1],rCube[2][4],rCube[2][7],rCube[2][0],rCube[2][3],rCube[2][6]]
    tempRFace =[rCube[0][6],rCube[0][3],rCube[0][0],rCube[0][7],rCube[0][4],rCube[0][1],rCube[0][8],rCube[0][5],rCube[0][2]]
    tempBFace = [rCube[1][8], rCube[1][7], rCube[1][6], rCube[1][5], rCube[1][4], rCube[1][3], rCube[1][2], rCube[1][1],rCube[1][0]]
    tempDFace = [rCube[5][8], rCube[5][7], rCube[5][6], rCube[5][5], rCube[5][4], rCube[5][3], rCube[5][2], rCube[5][1],rCube[5][0]]
    tempCube = [tempRFace,rCube[4],tempLFace,tempDFace,rCube[3],tempBFace]
    return(tempCube)
def rotateCubeRight(rCube):
    tempUFace =[rCube[1][2],rCube[1][5],rCube[1][8],rCube[1][1],rCube[1][4],rCube[1][7],rCube[1][0],rCube[1][3],rCube[1][6]]
    tempDFace = [rCube[3][6], rCube[3][3], rCube[3][0], rCube[3][7], rCube[3][4], rCube[3][1], rCube[3][8], rCube[3][5],rCube[3][2]]
    tempCube = [rCube[4],tempUFace,rCube[5],tempDFace,rCube[2],rCube[0]]
    return(tempCube)
def right(rCube):
   tempCube = [list(row) for row in rCube]
   tempCube[4][2] = rCube[3][2]
   tempCube[4][5] = rCube[3][5]
   tempCube[4][8] = rCube[3][8]
   tempCube[3][2] = rCube[5][6]
   tempCube[3][5] = rCube[5][3]
   tempCube[3][8] = rCube[5][0]
   tempCube[5][6] = rCube[1][2]
   tempCube[5][3] = rCube[1][5]
   tempCube[5][0] = rCube[1][8]
   tempCube[1][2] = rCube[4][2]
   tempCube[1][5] = rCube[4][5]
   tempCube[1][8] = rCube[4][8]
   tempCube[0][0] = rCube[0][6]
   tempCube[0][1] = rCube[0][3]
   tempCube[0][2] = rCube[0][0]
   tempCube[0][3] = rCube[0][7]
   tempCube[0][5] = rCube[0][1]
   tempCube[0][6] = rCube[0][8]
   tempCube[0][7] = rCube[0][5]
   tempCube[0][8] = rCube[0][2]
   return(tempCube)


def back(rCube):
   tempCube = [list(row) for row in rCube]
   tempCube[5][2] = rCube[5][0]
   tempCube[5][5] = rCube[5][1]
   tempCube[5][8] = rCube[5][2]
   tempCube[5][7] = rCube[5][5]
   tempCube[5][6] = rCube[5][8]
   tempCube[5][3] = rCube[5][7]
   tempCube[5][0] = rCube[5][6]
   tempCube[5][1] = rCube[5][3]
   tempCube[0][2] = rCube[3][8]
   tempCube[0][5] = rCube[3][7]
   tempCube[0][8] = rCube[3][6]
   tempCube[3][6] = rCube[2][0]
   tempCube[3][7] = rCube[2][3]
   tempCube[3][8] = rCube[2][6]
   tempCube[2][0] = rCube[1][2]
   tempCube[2][3] = rCube[1][1]
   tempCube[2][6] = rCube[1][0]
   tempCube[1][0] = rCube[0][2]
   tempCube[1][1] = rCube[0][5]
   tempCube[1][2] = rCube[0][8]
   return(tempCube)


def down(rCube):
   tempCube = [list(row) for row in rCube]
   tempCube[3][0] = rCube[3][6]
   tempCube[3][1] = rCube[3][3]
   tempCube[3][2] = rCube[3][0]
   tempCube[3][5] = rCube[3][1]
   tempCube[3][8] = rCube[3][2]
   tempCube[3][7] = rCube[3][5]
   tempCube[3][6] = rCube[3][8]
   tempCube[3][3] = rCube[3][7]
   tempCube[4][6] = rCube[2][6]
   tempCube[4][7] = rCube[2][7]
   tempCube[4][8] = rCube[2][8]
   tempCube[0][6] = rCube[4][6]
   tempCube[0][7] = rCube[4][7]
   tempCube[0][8] = rCube[4][8]
   tempCube[5][6] = rCube[0][6]
   tempCube[5][7] = rCube[0][7]
   tempCube[5][8] = rCube[0][8]
   tempCube[2][6] = rCube[5][6]
   tempCube[2][7] = rCube[5][7]
   tempCube[2][8] = rCube[5][8]
   return(tempCube)
def left(rCube):
   tempCube = [list(row) for row in rCube]
   tempCube[4][0] = rCube[1][0]
   tempCube[4][3] = rCube[1][3]
   tempCube[4][6] = rCube[1][6]
   tempCube[3][0] = rCube[4][0]
   tempCube[3][3] = rCube[4][3]
   tempCube[3][6] = rCube[4][6]
   tempCube[1][0] = rCube[5][8]
   tempCube[1][3] = rCube[5][5]
   tempCube[1][6] = rCube[5][2]
   tempCube[5][2] = rCube[3][6]
   tempCube[5][5] = rCube[3][3]
   tempCube[5][8] = rCube[3][0]
   tempCube[2][2] = rCube[2][0]
   tempCube[2][5] = rCube[2][1]
   tempCube[2][8] = rCube[2][2]
   tempCube[2][7] = rCube[2][5]
   tempCube[2][6] = rCube[2][8]
   tempCube[2][3] = rCube[2][7]
   tempCube[2][0] = rCube[2][6]
   tempCube[2][1] = rCube[2][3]
   return(tempCube)
def up(rCube):
   tempCube = [list(row) for row in rCube]
   tempCube[2][0] = rCube[4][0]
   tempCube[2][1] = rCube[4][1]
   tempCube[2][2] = rCube[4][2]
   tempCube[4][0] = rCube[0][0]
   tempCube[4][1] = rCube[0][1]
   tempCube[4][2] = rCube[0][2]
   tempCube[0][0] = rCube[5][0]
   tempCube[0][1] = rCube[5][1]
   tempCube[0][2] = rCube[5][2]
   tempCube[5][0] = rCube[2][0]
   tempCube[5][1] = rCube[2][1]
   tempCube[5][2] = rCube[2][2]
   tempCube[1][0] = rCube[1][6]
   tempCube[1][1] = rCube[1][3]
   tempCube[1][2] = rCube[1][0]
   tempCube[1][5] = rCube[1][1]
   tempCube[1][8] = rCube[1][2]
   tempCube[1][7] = rCube[1][5]
   tempCube[1][6] = rCube[1][8]
   tempCube[1][3] = rCube[1][7]
   return(tempCube)

def front(rCube):
    tempCube = [list(row) for row in rCube]
    tempCube[1][6] = rCube[2][8]
    tempCube[1][7] = rCube[2][5]
    tempCube[1][8] = rCube[2][2]
    tempCube[0][0] = rCube[1][6]
    tempCube[0][3] = rCube[1][7]
    tempCube[0][6] = rCube[1][8]
    tempCube[3][2] = rCube[0][0]
    tempCube[3][1] = rCube[0][3]
    tempCube[3][0] = rCube[0][6]
    tempCube[2][8] = rCube[3][2]
    tempCube[2][5] = rCube[3][1]
    tempCube[2][2] = rCube[3][0]
    tempCube[4][0] = rCube[4][6]
    tempCube[4][1] = rCube[4][3]
    tempCube[4][2] = rCube[4][0]
    tempCube[4][5] = rCube[4][1]
    tempCube[4][8] = rCube[4][2]
    tempCube[4][7] = rCube[4][5]
    tempCube[4][6] = rCube[4][8]
    tempCube[4][3] = rCube[4][7]
    return(tempCube)
cube40 = pygame.Rect((300,250,50,50))
cube41 = pygame.Rect((355,250,50,50))
cube42 = pygame.Rect((410,250,50,50))
cube43 = pygame.Rect((300,305,50,50))
cube44 = pygame.Rect((355,305,50,50))
cube45 = pygame.Rect((410,305,50,50))
cube46 = pygame.Rect((300,360,50,50))
cube47 = pygame.Rect((355,360,50,50))
cube48 = pygame.Rect((410,360,50,50))
cube00 = pygame.Rect((300,250,50,50))
cube01 = pygame.Rect((360,250,50,50))
cube02 = pygame.Rect((420,250,50,50))
cube03 = pygame.Rect((300,310,50,50))
cube04 = pygame.Rect((360,310,50,50))
cube05 = pygame.Rect((420,310,50,50))
cube06 = pygame.Rect((300,370,50,50))
cube07 = pygame.Rect((360,370,50,50))
cube08 = pygame.Rect((420,370,50,50))
def rfacecube(x,y):
    return([(x,y),(x+11,y-22),(x+11,y+25),(x,y+50)])
def ufacecube(x,y):
    return([(x,y),(x+12,y-26),(x+61,y-26),(x+49,y)])

in_start_screen = True
in_solver = False
game_running = True

# Function to draw the cube
def drawCube():
    pygame.draw.rect(screen, cube[4][0], cube40)
    pygame.draw.rect(screen, cube[4][1], cube41)
    pygame.draw.rect(screen, cube[4][2], cube42)
    pygame.draw.rect(screen, cube[4][3], cube43)
    pygame.draw.rect(screen, cube[4][4], cube44)
    pygame.draw.rect(screen, cube[4][5], cube45)
    pygame.draw.rect(screen, cube[4][6], cube46)
    pygame.draw.rect(screen, cube[4][7], cube47)
    pygame.draw.rect(screen, cube[4][8], cube48)

    pygame.draw.polygon(screen, cube[0][0], rfacecube(460, 250))
    pygame.draw.polygon(screen, cube[0][1], rfacecube(475, 218))
    pygame.draw.polygon(screen, cube[0][2], rfacecube(490, 186))
    pygame.draw.polygon(screen, cube[0][3], rfacecube(460, 304))
    pygame.draw.polygon(screen, cube[0][4], rfacecube(475, 218+54))
    pygame.draw.polygon(screen, cube[0][5], rfacecube(490, 186+54))
    pygame.draw.polygon(screen, cube[0][6], rfacecube(460, 250+108))
    pygame.draw.polygon(screen, cube[0][7], rfacecube(475, 218+108))
    pygame.draw.polygon(screen, cube[0][8], rfacecube(490, 186+108))
    pygame.draw.polygon(screen, cube[1][6], ufacecube(300,250))
    pygame.draw.polygon(screen, cube[1][7], ufacecube(355,250))
    pygame.draw.polygon(screen, cube[1][8], ufacecube(410, 250))
    pygame.draw.polygon(screen, cube[1][3], ufacecube(314, 250-30))
    pygame.draw.polygon(screen, cube[1][4], ufacecube(369, 250-30))
    pygame.draw.polygon(screen, cube[1][5], ufacecube(424, 250-30))
    pygame.draw.polygon(screen, cube[1][0], ufacecube(328, 250-60))
    pygame.draw.polygon(screen, cube[1][1], ufacecube(383, 250-60))
    pygame.draw.polygon(screen, cube[1][2], ufacecube(438, 250-60))

    return None
def orientCube(c):
    if (c[1][4] != white and c[3][4] != white):
        while c[4][4] != white:
            c = rotateCubeRight(c)
        c = rotateCubeUp(c)
    elif c[3][4] == white:
        c = rotateCubeUp(rotateCubeUp(c))
    while c[4][4] != green:
        c = rotateCubeRight(c)
    return c
def draw_controls(screen, font):
    controls_text = [
        "Controls:",
        "Rotate Right Face: Press 'R'",
        "Rotate Left Face: Press 'L'",
        "Rotate Up Face: Press 'U'",
        "Rotate Down Face: Press 'D'",
        "Rotate Front Face: Press 'F'",
        "Rotate Back Face: Press 'B'",
        "Scramble Cube: Press 'S'",
        "Reset Cube to Solved State: Press Shift + 'S'",
        "By default, the direction of rotation will be clockwise",
        "Press Shift + 'R','L','U','D','F' or 'B' to rotate counter-clockwise",
        "Quit Game: Press the Escape key or close the window.",
        "                      Return to menu: Press Any Key"
    ]

    y_offset = 0
    for line in controls_text:
        text_surface = font.render(line, True, (255, 255, 255))  # White color
        screen.blit(text_surface, (50, 50 + y_offset))  # Adjust position as needed
        y_offset += 30
def start_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return 'game'
                elif event.key == pygame.K_i:
                    return 'instructions'
                elif event.key == pygame.K_a:
                    return 'arcade'

        screen.fill(black)
        # Drawing the start screen elements
        title = titleFont.render('Cube Town', True, white)
        title_rect = title.get_rect(center=(width / 2, height / 4))
        startPrompt = font.render('Press "Enter" to Start', True, white)
        startPrompt_rect = startPrompt.get_rect(center=(width / 2, height / 3))
        instructionsPrompt = font.render('Press "I" for Instructions', True, white)
        instructionsPrompt_rect = instructionsPrompt.get_rect(center=(width / 2, (height / 3) + 50))
        arcadePrompt = font.render('Press "A" for Arcade', True, white)
        arcadePrompt_rect = arcadePrompt.get_rect(center=(width / 2, (height / 3) + 100))
        screen.blit(title, title_rect)
        screen.blit(startPrompt, startPrompt_rect)
        screen.blit(instructionsPrompt, instructionsPrompt_rect)
        screen.blit(arcadePrompt, arcadePrompt_rect)

        pygame.display.update()

def draw_text(text, position, font, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)
def execute_move(cube, move):
    move_functions = {
        'R': right, 'R\'': lambda c: right(right(right(c))),
        'L': left, 'L\'': lambda c: left(left(left(c))),
        'U': up, 'U\'': lambda c: up(up(up(c))),
        'D': down, 'D\'': lambda c: down(down(down(c))),
        'F': front, 'F\'': lambda c: front(front(front(c))),
        'B': back, 'B\'': lambda c: back(back(back(c)))
    }
    return move_functions[move](cube)

# Main game loop
while game_running:
    if in_start_screen:
        result = start_screen()
        if result == 'quit':
            break
        elif result == 'game':
            in_start_screen = False
            in_solver = True
            in_arcade = False
        elif result == 'instructions':
            screen.fill(black)
            draw_controls(screen, font)
            pygame.display.update()
            # Wait for any key to return to the start screen
            pygame.event.clear()
            waiting_for_key = True
            while waiting_for_key:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                        waiting_for_key = False
            in_start_screen = True
            in_arcade = False
        elif result == 'arcade':
            roundStart = True
            round = 1
            in_arcade = True
            in_start_screen = False

    if in_solver:
        screen.fill(black) # Clear the screen before drawing the cube
        drawCube()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.KEYDOWN:
                # Handle key events for the game
                if event.key == pygame.K_ESCAPE:
                    cube = [row[:] for row in solvedCube]
                    in_solver = False
                    in_start_screen = True
                elif event.type == pygame.KEYDOWN:
                    mods = pygame.key.get_mods()

                    if event.key == pygame.K_r:
                        if mods & pygame.KMOD_SHIFT:
                            cube = right(right(right(cube)))
                        else:
                            cube = right(cube)

                    elif event.key == pygame.K_l:
                        if mods & pygame.KMOD_SHIFT:
                            cube = left(left(left(cube)))
                        else:
                            cube = left(cube)

                    elif event.key == pygame.K_d:
                        if mods & pygame.KMOD_SHIFT:
                            cube = down(down(down(cube)))
                        else:
                            cube = down(cube)

                    elif event.key == pygame.K_f:
                        if mods & pygame.KMOD_SHIFT:
                            cube = front(front(front(cube)))
                        else:
                            cube = front(cube)

                    elif event.key == pygame.K_u:
                        if mods & pygame.KMOD_SHIFT:
                            cube = up(up(up(cube)))
                        else:
                            cube = up(cube)

                    elif event.key == pygame.K_b:
                        if mods & pygame.KMOD_SHIFT:
                            cube = back(back(back(cube)))
                        else:
                            cube = back(cube)
                    elif event.key == pygame.K_y:
                        if mods & pygame.KMOD_SHIFT:
                            cube = rotateCubeUp(rotateCubeUp(rotateCubeUp(cube)))
                        else:
                            cube = rotateCubeUp(cube)
                    elif event.key == pygame.K_x:
                        if mods & pygame.KMOD_SHIFT:
                            cube = rotateCubeRight(rotateCubeRight(rotateCubeRight(cube)))
                        else:
                            cube = rotateCubeRight(cube)

                    elif event.key == pygame.K_s:
                        if mods & pygame.KMOD_SHIFT:
                            cube = solvedCube
                        else:
                            cube = scramble(cube)

        pygame.display.update()
    if in_arcade:
        screen.fill(black)
        drawCube()
        round_text = f"Round: {round}"
        draw_text(round_text, (10, 10), font)
        if roundStart:
            if round == 1:
                arcade_sequence = generateArcadeSequence(50)
                cube = solvedCube  # Start with a solved cube
            cube = [row[:] for row in solvedCube]
            for move in arcade_sequence[:round]:  # Execute moves up to the current round
                cube = execute_move(cube, move)
            roundStart = False
        if orientCube(cube) == solvedCube:
            round = round + 1
            roundStart = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.KEYDOWN:
                # Handle key events for the game
                if event.key == pygame.K_ESCAPE:
                    cube = [row[:] for row in solvedCube]
                    in_arcade = False
                    in_start_screen = True
                elif event.type == pygame.KEYDOWN:
                    mods = pygame.key.get_mods()

                    if event.key == pygame.K_r:
                        if mods & pygame.KMOD_SHIFT:
                            cube = right(right(right(cube)))
                        else:
                            cube = right(cube)

                    elif event.key == pygame.K_l:
                        if mods & pygame.KMOD_SHIFT:
                            cube = left(left(left(cube)))
                        else:
                            cube = left(cube)

                    elif event.key == pygame.K_d:
                        if mods & pygame.KMOD_SHIFT:
                            cube = down(down(down(cube)))
                        else:
                            cube = down(cube)

                    elif event.key == pygame.K_f:
                        if mods & pygame.KMOD_SHIFT:
                            cube = front(front(front(cube)))
                        else:
                            cube = front(cube)

                    elif event.key == pygame.K_u:
                        if mods & pygame.KMOD_SHIFT:
                            cube = up(up(up(cube)))
                        else:
                            cube = up(cube)

                    elif event.key == pygame.K_b:
                        if mods & pygame.KMOD_SHIFT:
                            cube = back(back(back(cube)))
                        else:
                            cube = back(cube)
                    elif event.key == pygame.K_y:
                        if mods & pygame.KMOD_SHIFT:
                            cube = rotateCubeUp(rotateCubeUp(rotateCubeUp(cube)))
                        else:
                            cube = rotateCubeUp(cube)
                    elif event.key == pygame.K_x:
                        if mods & pygame.KMOD_SHIFT:
                            cube = rotateCubeRight(rotateCubeRight(rotateCubeRight(cube)))
                        else:
                            cube = rotateCubeRight(cube)

                    elif event.key == pygame.K_s:
                        if mods & pygame.KMOD_SHIFT:
                            cube = solvedCube
                        else:
                            cube = scramble(cube)

        pygame.display.update()

pygame.quit()
