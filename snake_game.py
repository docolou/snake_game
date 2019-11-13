import pygame, sys
import time

pygame.init()


IS_RUNNING = True
base=pygame.display.set_mode((640,480))
game_font=pygame.font.SysFont(pygame.font.get_default_font(),40)

sound_obj = pygame.mixer.Sound("/Users/docoben/Desktop/python 遊戲課程/sound01.wav")
sound_obj.play()

snake_head = pygame.image.load("snake_head.png")
snake_straight = pygame.image.load("snake_straight.png")
snake_straight = pygame.transform.scale(snake_straight,(30,30)) #縮小或放大圖片用
snake_tail = pygame.image.load("snake_tail.png")



# snake = pygame.transform.scale(snake,(80,80)) #縮小或放大圖片用

px, py = 100, 200
direction_mode = 1





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


    point = [(100, 200), (130, 200), (160, 200), (160, 170)]
    point = { }

    point_px = [100, 130, 160]
    point_py = [200, 200, 200]

    if direction_mode == 1:
        px += 30 
    elif direction_mode == 2:
        px -= 30  
    elif direction_mode == 3:
        py -= 30 
    elif direction_mode == 4:
        py += 30

  
    
    
    # create window
    base.fill((0,0,0)) #避免殘影

    # base.blit(snake_head, (px,py-300))
    # base.blit(snake_straight, (px,py))    
    # base.blit(snake_straight, (px+30,py))
    # base.blit(snake_straight, (px+60,py))
    for point_px,point_py in point:
        base.blit(snake_straight, (point_px,point_py))    
    # base.blit(snake_tail, (px,py+67))
    pygame.display.update() #update 視窗
    time.sleep(0.5)
    


exit()
