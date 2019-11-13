# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:34:28 2019

@author: a9302
"""

import pygame
import random

BLACK = (0, 0, 0)
RED = (255, 0, 0)

# set clock of the game(數字越大越快)
Gb_game_clock = 120

# set the width and height of base surf
Gb_base_surf_width = 640
Gb_base_surf_height = 480

# set the width and height of snake and point
Gb_snake_width = 22
Gb_snake_height = 22

Gb_point_width = 22
Gb_point_height = 22

# direction of snake
HeadRight = 0
HeadLeft = 1
HeadUp = 2
HeadDown = 3

def goNextPosition( headDirection, snake_position, point_px, point_py, eatPoint ):
    # get the head position
    px = snake_position[0][0]
    py = snake_position[0][1]
    
    if headDirection == HeadRight:
        px += 1
    elif headDirection == HeadLeft:
        px -= 1
    elif headDirection == HeadUp:
        py -= 1
    elif headDirection == HeadDown:
        py += 1
        
    if eatPoint:
        snake_position.insert(0, [point_px, point_py])
        
    if len(snake_position) > 1 :    # 如果有body
        # 刪除最後一個 body position
        snake_position.pop()
        # 將頭的位置新增在最前面
        snake_position.insert(0, [px, py])
    else:
        snake_position[0][0] = px
        snake_position[0][1] = py
        
    return snake_position      

def showSnake(base_surf, snake_obj, snakeBody_obj, snake_position):
    base_surf.blit(snake_obj, (snake_position[0][0], snake_position[0][1]))    # 貼 snake head 在base_surf 的 snake_px, snake_py
    for i in range ( len(snake_position) ):
        px = snake_position[i][0]
        py = snake_position[i][1]
        base_surf.blit(snake_obj, (px, py))    # 貼 snake head 在base_surf 的 snake_px, snake_py
    
def eatFood(snake_obj, point_obj, snake_position, point_px, point_py):
    # get the position of snake head
    snake_px = snake_position[0][0]
    snake_py = snake_position[0][1]
    
    # get the attribute of snake and point
    snake_rect_first = snake_obj.get_rect()
    point_rect_first = point_obj.get_rect()
        
    snake_rect = pygame.Rect(snake_px, snake_py, snake_rect_first.width, snake_rect_first.height)
    point_rect = pygame.Rect(point_px, point_py, point_rect_first.width, point_rect_first.height)
    
    # 如果蛇有吃到點
    if snake_rect.colliderect(point_rect):
        return True
    else:
        return False
    
def run():
    pygame.init()   # initial pygame

    # set sound of the game
    sound_obj = pygame.mixer.Sound('sound01.wav')
    
    basic_font = pygame.font.SysFont("arial", 16)   # 設定字型
    
    # 開視窗
    base_surf = pygame.display.set_mode((Gb_base_surf_width, Gb_base_surf_height))
    
    # read image
    snake_obj = pygame.image.load('snake_head.png') # for head of snake
    snake_obj = pygame.transform.scale( snake_obj, (Gb_snake_width, Gb_snake_height) )   # 縮小圖片大小
    
    snakeBody_obj = pygame.image.load('snake_head.png') # for body of snake
    snakeBody_obj = pygame.transform.scale( snakeBody_obj, (Gb_snake_width, Gb_snake_height) )   # 縮小圖片大小
    
    point_obj = pygame.image.load('point.jpg')  # for point
    point_obj = pygame.transform.scale( point_obj, (Gb_point_width, Gb_point_height) )   # 縮小圖片大小
    

    isRunning = True # boolean for game running or not

    
    snake_position = [] # initialize the position of snake body
    snake_position.append([10, 20]) # initialize the position of snake head
    print(snake_position)
    direction = HeadRight  # intial the direction
    
    # set the position of point
    point_px = random.randint(0, Gb_base_surf_width)
    point_py = random.randint(0, Gb_base_surf_height)
            
    player_point = 0
    
    pygame.key.set_repeat(1)    # 打開連續鍵盤輸入
    
    
    
    main_clock = pygame.time.Clock()
    while isRunning:
        main_clock.tick(Gb_game_clock) # set clock of the game(數字越大越快)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # 使用者離開
                isRunning = False
                
            if event.type == pygame.KEYDOWN:    # press keyboard
                # 使用者輸入上下左右
                if event.key == pygame.K_LEFT and direction != HeadRight:
                    direction = HeadLeft  # set the direction of snake
                if event.key == pygame.K_RIGHT and direction != HeadLeft:
                    direction = HeadRight  # set the direction of snake
                if event.key == pygame.K_UP and direction != HeadDown:
                    direction = HeadUp  # set the direction of snake
                if event.key == pygame.K_DOWN and direction != HeadUp:
                    direction = HeadDown  # set the direction of snake
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                sound_obj.play()
                
        eatPoint = False
        # 如果蛇有吃到點
        if eatFood(snake_obj, point_obj, snake_position, point_px, point_py):
            # snake body ++
            player_point += 1
            # change position of point
            point_px = random.randint(0, ( Gb_base_surf_width - Gb_point_width ) )
            point_py = random.randint(0, ( Gb_base_surf_height - Gb_point_height ) )
            eatPoint = True
        
        # snake go next position
        snake_position = goNextPosition( direction, snake_position, point_px, point_py, eatPoint )
        print('after next position : ', snake_position)
        
        #設定物件屬性
        base_surf.fill(BLACK)    # 上色，讓上一張blit的圖片消失

        #base_surf.blit(snake_obj, (snake_px, snake_py))    # 貼 img_obj 在base_surf 的px, py
        showSnake(base_surf, snake_obj, snakeBody_obj, snake_position)
        
        base_surf.blit(point_obj, (point_px, point_py))    # 貼加命菇 在base_surf 的 point_px, point_py

        #更新畫面
        pygame.display.update() #更新畫面
    exit()
    
    
    
run()