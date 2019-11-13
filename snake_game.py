import pygame, sys
import time
import random

pygame.init()


IS_RUNNING = True
base=pygame.display.set_mode((690,510))
game_font=pygame.font.SysFont(pygame.font.get_default_font(),40)
surface = game_font.render('hello python!',False,(255,200,10))


sound_obj = pygame.mixer.Sound("/Users/docoben/Desktop/python 遊戲課程/sound01.wav")
sound_obj.play()

snake_head = pygame.image.load("snake_head.png")
snake_straight = pygame.image.load("snake_straight.png")
snake_straight = pygame.transform.scale(snake_straight,(30,30)) #縮小或放大圖片用
snake_tail = pygame.image.load("snake_tail.png")
mushroom = pygame.image.load("mushroom.png")
mushroom = pygame.transform.scale(mushroom,(30,30)) #縮小或放大圖片用


px, py = 150, 180
direction_mode = 1
point = [[90, 180], [120, 180], [150, 180]]

#隨機產生食物位置-第一次
food_point_px = random.randrange(30, 600, 30)
food_point_py = random.randrange(30, 420, 30)





while IS_RUNNING:

    for detect_key in pygame.event.get():

        if detect_key.type == pygame.QUIT:
            IS_RUNNING = False

        if detect_key.type == pygame.KEYDOWN:
            if detect_key.key == pygame.K_RIGHT:
                direction_mode = 1
            if detect_key.key == pygame.K_LEFT:
                direction_mode = 2
            if detect_key.key == pygame.K_UP:
                direction_mode = 3
            if detect_key.key == pygame.K_DOWN:
                direction_mode = 4

    if direction_mode == 1:
        px += 30 
    elif direction_mode == 2:
        px -= 30  
    elif direction_mode == 3:
        py -= 30 
    elif direction_mode == 4:
        py += 30
    
    
  
    #蛇是否有碰撞到食物
    rect_snake_head = pygame.Rect(px, py, 30, 30)  # (left, top, width, height)
    rect_food = pygame.Rect(food_point_px, food_point_py, 30, 30)
    if  pygame.Rect.colliderect(rect_snake_head, rect_food):
        #隨機產生食物位置
        food_point_px = random.randrange(30, 600, 30)
        food_point_py = random.randrange(30, 420, 30)
        #新增跟刪除蛇的座標
        point.append([px, py])
        print(point)
        #結束遊戲畫面
        # exit()

    else:
        #新增跟刪除蛇的座標
        point.append([px, py])
        point.pop(0)
        print(point)

    rect_wall_1 = pygame.Rect(0, 0, 690, 30)
    rect_wall_2 = pygame.Rect(0, 0, 30, 510)
    rect_wall_3 = pygame.Rect(660, 0, 30, 510)
    rect_wall_4 = pygame.Rect(0, 480, 690, 30)
    if  pygame.Rect.colliderect(rect_snake_head, rect_wall_1):
        exit()
    if  pygame.Rect.colliderect(rect_snake_head, rect_wall_2):
        exit()
    if  pygame.Rect.colliderect(rect_snake_head, rect_wall_3):
        exit()
    if  pygame.Rect.colliderect(rect_snake_head, rect_wall_4):
        exit()
    
    # create window
    base.fill((0,0,0)) #避免殘影
    base.blit(mushroom, (food_point_px, food_point_py)) #放上香菇
    for point_px,point_py in point:#放上蛇的身體
        base.blit(snake_straight, (point_px,point_py)) 
    #外牆
    pygame.draw.rect(base,[0,0,255],[0,0,690,30],0) #Rect(left,top,width,height)
    pygame.draw.rect(base,[0,0,255],[0,0,30,510],0)
    pygame.draw.rect(base,[0,0,255],[660,0,30,510],0)
    pygame.draw.rect(base,[0,0,255],[0,480,690,30],0)
      
    pygame.display.update() #update 視窗
    time.sleep(0.3)
    


exit()
