# import relevant libraries
import pygame
import sys
import random
import math

width, height = 800, 600    # screen dimensions
Gray = (100, 100, 100)      # values for the colour gray
tiles_dug = 0   # count will increase as tiles are clicked resulting in win when all non-bomb tiles are cleared
easy_max_clear_count = 70   # number of non-bomb tiles in easy mode when clear tiles = max_clear_count player wins
med_max_clear_count = 198   # number of non-bomb tiles in medium mode when clear tiles = max_clear_count player wins
hard_max_clear_count = 381  # number of non-bomb tiles in hard mode when clear tiles = max_clear_count player wins
generatemap = False     # means the player has not made the first move, when player wins or loses generatemap = None
                        # prints the win or lose screen and allows player to return to start
win = 0     # win being 0 means player has not won nor lost yet 1 = win, 2 = lose
start = 0   # player has not started game until they click enter on the start screen
easy_rows = 8       # number of rows in the easy array
easy_cols = 10      # number of columns in the easy array
med_rows = 14       # number of rows in the medium array
med_cols = 17       # number of columns in the medium array
hard_rows = 16      # number of rows in the hard array
hard_cols = 30      # number of columns in the hard array
easy_bomb_max = 10      # max number of bombs that will print in easy mode
easy_flagcount = 10     # number of flags at the start of medium mode
med_bomb_max = 40       # max number of bombs that will print in medium mode
med_flagcount = 40      # number of flags at the start of medium mode
hard_bomb_max = 99      # max number of bombs that will print in hard mode
hard_flagcount = 99     # number of flags at the start of hard mode


def randomize_map(x, y):    # randomly places bombs after players first move (entry point (x, y))
    bomb_count = 0  # bomb_count is set to 0 and increases with every bomb placed until the max # of bombs are placed
    for vertical in range(rows):    # loop through each column
        for horizontal in range(cols):  # loop through each row
            if bomb_count < bomb_max:   # checks if the maximum amount of bombs has been reached
                # this if statement won't allow bombs to be placed in a 3 X 5 square centered around the first move
                # if the loop is at any of these points in the array it skips bomb making for this entry
                if (not (x == horizontal and y == vertical) and                 # first move
                        not (x - 1 == horizontal and y == vertical) and         # left of first move
                        not (x + 1 == horizontal and y == vertical) and         # right of first move
                        not (x == horizontal and y - 1 == vertical) and         # above first move
                        not (x + 1 == horizontal and y - 1 == vertical) and     # above and right of first move
                        not (x - 1 == horizontal and y - 1 == vertical) and     # above and left of first move
                        not (x == horizontal and y + 1 == vertical) and         # below first move
                        not (x + 1 == horizontal and y + 1 == vertical) and     # below and right of first move
                        not (x - 1 == horizontal and y + 1 == vertical) and     # below and left of first move
                        not (x - 1 == horizontal and y + 2 == vertical) and     # below 2 and to the left of first move
                        not (x == horizontal and y + 2 == vertical) and         # below 2 of first move
                        not (x + 1 == horizontal and y + 2 == vertical) and     # below 2 and to the right of first move
                        not (x - 1 == horizontal and y - 2 == vertical) and     # above 2 and to the left of first move
                        not (x + 1 == horizontal and y - 2 == vertical) and     # above 2 and to the right of first move
                        not (x == horizontal and y - 2 == vertical)):           # above 2 of first move

                    # this if statement does not allow a 3 X 3 box to form (bomb = 1)
                    # it checks if values to the left and above are bombs and if they are all bombs, bomb making skips
                    if ((gamearray[vertical - 1][horizontal] != 1) or          # above the entry
                            (gamearray[vertical - 2][horizontal] != 1) or      # 2 above the entry
                            (gamearray[vertical][horizontal - 1] != 1) or      # left of entry
                            (gamearray[vertical][horizontal - 2] != 1) or      # 2 left of entry
                            (gamearray[vertical - 1][horizontal - 2] != 1) or  # 2 left and above entry
                            (gamearray[vertical - 2][horizontal - 2] != 1) or  # 2 left and 2 above entry
                            (gamearray[vertical - 2][horizontal - 1] != 1)):    # left and 2 above entry

                        # bomb making
                        if gamearray[vertical][horizontal] == 0:    # if the entry is clear (0) random bomb maker starts
                            bomb_yn = random.randint(1, 7)    # random int made using random.randint from 1-7

                            if bomb_yn == 1:    # if random int is 1 bomb is created
                                bomb_count += 1     # bomb_count increases by 1
                                gamearray[vertical][horizontal] = 1     # changes entry value from 0 to 1
    return gamearray    # returns the gamearray with bombs to where this function was called


