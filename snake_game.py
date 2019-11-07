import pygame
import time

pygame.init()


IS_RUNNING = True
base=pygame.display.set_mode((640,480))
game_font=pygame.font.SysFont(pygame.font.get_default_font(),40)

sound_obj = pygame.mixer.Sound("/Users/docoben/Desktop/python 遊戲課程/sound01.wav")
sound_obj.play()

player_imamge1 = pygame.image.load("snake_whole.png")


px, py = 100, 200
direction_mode = 1

# idx = 0

# player_stretchedimage = pygame.transform.scale(player_imamge1,(40,40))


while IS_RUNNING:

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            IS_RUNNING = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                direction_mode = 1
            if e.key == pygame.K_LEFT:
                direction_mode = 2
            if e.key == pygame.K_UP:
                direction_mode = 3
            if e.key == pygame.K_DOWN:
                direction_mode = 4

        
    if direction_mode == 1:
        px += 10  
    elif direction_mode == 2:
        px -= 10  
    elif direction_mode == 3:
        py -= 10 
    elif direction_mode == 4:
        py += 10
    

    time.sleep(1)
    # create window
    base.fill((0,0,0))
    # idx %= 6
    base.blit(player_imamge1, (px,py))
    pygame.display.update() #update 視窗
    # idx += 1
    # time.sleep(0.1)
    


exit()
