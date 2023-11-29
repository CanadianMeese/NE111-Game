# import all modules neccesary
# pygame for the basic display funtions,
import pygame
# import pygame.locals for key controls
from pygame.locals import *
# time for the game clock (frame rate and refresh speed)
import time
# import random used for random placement of apple after each time snake eats one
import random

# size used for game grid cells
size = 40
# variable for the starting length of the snake
length = 1
# set colours used in game
background_colour = (100, 120, 15)
black = (0, 0, 0)
white_text = (255, 255, 255)
# screen dimension variables
width = 800
height = 600

# Apple class manages the apple within the game
class Apple:
    # initilize the apple with a screen to draw on and sets its initial position
    def __init__(self, parent_screen):
        # uploaded image for the apple already scaled to size
        self.image = pygame.image.load("apple_with_new_background.png").convert()
       # the sceen where the apple will be drawn
        self.parent_screen = parent_screen
        # coordinates are multiples of 'size' in order to make sure the apples always line up with the snake
        # it is the placement of the first apple
        self.x = size * 3
        self.y = size * 3

    # updates the screen whenever it is called in class Apple, updates position of apple with new x and y coordinates
    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        # updates the screen display
        pygame.display.flip()

    # randomizes the placement of the apple within the screen grid each time one is eaten by the snake
    def move(self):
        # random x coordinate
        self.x = random.randint(0, 19) * size
        # random y coordinate
        self.y = random.randint(0, 14) * size

# parameters of the snake
class Snake:
    # initilize the snake with a screen, sets its initial length
    def __init__(self, parent_screen, length):
        # setting variables to represent the instances of the Snake class
        self.length = length # the initial length
        self.parent_screen = parent_screen # the screen where the snake will be drawn
        # list of x and y coordinates for theposition of the snake
        self.x = [size] * length
        self.y = [size] * length
        # uses image for snake segmants
        # body image and all the different possible head images
        # all have been sized at 40x40 pixels to fit within the game grid properly so it looks better
        self.block = pygame.image.load("yellow_circle_new.png").convert()
        self.head = pygame.image.load("sad_face.png").convert()
        self.second_head = pygame.image.load("happy_face.png").convert()
        self.third_head = pygame.image.load("heart_face.png").convert()
        self.fourth_head = pygame.image.load("winner.png").convert()

        # starting direction is right
        self.direction = 'right'

    # funtion for the snake to increase length
    def increase_length(self):
        # snake length increases in increments of 1
        self.length += 1
        # adds the new x and y coodinates to the list for the snake
        self.x.append(-1)
        self.y.append(-1)

    # setting methods for the 4 possible directions (up, down, left, right)
    def move_up(self):
        self.direction = 'up'
    def move_down(self):
        self.direction = 'down'
    def move_left(self):
        self.direction = 'left'
    def move_right(self):
        self.direction = 'right'

    # move the snake by updating the position of its head and  body
    def walk(self):
        for i in range(self.length-1, 0 , -1):
            # shift the position of each segment to the last position of the segmant infront of it
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # update the head position based on the imput direction
        # an increase in x menans movement to the right and vice versa
        # and increase in y means movement in the down direction and vice versa
        if self.direction == 'up':
            self.y[0] -= size
        if self.direction == 'down':
            self.y[0] += size
        if self.direction == 'left':
            self.x[0] -= size
        if self.direction == 'right':
            self.x[0] += size
        # calls on the function defined below to draw the updated snake
        self.draw()

    # draw the snake on the screen
    def draw(self):
        self.parent_screen.fill((background_colour))
        for i in range(self.length):
            if i == 0:
                # use the head images for the first segmant and the  body segmant for the rest
                # Check if length is greater than or equal to the threshold
                # Change head photo if length is over specified threshold
                # food makes snake happy
                if self.length >= 20:
                    self.parent_screen.blit(self.fourth_head, (self.x[i], self.y[i]))
                elif self.length >= 10:
                    self.parent_screen.blit(self.third_head, (self.x[i], self.y[i]))
                elif self.length >= 5:
                    self.parent_screen.blit(self.second_head, (self.x[i], self.y[i]))
                else:
                    self.parent_screen.blit(self.head, (self.x[i], self.y[i]))
            else:
                self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