def adjacent_values():  # counts the number of bombs that are adjacent to each tile in the gamearray
    # assigns a value to the entry corresponding to the number of adjacent bombs (1)
    for vertical in range(rows):    # loop through each column
        for horizontal in range(cols):  # loop through each row
            num_adjacent = 0    # initialize the number of adjacent bombs at 0 and resets for each entry
            if minefield[vertical][horizontal] != 1:    # checks if entry is a bomb (1) if not code runs

                # checks if there is an array value below the given entry
                if 0 <= horizontal <= cols - 1 and 0 <= vertical - 1 <= rows - 1:
                    # then checks if a bomb is there
                    if minefield[vertical - 1][horizontal] == 1:
                        num_adjacent += 1   # if a bomb is there add value to num adjacent

                # checks if there is an array value below and to the left the given entry
                if 0 <= horizontal - 1 <= cols - 1 and 0 <= vertical - 1 <= rows - 1:
                    # then checks if a bomb is there
                    if minefield[vertical - 1][horizontal - 1] == 1:
                        num_adjacent += 1   # if a bomb is there add value to num adjacent

                # checks if there is an array value below and to the right of the given entry
                if 0 <= horizontal + 1 <= cols - 1 and 0 <= vertical - 1 <= rows - 1:
                    # then checks if a bomb is there
                    if minefield[vertical - 1][horizontal + 1] == 1:
                        num_adjacent += 1   # if a bomb is there add value to num adjacent

                # checks if there is an array value to the left of the given entry
                if 0 <= horizontal - 1 <= cols - 1 and 0 <= vertical <= rows - 1:
                    # then checks if a bomb is there
                    if minefield[vertical][horizontal - 1] == 1:
                        num_adjacent += 1   # if a bomb is there add value to num adjacent

                # checks if there is an array value to the right of the given entry
                if 0 <= horizontal + 1 <= cols - 1 and 0 <= vertical <= rows - 1:
                    # then checks if a bomb is there
                    if minefield[vertical][horizontal + 1] == 1:
                        num_adjacent += 1   # if a bomb is there add value to num adjacent

                # checks if there is an array value above the given entry
                if 0 <= horizontal <= cols - 1 and 0 <= vertical + 1 <= rows - 1:
                    # then checks if a bomb is there
                    if minefield[vertical + 1][horizontal] == 1:
                        num_adjacent += 1   # if a bomb is there add value to num adjacent

                # checks if there is an array value above and to the left of the given entry
                if 0 <= horizontal - 1 <= cols - 1 and 0 <= vertical + 1 <= rows - 1:
                    # then checks if a bomb is there
                    if minefield[vertical + 1][horizontal - 1] == 1:
                        num_adjacent += 1   # if a bomb is there add value to num adjacent

                # checks if there is an array value above and to the right of the given entry
                if 0 <= horizontal + 1 <= cols - 1 and 0 <= vertical + 1 <= rows - 1:
                    # then checks if a bomb is there
                    if minefield[vertical + 1][horizontal + 1] == 1:
                        num_adjacent += 1   # if a bomb is there add value to num adjacent

                # if there are no bombs (1) adjacent value in the given entry stays as 0
                # if there are bombs (1) adjacent to the entry assigns a value of the number of adjacent bombs X 10
                # so that the bomb number (1) is not the same as if there is 1 adjacent bomb
                if num_adjacent == 1:
                    minefield[vertical][horizontal] = 10    # 1 bombs adjacent

                if num_adjacent == 2:
                    minefield[vertical][horizontal] = 20    # 2 bombs adjacent

                if num_adjacent == 3:
                    minefield[vertical][horizontal] = 30    # 3 bombs adjacent

                if num_adjacent == 4:
                    minefield[vertical][horizontal] = 40    # 4 bombs adjacent

                if num_adjacent == 5:
                    minefield[vertical][horizontal] = 50    # 5 bombs adjacent

                if num_adjacent == 6:
                    minefield[vertical][horizontal] = 60    # 6 bombs adjacent

                if num_adjacent == 7:
                    minefield[vertical][horizontal] = 70    # 7 bombs adjacent

                if num_adjacent == 8:
                    minefield[vertical][horizontal] = 80    # 8 bombs adjacent
    return minefield    # returns the minefield including the adjacent bomb values to where the function was called


