import pygame
import time

pygame.init()


IS_RUNNING = True
base=pygame.display.set_mode((640,480))
game_font=pygame.font.SysFont(pygame.font.get_default_font(),40)

sound_obj = pygame.mixer.Sound("/Users/docoben/Desktop/python 遊戲課程/sound01.wav")
sound_obj.play()

player_imamge1 = pygame.image.load("/Users/docoben/Desktop/python 遊戲課程/santas/1.gif")
player_imamge2 = pygame.image.load("/Users/docoben/Desktop/python 遊戲課程/santas/2.gif")
player_imamge3 = pygame.image.load("/Users/docoben/Desktop/python 遊戲課程/santas/3.gif")
player_imamge4 = pygame.image.load("/Users/docoben/Desktop/python 遊戲課程/santas/4.gif")
player_imamge5 = pygame.image.load("/Users/docoben/Desktop/python 遊戲課程/santas/5.gif")
player_imamge6 = pygame.image.load("/Users/docoben/Desktop/python 遊戲課程/santas/6.gif")

santas = [player_imamge1, player_imamge2, player_imamge3, player_imamge4, player_imamge5, player_imamge6]
px, py = 100, 200

# idx = 0

# player_stretchedimage = pygame.transform.scale(player_imamge1,(40,40))


while IS_RUNNING:

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            IS_RUNNING = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                px += 1
            if e.key == pygame.K_LEFT:
                px -= 1
            if e.key == pygame.K_UP:
                py -= 1
            if e.key == pygame.K_DOWN:
                py += 1  

    
    # create window
    base.fill((0,0,0))
    # idx %= 6
    base.blit(santas[1], (px,py))
    pygame.display.update() #update 視窗
    # idx += 1
    # time.sleep(0.1)
    


exit()
