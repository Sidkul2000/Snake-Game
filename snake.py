import pygame
import random
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)
yellow = (255,255,102)
red = (213,50,80)
green = (0,255,0)
blue = (50,153,213)

block = 10
w = 800
h = 600

dis = pygame.display.set_mode((w,h))
pygame.display.set_caption('Snake Game by Siddhant')

clock = pygame.time.Clock()
bg_img = pygame.image.load("snake_bg.jpg").convert()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render('YOUR SCORE: ' + str(score), True, blue)
    dis.blit(value, [0,0])

def our_snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], 10, 10])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [150, 200])

def gameloop():
    game_over = False
    game_close = False
    x1 = 400
    y1 = 300
    x1_c = 0
    y1_c = 0
    snake_List = []
    len_snake = 1

    x_food = round(random.randrange(0, 790)/10.0) * 10.0
    y_food = round(random.randrange(0, 590)/10.0) * 10.0

    while not game_over:
        while game_close == True:
            dis.blit(bg_img, [0,0])
            message("You Lost! Press c - Play Again, q - Quit", red)
            Your_score(len_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameloop()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_c = -10
                    y1_c = 0
                elif event.key == pygame.K_RIGHT:
                    x1_c = 10
                    y1_c = 0
                elif event.key == pygame.K_UP:
                    x1_c = 0
                    y1_c = -10
                elif event.key == pygame.K_DOWN:
                    x1_c = 0
                    y1_c = 10

        if x1 >= 800 or y1 >= 600 or x1 < 0 or y1 < 0:
            game_close = True
        x1 += x1_c
        y1 += y1_c
        dis.blit(bg_img, [0,0])
        pygame.draw.rect(dis, red, [x_food, y_food, 8, 8])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > len_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_head:
                game_close == True

        our_snake(10, snake_List)
        Your_score(len_snake - 1)

        pygame.display.update()

        if x1 == x_food and y1 == y_food:
            x_food = round(random.randrange(0, 790)/10.0) * 10.0
            y_food = round(random.randrange(0, 590)/10.0) * 10.0
            len_snake += 1

        clock.tick(15)

    pygame.quit()
    quit()

gameloop()