def flag(x, y):     # if player right-clicks place a flag at entry point (x,y)
    foreground[y][x] = 2    # value of 2 in the foreground means flag
    return foreground   # returns the foreground array with a flag at the point the player right-clicked


def rflag(x, y):    # if player right-clicks on a tile already with a flag remove flag at entry point (x,y)
    foreground[y][x] = 0    # makes the foreground tile a 0 again
    return foreground   # returns the foreground array without a flag at the point the player right-clicked


def digging(x, y):  # if player left-clicks on a tile make the foreground clear at entry point (x,y)
    foreground[y][x] = 1    # # makes the foreground tile a 1 and therefore clear
    no_ajacent(x, y)    # calls function no adjacent to see if there are adjacent bombs
    return foreground


def no_ajacent(x, y):   # checks if there are any adjacent bombs at entry point (x,y)
    if complete_minefield[y][x] == 0:   # if that tile has no adjacent bombs call mass dig
        mass_dig(x, y)


def mass_dig(x, y):     # clears all tiles adjacent tiles without bombs at entry point (x,y)
    # checks if there is an array value above the given entry
    if 0 <= x <= cols - 1 and 0 <= y - 1 <= rows - 1:
        # then checks if it is already clear
        if foreground[y - 1][x] != 1:
            # if it is not already clear then it clears it
            foreground[y - 1][x] = 1
            # then it calls no_adjacent to see if this new value has no adjacent bombs resulting in a loop if it does
            no_ajacent(x, y - 1)

    # checks if there is an array value above and to the left of the given entry
    if 0 <= x - 1 <= cols - 1 and 0 <= y - 1 <= rows - 1:
        # then checks if it is already clear
        if foreground[y - 1][x - 1] != 1:
            # if it is not already clear then it clears it
            foreground[y - 1][x - 1] = 1
            # then it calls no_adjacent to see if this new value has no adjacent bombs resulting in a loop if it does
            no_ajacent(x - 1, y - 1)

    # checks if there is an array value above and to the right of the given entry
    if 0 <= x + 1 <= cols - 1 and 0 <= y - 1 <= rows - 1:
        # then checks if it is already clear
        if foreground[y - 1][x + 1] != 1:
            # if it is not already clear then it clears it
            foreground[y - 1][x + 1] = 1
            # then it calls no_adjacent to see if this new value has no adjacent bombs resulting in a loop if it does
            no_ajacent(x + 1, y - 1)

    # checks if there is an array value to the left of the given entry
    if 0 <= x - 1 <= cols - 1 and 0 <= y <= rows - 1:
        # then checks if it is already clear
        if foreground[y][x - 1] != 1:
            # if it is not already clear then it clears it
            foreground[y][x - 1] = 1
            # then it calls no_adjacent to see if this new value has no adjacent bombs resulting in a loop if it does
            no_ajacent(x - 1, y)

    # checks if there is an array value to the right of the given entry
    if 0 <= x + 1 <= cols - 1 and 0 <= y <= rows - 1:
        # then checks if it is already clear
        if foreground[y][x + 1] != 1:
            # if it is not already clear then it clears it
            foreground[y][x + 1] = 1
            # then it calls no_adjacent to see if this new value has no adjacent bombs resulting in a loop if it does
            no_ajacent(x + 1, y)

    # checks if there is an array value below the given entry
    if 0 <= x <= cols - 1 and 0 <= y + 1 <= rows - 1:
        # then checks if it is already clear
        if foreground[y + 1][x] != 1:
            # if it is not already clear then it clears it
            foreground[y + 1][x] = 1
            # then it calls no_adjacent to see if this new value has no adjacent bombs resulting in a loop if it does
            no_ajacent(x, y + 1)

    # checks if there is an array value below and to the left of the given entry
    if 0 <= x - 1 <= cols - 1 and 0 <= y + 1 <= rows - 1:
        # then checks if it is already clear
        if foreground[y + 1][x - 1] != 1:
            # if it is not already clear then it clears it
            foreground[y + 1][x - 1] = 1
            # then it calls no_adjacent to see if this new value has no adjacent bombs resulting in a loop if it does
            no_ajacent(x - 1, y + 1)

    # checks if there is an array value above and to the right of the given entry
    if 0 <= x + 1 <= cols - 1 and 0 <= y + 1 <= rows - 1:
        # then checks if it is already clear
        if foreground[y + 1][x + 1] != 1:
            # if it is not already clear then it clears it
            foreground[y + 1][x + 1] = 1
            # then it calls no_adjacent to see if this new value has no adjacent bombs resulting in a loop if it does
            no_ajacent(x + 1, y + 1)


