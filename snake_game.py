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
