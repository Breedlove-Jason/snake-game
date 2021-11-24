import time

import pygame

# initializes all of the imported pygame modules and returns a tuple with success or failure
pygame.init()

# create screen/display
disp_width = 600
disp_height = 600
disp = pygame.display.set_mode((disp_width, disp_height))

pygame.display.update()
pygame.display.set_caption("Snake Game By Jason Breedlove")

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
game_over = False

x1 = disp_width / 2
y1 = disp_height / 2
snake_block = 10
x1_change = 0
y1_change = 0
clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    disp.blit(mesg, [disp_width / 2, disp_height / 2])


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
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

    if x1 >= disp_width or x1 < 0 or y1 >= disp_height or y1 < 0:
        game_over = True
    x1 += x1_change
    y1 += y1_change

    disp.fill(black)
    pygame.draw.rect(disp, white, [x1, y1, 15, 15])

    pygame.display.update()

    clock.tick(snake_speed)
message("You Lost", red)
pygame.display.update()
time.sleep(2)

# quit
pygame.quit()
quit()
