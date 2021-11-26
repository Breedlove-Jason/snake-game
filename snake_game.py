# reference: https://www.edureka.co/blog/snake-game-with-pygame/

import random
import pygame

# initialize pygame
pygame.init()

# color values
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# set display dimensions
dis_width = 600
dis_height = 400

# create title bar caption
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Jason Breedlove')

# start the clock timer from time module import
clock = pygame.time.Clock()

# create the size of our snake
snake_block = 10
# set the speed of the snake element
snake_speed = 15

# set the game fonts for caption and scoreboard
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


# create our snake
def our_snake(snake_block, snake_list):
    # loop through the variable snake_list to increase the size of the tail after snake eats food
    for x in snake_list:
        # draw the snake on the display with an increase of 10 as defined in the snake variable
        # rectangle = pygame.Rect(display, color, x_pos, y_pos, width, height)
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


# create the message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    # center the message on the screen by dividing the width and the height
    # the .blit method is how you copy contents between surfaces, one to another
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # random(start, stop, step)
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # loop to test for game over
    while not game_over:

        while game_close == True:
            # fill the game over screen with blue
            dis.fill(blue)
            # send the user a message
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            # check for user key input after each pygame event and
            for event in pygame.event.get():
                # scan for keyboard input
                if event.type == pygame.KEYDOWN:
                    # if user presses q then the game is over
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    # if user presses see then run gameLoop
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            # if user clicks the close button then quit
            if event.type == pygame.QUIT:
                game_over = True
            # if user presses up, down, left, right then move the snake along each x, y, axis
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