# manages the game environment
class Game:
    # display start screen
    def start_screen(self):
        # set background colour
        self.surface.fill(black)
        # fonts for the start screen
        font1 = pygame.font.SysFont('arial', 55)
        font2 = pygame.font.SysFont('arial', 43)
        # text displayed and position of text
        line1 = font1.render("WELCOME TO SNAKE GAME!", True, (white_text))
        self.surface.blit(line1, (100, 250))
        line2 = font2.render("To play press ENTER. To exit press X.", True, (white_text))
        self.surface.blit(line2, (90, 340))
        pygame.display.flip()

        # wait for user imput when game screen is displayed
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # exit the game if x key is pressed
                    if event.key == K_x:
                        waiting = False
                        pygame.quit() # stop all pygame modules
                        exit()
                    # start the game loop is ENTER is pressed
                    if event.key == K_RETURN:
                        waiting = False


    # sets up the game environment
    def __init__(self):
        pygame.init()
        # window caption
        pygame.display.set_caption("Snake Eater")
        # window size using variables
        self.surface = pygame.display.set_mode((width, height))
        self.surface.fill((background_colour))
        # starting length of snake and drawing it on the screen surface
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        # drawing the apple on the screen surface
        self.apple = Apple(self.surface)
        self.apple.draw()

    # detects when collisions occur, i.e when snake position equals position of the givin object
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True

        return False

    def display_score(self):
        # font and size parameters of the score board
        font = pygame.font.SysFont('arial', 30)
        # writting for the score board which is just the length of the snake
        score = font.render(f"Score: {self.snake.length}", True, (white_text))
        # position of the score board
        self.surface.blit(score, (680, 10))

    def play(self):
        # update snake, apple, and score with pygame.flip
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # snake collididing with apples
        # snake length increases by 1 for every apple collided
        for i in range(self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
                self.snake.increase_length()
                self.apple.move()

        # snake colliding with its tail
        # snake hits its tail start the "game over" sequence
        for i in range(1, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Game Over"

        # snake collides with borders
        # if the snake leaves the given borders of the window start the "game over" sequence
        if not (0 <= self.snake.x[0] <= width and 0 <= self.snake.y[0] <= height):
            raise "Game Over"

    # game over sequence
    def show_game_over(self):
        self.surface.fill(black)
        # fonts used for the text
        font1 = pygame.font.SysFont('arial', 45)
        font2 = pygame.font.SysFont('arial', 40)
        # line1 shows final score before game over
        line1 = font1.render(f"Game Over! Your Score is {self.snake.length}", True, (white_text))
        # draw line1 at position
        self.surface.blit(line1, (170, 180))
        # line2 propts user with options to quit or continue
        line2 = font2.render("To play again press Enter. To exit press X.", True, (white_text))
        # draw line2 at position
        self.surface.blit(line2, (50, 240))
        pygame.display.flip()

    # reset sequence, just reuses the same initial code to overwrite the snake and the apple
    # snake resets to length 1 and apple returns to the original start position
    def reset(self):
        self.snake = Snake(self.surface, length)
        self.apple = Apple(self.surface)

    # main loop for handling direction changes according the keys pressed
    def run(self):
        # display the start screen before anything else
        self.start_screen()
        running = True
        pause = False
        while running:
            # key controls
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_x: # ESCAPE sets running to False, exits game
                        running = False

                    if event.key == K_RETURN: # ENTER sets pause to False, starts game
                        pause = False

                    if not pause:
                        # w key is set to change the direction to up
                        if event.key == K_w:
                            self.snake.move_up()
                        # s key is set to change the direction to down
                        if event.key == K_s:
                            self.snake.move_down()
                        # a key is set to change the direction to left
                        if event.key == K_a:
                            self.snake.move_left()
                        # d key is set to change the direction to right
                        if event.key == K_d:
                            self.snake.move_right()
                elif event.type == QUIT: # if QUIT occured, change running to False
                    running = False
            try:
                # if the game is not paused then start play method
                if not pause:
                    self.play()
            # call on reset function after return button is pressed
            except Exception as e: # catches all potential exceptions
                self.show_game_over() # displays game over screen by calling show_game_over method
                pause = True # puases game
                self.reset() # calls reset method

            # game speed
            # controls update rate and snake speed
            time.sleep(0.2)


# checks is the script is the main module being  run
if __name__ == "__main__":
    game = Game()
    # creates instance of the Game class and initiates the game loop
    game.run()
    # sets running equal to true until game end function is called to change it to false
    running = True
