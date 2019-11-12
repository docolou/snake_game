# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:34:28 2019

@author: a9302
"""

import pygame
import random
import time

BLACK = (0, 0, 0)
RED = (255, 0, 0)

# direction of snake
HeadRight = 0
HeadLeft = 1
HeadUp = 2
HeadDown = 3

def goNextPosition( headDirection, px, py ):
    if headDirection == HeadRight:
        px += 1
    elif headDirection == HeadLeft:
        px -= 1
    elif headDirection == HeadUp:
        py -= 1
    elif headDirection == HeadDown:
        py += 1
    return px, py        

def run():
    pygame.init()   # initial pygame

    # set sound of the game
    sound_obj = pygame.mixer.Sound('sound01.wav')
    
    basic_font = pygame.font.SysFont("arial", 16)   # 設定字型
    
    # 開視窗
    base_surf = pygame.display.set_mode((640, 480))
    
    # read image
    snake_obj = pygame.image.load('1.gif')

    isRunning = True # boolean for game running or not

    px, py = 10, 20 # intial the position
    direction = HeadRight  # intial the direction
    
    pygame.key.set_repeat(1)    # 打開連續鍵盤輸入
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
                
            if event.type == pygame.KEYDOWN:    # press keyboard
                if event.key == pygame.K_LEFT:
                    direction = HeadLeft  # set the direction of snake
                if event.key == pygame.K_RIGHT:
                    direction = HeadRight  # set the direction of snake
                if event.key == pygame.K_UP:
                    direction = HeadUp  # set the direction of snake
                if event.key == pygame.K_DOWN:
                    direction = HeadDown  # set the direction of snake
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                sound_obj.play()
                    
        
        # go next position
        px, py = goNextPosition( direction, px, py )
        
        
        #設定物件屬性
        base_surf.fill(BLACK)    # 上色，讓上一張blit的圖片消失


        base_surf.blit(snake_obj, (px, py))    # 貼 img_obj 在base_surf 的px, py
        #更新畫面
        pygame.display.update() #更新畫面
        time.sleep(0.01) # slow down the speed of the game
    exit()
    
    
    
run()