def win_lose(x, y):     # function that checks if the player wins or loses based on the most recent entry at point (x,y)
    global generatemap, win, tiles_dug  # makes these variables usable throughout the code

    if 1 == complete_minefield[y][x]:   # if the player opens up a bomb
        win = 2     # then the win variable is set to 2 meaning the player loses
        generatemap = None  # generate map is now set to None and win = 2 meaning that the loser screen prints

    if 1 != complete_minefield[y][x]:   # if the open tile is not a bomb then see if the win conditions are met
        # vert is the index of the current row in foreground
        # row is the content of the current row in foreground
        for vert, row in enumerate(foreground):
            # hori is the index of the current element in the current row
            # value is the content of the current element in the current row
            for hori, value in enumerate(row):
                if value == 1:
                    # if the foreground tile is clear (1) add 1 to the amount of tiles dug
                    tiles_dug += 1

        # if the tiles dug is greater than or equal to the max_clear_count then the player wins
        if tiles_dug >= max_clear_count:
            win = 1     # then the win variable is set to 1 meaning the player wins
            generatemap = None  # generate map is now set to None and win = 1 meaning that the winner screen prints

        # if the player does not win reset the tiles_dug variable
        else:
            tiles_dug = 0


# Initialize Pygame
pygame.init()

# Set up fonts for text rendering
font = pygame.font.Font(None, 24)
title_font = pygame.font.Font(None, 70)

# Set the dimensions of the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mine Sweeper")

