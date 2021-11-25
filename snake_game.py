# reference: https://www.edureka.co/blog/snake-game-with-pygame/

import pygame
import time
import random

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


# create function to track score
def your_score(score):
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
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
