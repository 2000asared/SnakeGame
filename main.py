#import the pygame library
import pygame
import time
import random

from snake import Snake
pygame.init()
#define the colours
black = (0,0,0)
white = (255,255,255)
brown = (134,72,22)
green = (0,255,0)
red = (255,0,0)

#open a window
size = (700,500)
d_width = 800
d_height = 600
screen = pygame.display.set_mode((d_width, d_height))
pygame.display.set_caption("Snake Game")

font_style = pygame.font.SysFont("verdana", 50)
score_font = pygame.font.SysFont("gadugi", 45)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    screen.blit(value, [0,0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])


def message(msg, colour, a, b):
    mesg = font_style.render(msg, True, colour)
    screen.blit(mesg, [a, b])

def game_Loop():
    game_over = False
    game_close = False
    clock = pygame.time.Clock()
    snake_List = []
    snake_length = 1
    x1_change = 0
    y1_change = 0
    x1 = d_width / 2
    y1 = d_height / 2
    snake_block = 10
    snake_speed = 20

    foodx = round(random.randrange(0, d_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, d_height - snake_block) / 10.0) * 10.0
    while not game_over:
        while game_close == True:
            screen.fill(white)
            message('GAME OVER! :(', red, 220, 100)
            message('You scored: ' + str(snake_length -1), red, 220, 170)
            message('Press P to play again', red, 160, 270)
            message('Press Q to quit', red, 160, 340)
            pygame.display.update()

        #Main event loop
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game_Loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False
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

        if x1 >= 800 or x1 < 0 or y1 >= 600 or y1 < 0:
            game_close = True

        screen.fill(white)
        x1 += x1_change
        y1 += y1_change

        pygame.draw.rect(screen, brown, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > snake_length:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(snake_length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, d_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, d_height - snake_block) / 10.0) * 10.0
            snake_length += 1
            snake_speed += 3

        clock.tick(snake_speed)
    pygame.quit()
    quit()

game_Loop()