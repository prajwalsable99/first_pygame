#initialize
import os 
import sys
import random
import pygame
import time


from pygame import mixer
x=pygame.init()
print(x)

#creating game window
screen_wid=1000
screen_hei=500
gamewindow=pygame.display.set_mode((screen_wid,screen_hei))

#title to game

pygame.display.set_caption("prajwal_ka_game")
pygame.display.update()

#game_variables

exit_game=False
Game_over=False
fps=30
clock=pygame.time.Clock()
#game_colors

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,255,0)
blue=(0,0,255)
#charcter_var
snake_x=200
snake_y=150
snake_size=20

move_x=0
move_y=0
n=10
food_x=random.randint(100,screen_wid-100)
food_y=random.randint(100,screen_hei-100)


m1='Elektronomia_Sky_High.mp3'
m2='Dil-Wale-Puchde-Ne-Cha-Oooo-Ringtone.mp3'
mixer.music.load(m1)
mixer.music.play(-1)
#display score
score=0

font=pygame.font.SysFont(None,30)
def showscore(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])

#Game lOOP

while not exit_game:
    

    for event in pygame.event.get():
        #print(event)
        if event.type==pygame.QUIT:
            exit_game=True
            

        if event.type ==pygame.KEYDOWN:
            
            if event.key == pygame.K_RIGHT:
                move_x=n
                move_y=0
            
            if event.key == pygame.K_LEFT:
                move_x=-n
                move_y=0
               
            if event.key == pygame.K_UP:
                move_x=0
                move_y=-n

            if event.key == pygame.K_DOWN:
                move_x=0
                move_y=n
               
                
                
    snake_x=snake_x + move_x
    snake_y=snake_y+ move_y
    
    if abs(snake_x-food_x)<17 and abs(snake_y-food_y)<17:
        score=score+1
        # print("score=",score)
        # showscore("score : "+str(score),blue,5,5)
        food_x=random.randint(80,screen_wid-80)
        food_y=random.randint(80,screen_hei-80)
        
        n=n+2


     
    
   
       
        
       

    if snake_y<30 or snake_x<33 or snake_x >975 or snake_y>475:
        
        exit_game=True
        


    gamewindow.fill(green)
    showscore("can u score above 50 ||score : "+str(score),blue,70,5)


   

    pygame.draw.rect(gamewindow,black,[0,25,1000,25])
    pygame.draw.rect(gamewindow,black,[0,475,1000,500]) 
    pygame.draw.rect(gamewindow,black,[0,0,25,500])
    pygame.draw.rect(gamewindow,black,[975,0,1000,500])

    pygame.draw.rect(gamewindow,red,[food_x,food_y,15,15])

   

    pygame.draw.rect(gamewindow,blue,[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps)





#quitting game function

end=mixer.music.load(m2)
mixer.music.play()
time.sleep(10)
pygame.quit()
quit()