# Main loop
running = True
left_on = False
right_on = False
while running:
    # fill the screen with black to reset and allow for changes to the screen
    screen.fill("black")

    # event handling checks if an event has occurred such as a mouse or key press
    for event in pygame.event.get():

        # checks if the window is closed
        if event.type == pygame.QUIT:
            # if window is closed then the while loop ends
            running = False

        # check if the game is won or lost and enter key is pressed for a reset
        elif win == 1 or win == 2:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # all initial variables are reset as they were at the beginning of the code
                generatemap = False
                win = 0
                tiles_dug = 0
                start = 0

        # check if the game is not started, and keys 1, 2, or 3 are pressed for difficulty selection
        elif start == 0:
            # detects is a key is pressed and sees if it was 1, 2, or 3
            if event.type == pygame.KEYDOWN:
                # easy mode
                if event.key == pygame.K_1:
                    # set parameters for easy mode
                    max_clear_count = easy_max_clear_count
                    bomb_max = easy_bomb_max
                    flagcount = easy_flagcount
                    rows = easy_rows
                    cols = easy_cols
                    # initialize the array size for the gamearray and foreground based on the dimensions of easy mode
                    gamearray = [[0 for _ in range(cols)] for _ in range(rows)]
                    foreground = [[0 for _ in range(cols)] for _ in range(rows)]
                    start = 1   # starts game

                # medium mode
                elif event.key == pygame.K_2:
                    # set parameters for medium mode
                    rows = med_rows
                    cols = med_cols
                    max_clear_count = med_max_clear_count
                    bomb_max = med_bomb_max
                    flagcount = med_flagcount
                    # initialize the array size for the gamearray and foreground based on the dimensions of medium mode
                    gamearray = [[0 for _ in range(cols)] for _ in range(rows)]
                    foreground = [[0 for _ in range(cols)] for _ in range(rows)]
                    start = 1   # starts game

                # hard mode
                elif event.key == pygame.K_3:
                    # set parameters for hard mode
                    rows = hard_rows
                    cols = hard_cols
                    max_clear_count = hard_max_clear_count
                    bomb_max = hard_bomb_max
                    flagcount = hard_flagcount
                    # initialize the array size for the gamearray and foreground based on the dimensions of hard mode
                    gamearray = [[0 for _ in range(cols)] for _ in range(rows)]
                    foreground = [[0 for _ in range(cols)] for _ in range(rows)]
                    start = 1   # starts game

    # sees if game has started and a win or loss has not happened
    if win != 1 and win != 2 and start == 1:
        left_click = pygame.mouse.get_pressed()[0]      # left-click
        right_click = pygame.mouse.get_pressed()[2]     # right-click

        # if the map is not generated, left-click initializes the minefield and foreground
        if not generatemap:
            if left_click and not left_on:
                # mouse position in the x and y direction
                mousey = pygame.mouse.get_pos()[1]
                mousex = pygame.mouse.get_pos()[0]
                # arrays on screen are shifted 100 pixels horizontally and 130 pixels vertically
                # size of each tile is 20 X 20
                y = (mousey - 130) / 20
                x = (mousex - 100) / 20
                # round down for both x and y as they are floats
                y = math.floor(y)
                x = math.floor(x)

                # check if the coordinates are within the valid grid bounds
                if (cols - 1 >= x >= 0) and (rows - 1 >= y >= 0):
                    # calls the randomize_map function and assigns the new array to minefield
                    minefield = randomize_map(x, y)
                    # calls the adjacent_values function and assigns the new array to complete
                    complete_minefield = adjacent_values()
                    digging(x, y)   # calls digging function do clear the tile that is clicked
                    generatemap = True  # map is now generated

        # if the map is generated, handle left and right clicks
        if generatemap:
            # left-click
            if left_click and not left_on:
                # mouse position in the x and y direction
                mousey = pygame.mouse.get_pos()[1]
                mousex = pygame.mouse.get_pos()[0]
                # arrays on screen are shifted 100 pixels horizontally and 130 pixels vertically
                # size of each tile is 20 X 20
                y = (mousey - 130) / 20
                x = (mousex - 100) / 20
                # round down for both x and y as they are floats
                y = math.floor(y)
                x = math.floor(x)

                # check if the coordinates are within the valid grid bounds
                if (cols - 1 >= x >= 0) and (rows - 1 >= y >= 0):
                    # if a flag has been placed on the tile that is clicked then the dig function will not be called
                    if foreground[y][x] != 2:
                        digging(x, y)   # calls digging function do clear the tile that is clicked
                        win_lose(x, y)  # calls the win_lose function to see if the player wins after each move

            # Right-click flags or removes flags from tiles
            elif right_click and not right_on:
                # mouse position in the x and y direction
                mousey = pygame.mouse.get_pos()[1]
                mousex = pygame.mouse.get_pos()[0]
                # arrays on screen are shifted 100 pixels horizontally and 130 pixels vertically
                # size of each tile is 20 X 20
                y = (mousey - 130) / 20
                x = (mousex - 100) / 20
                # round down for both x and y as they are floats
                y = math.floor(y)
                x = math.floor(x)

                # check if the coordinates are within the valid grid bounds
                if (cols - 1 >= x >= 0) and (rows - 1 >= y >= 0):
                    # check if the tile that is right-clicked is clear (1) already
                    if foreground[y][x] != 1:
                        # check if tile that is right-clicked is normal (0) and that there are still flags left to use
                        if foreground[y][x] == 0 and flagcount > 0:
                            # calls flag function to add a flag on that tile and remove 1 flag from the flag count
                            flag(x, y)
                            flagcount -= 1

                        # check if tile that is right-clicked is already flagged (2)
                        elif foreground[y][x] == 2:
                            # calls rflag function to remove a flag on that tile and add 1 flag to the flag count
                            rflag(x, y)
                            flagcount += 1
        # Update the status of left and right mouse clicks
        left_on = left_click
        right_on = right_click

    # Printing the start screen
    if start == 0:
        # title text using title font
        text_surface = title_font.render("Welcome to Minesweeper", True, "White")
        # center text near top of screen
        text_rect = text_surface.get_rect(center=(600 / 2 + 100, 100 / 2 + 15))
        # displays text to screen
        screen.blit(text_surface, text_rect)

        # print easy mode option in green
        text_surface = font.render("Press 1 to start Easy Mode", True, "Green")
        # center text just below title
        text_rect = text_surface.get_rect(center=(600 / 2 + 100, 100 / 2 + 55))
        # displays text to screen
        screen.blit(text_surface, text_rect)

        # print medium mode option
        text_surface = font.render("Press 2 to start Medium Mode", True, "Yellow")
        # center text just below easy mode option
        text_rect = text_surface.get_rect(center=(600 / 2 + 100, 100 / 2 + 85))
        # displays text to screen
        screen.blit(text_surface, text_rect)

        # print hard mode option
        text_surface = font.render("Press 3 to start Hard Mode", True, "Red")
        # center text just below medium mode option
        text_rect = text_surface.get_rect(center=(600 / 2 + 100, 100 / 2 + 115))
        # displays text to screen
        screen.blit(text_surface, text_rect)

        # making instructions an array
        instructions = [
            "Instructions:",
            "Left click to clear tiles",
            "Right click to place flags on suspected bomb tiles",
            "You cannot left click on flagged tiles",
            "White tile represents no adjacent bombs",
            "Numbers represent # of adjacent bombs",
            "Clear all non-bomb tiles to win",
            "Clear a bomb tile and lose",
            "Press X close to return to maze at any time"
        ]
        y_offset = 0    # distance from top
        for line in instructions:  # printing the instructions array as a for loop
            # print the text from the corresponding line
            text_surface = font.render(line, True, "White")
            # displays text to screen 50 pixels from the left and 150 pixels down + 30 more depending on what line it is
            screen.blit(text_surface, (50, 150 + y_offset))
            # move line down 30 pixels
            y_offset += 30

    # Draw the bomb background on the screen behind foreground
    if start == 1:
        if generatemap or generatemap is None:
            # vert is the index of the current row in complete_minefield
            # row is the content of the current row in complete_minefield
            for vert, row in enumerate(complete_minefield):
                # hori is the index of the current element in the current row
                # value is the content of the current element in the current row
                for hori, value in enumerate(row):

                    if value == 0:
                        # print white background tile representing no adjacent bombs
                        pygame.draw.rect(screen, "white", (100 + hori * (600 / 30), 130 + vert * (320 / 16), 15, 15))

                    if value == 1:
                        # print red background tile representing bomb
                        pygame.draw.rect(screen, "Red", (100 + hori * (600 / 30), 130 + vert * (320 / 16), 15, 15))

                    # value of 10 means 1 adjacent bomb
                    if value == 10:
                        # blue rectangle background behind #1
                        pygame.draw.rect(screen, "Blue", (100 + hori * (600 / 30), 130 + vert * (320 / 16), 15, 15))
                        # print white #1 on top of the blue square
                        text_surface = font.render("1", True, "white")
                        # center text in square
                        text_rect = text_surface.get_rect(
                            center=(100 + hori * (600 / 30) + 15 / 2, 130 + vert * (320 / 16) + 15 / 2))
                        # displays text to screen
                        screen.blit(text_surface, text_rect)

                    # value of 20 means 2 adjacent bomb
                    if value == 20:
                        # dark green rectangle background behind #2
                        pygame.draw.rect(screen, "Dark Green", (100 + hori * (600 / 30), 130 + vert * (320 / 16), 15, 15))
                        # print white #2 on top of the dark green square
                        text_surface = font.render("2", True, "white")
                        # center text in square
                        text_rect = text_surface.get_rect(
                            center=(100 + hori * (600 / 30) + 15 / 2, 130 + vert * (320 / 16) + 15 / 2))
                        # displays text to screen
                        screen.blit(text_surface, text_rect)

                    # value of 30 means 3 adjacent bomb
                    if value == 30:
                        # teal rectangle background behind #3
                        pygame.draw.rect(screen, "Teal", (100 + hori * (600 / 30), 130 + vert * (320 / 16), 15, 15))
                        # print white #3 on top of the teal square
                        text_surface = font.render("3", True, "White")
                        # center text in square
                        text_rect = text_surface.get_rect(
                            center=(100 + hori * (600 / 30) + 15 / 2, 130 + vert * (320 / 16) + 15 / 2))
                        # displays text to screen
                        screen.blit(text_surface, text_rect)

                    # value of 40 means 4 adjacent bomb
                    if value == 40:
                        # magenta rectangle background behind #4
                        pygame.draw.rect(screen, "Magenta", (100 + hori * (600 / 30), 130 + vert * (320 / 16), 15, 15))
                        # print white #4 on top of the magenta square
                        text_surface = font.render("4", True, "white")
                        # center text in square
                        text_rect = text_surface.get_rect(
                            center=(100 + hori * (600 / 30) + 15 / 2, 130 + vert * (320 / 16) + 15 / 2))
                        # displays text to screen
                        screen.blit(text_surface, text_rect)

                    # value of 50 means 5 adjacent bomb
                    if value == 50:
                        # orange rectangle background behind #5
                        pygame.draw.rect(screen, "Orange", (100 + hori * (600 / 30), 130 + vert * (320 / 16), 15, 15))
                        # print white #5 on top of the orange square
                        text_surface = font.render("5", True, "white")
                        # center text in square
                        text_rect = text_surface.get_rect(
                            center=(100 + hori * (600 / 30) + 15 / 2, 130 + vert * (320 / 16) + 15 / 2))
                        # displays text to screen
                        screen.blit(text_surface, text_rect)

                    # value of 60 means 6 adjacent bomb
                    if value == 60:
                        # purple rectangle background behind #6
                        pygame.draw.rect(screen, "Purple", (100 + hori * (600 / 30), 130 + vert * (320 / 16), 15, 15))
                        # print white #6 on top of the purple square
                        text_surface = font.render("6", True, "white")
                        # center text in square
                        text_rect = text_surface.get_rect(
                            center=(100 + hori * (600 / 30) + 15 / 2, 130 + vert * (320 / 16) + 15 / 2))
                        # displays text to screen
                        screen.blit(text_surface, text_rect)

                    # value of 70 means 7 adjacent bomb
                    if value == 70:
                        # brown rectangle background behind #7
                        pygame.draw.rect(screen, "Brown", (100 + hori * (600 / 30), 130 + vert * (320 / 16), 15, 15))
                        # print white #7 on top of the brown square
                        text_surface = font.render("7", True, "white")
                        # center text in square
                        text_rect = text_surface.get_rect(
                            center=(100 + hori * (600 / 30) + 15 / 2, 130 + vert * (320 / 16) + 15 / 2))
                        # displays text to screen
                        screen.blit(text_surface, text_rect)

                    # value of 80 means 8 adjacent bomb
                    if value == 80:
                        # black rectangle background behind #8
                        pygame.draw.rect(screen, "Black", (100 + hori * (600 / 30), 130 + vert * (320 / 16), 15, 15))
                        # print white #8 on top of the black square
                        text_surface = font.render("8", True, "white")
                        # center text in square
                        text_rect = text_surface.get_rect(
                            center=(100 + hori * (600 / 30) + 15 / 2, 130 + vert * (320 / 16) + 15 / 2))
                        # displays text to screen
                        screen.blit(text_surface, text_rect)

        # print the foreground to the screen
        # same for loop as used in lines 261-266
        for vert, row in enumerate(foreground):
            for hori, value in enumerate(row):
                if value == 0:  # print gray tiles to the foreground
                    pygame.draw.rect(screen, Gray, (100 + hori * (600 / 30), 130 + vert * (320 / 16), 15, 15))

                # notice no statement for condition 1. if value is 1 the tile should be clear and show
                # corresponding background

                if value == 2:  # print flag tiles to the foreground
                    # gray rectangle background behind flag
                    pygame.draw.rect(screen, Gray, (100 + hori * (600 / 30), 130 + vert * (320 / 16), 15, 15))
                    # print red flag on top of the gray rectangle
                    text_surface = font.render("P", True, "Red")
                    text_rect = text_surface.get_rect(center=(100 + hori * (600 / 30) + 15 / 2, 130 + vert * (320 / 16) + 15 / 2))
                    screen.blit(text_surface, text_rect)

        # printing the flag count to screen in red font
        # str(flagcount) makes the amount of flags a string, so it can be printed
        text_surface = font.render("Flags = " + str(flagcount), True, "Red")
        text_rect = text_surface.get_rect(center=(50, 15))
        screen.blit(text_surface, text_rect)

        if generatemap is None:     # generate map returns none when the player wins or loses
            if win == 2:    # if player clears a bomb tile meaning player loses
                # prints the background for the loser screen
                pygame.draw.rect(screen, "Red", (100, 15, 600, 100))
                # text for the loser screen printed in black on a red background
                text_surface = font.render("Boom!!! You lose click enter to return to start", True, "Black")
                # centers the text
                text_rect = text_surface.get_rect(center=(600 / 2 + 100, 100 / 2 + 15))
                # displays text to screen
                screen.blit(text_surface, text_rect)

            if win == 1:    # if player clears all non-bomb tiles meaning player wins
                # prints the background for the win screen
                pygame.draw.rect(screen, "Green", (100, 15, 600, 100))
                # text for the win screen printed in black on a green background
                text_surface = font.render("Congratulations, you win, click enter to return to start", True, "Black")
                # centers the text
                text_rect = text_surface.get_rect(center=(600 / 2 + 100, 100 / 2 + 15))
                # displays text to screen
                screen.blit(text_surface, text_rect)

    pygame.display.update()   # refreshes screen
# Quit Pygame
pygame.quit()
sys.exit()
