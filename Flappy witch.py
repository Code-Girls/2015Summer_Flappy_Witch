# 1 - Import Library
import pygame
from pygame.locals import *
import random

# 2 - Initialize the game
pygame.init()
pygame.mixer.init()
width,height = 800,583
screen=pygame.display.set_mode((width,height))
playerpos = [200,182]
badtimer = 200
badtimer1 = 0
bound_ups=[[800,0]]
bound_downs=[[800,400]]

# 3 - Load images
sky = pygame.image.load("resouces/images/dawn.jpg")
playerimg1 = pygame.image.load("resouces/images/witch1.png")
playerimg2 = pygame.image.load("resouces/images/witch2.png")
bound_upimg2 = pygame.image.load("resouces/images/b_u.png")
bound_upimg = pygame.image.load("resouces/images/ghost.png")
bound_downimg = pygame.image.load("resouces/images/c_d.png")
castle_downimg = pygame.image.load("resouces/images/c_d.png")
gameover = pygame.image.load("resouces/images/gameover.png")
youwin =pygame.image.load("resouces/images/youwin.png")

# 3.2 - Load sounds
jump = pygame.mixer.Sound("resouces/sounds/fly.wav")
crash = pygame.mixer.Sound("resouces/sounds/crash.mp3")
jump.set_volume(0.05)
crash.set_volume(0.45)
pygame.mixer.music.load('resouces/sounds/back.mp3')
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.35)


# 4 - keep looping through
count = 0
score = 0
running = 1
# exitcode = 1
while running:
    badtimer -=1
    s = 3
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(sky,(0,0))   
    if count % 2 == 0:                       # anime effect
        screen.blit(playerimg1,playerpos)
    else:
        screen.blit(playerimg2,playerpos)
    count += 1
    
    count += 1
    # 6.1 Get the bird Moving                   
    if playerpos[1] > height - 85 :
        playerpos[1] = height - 85
    elif playerpos[1]< 0 :
        playerpos [1] = 0
    else:
        playerpos[1] +=3


    #6.2 - Draw the bound
    if badtimer ==0:
        y = random.randint(-50,100)
        bound_ups.append([800,y])
        bound_downs.append([800,y+300])
        score +=1
        badtimer = 200 -(badtimer1*2)
        if badtimer1 >=10:
            badtimer1 =10
        else:
            badtimer1 +=1
    index =0
    for bound_up in bound_ups:
        if bound_up[0] <-102:   
            bound_ups.pop(index)
        bound_up[0] -=s
        index +=1


    for bound_up in bound_ups: 
        screen.blit(bound_upimg,bound_up)
    
       
        
    index1 =0 
    for bound_down in bound_downs:
        if bound_down[0] <-102:   
            bound_downs.pop(index1)
        bound_down[0] -=s

        index1 +=1
    for bound_down in bound_downs:
        screen.blit(bound_downimg,bound_down)

    s +=2
        
        

    # 6.3 - Crash the bound
    for bound_down in bound_downs:
        bound_downrect = pygame.Rect(bound_downimg.get_rect()) 
        bound_downrect.left = bound_down[0]
        bound_downrect.top = bound_down[1]
    
        playerrect = pygame.Rect(playerimg2.get_rect()) 
        playerrect.left = playerpos[0]
        playerrect.top = playerpos[1]

    
    
    for bound_up in bound_ups:
        bound_uprect = pygame.Rect(bound_upimg.get_rect()) 
        bound_uprect.left = bound_up[0]
        bound_uprect.top = bound_up[1]  
    
        playerrect = pygame.Rect(playerimg2.get_rect()) 
        playerrect.left = playerpos[0]
        playerrect.top = playerpos[1]


    

    # 6.4 Draw score
    font = pygame.font.Font(None,48)
    survivedtext = font.render("Score: "+str(score), True, (165,224,244))
    textRect = survivedtext.get_rect()
    textRect.topright = [450, 5]
    screen.blit(survivedtext, textRect)

    

        
    # 7 - update the screen
    pygame.display.flip()
   
    # 8 - loop through the events
    for event in pygame.event.get():
        #check if the X button#
        if event.type == pygame.QUIT:
            #if it is quit the game
            pygame.quit()
            exit(0)
    
    # 9 - Jumping 
    if event.type == pygame.MOUSEBUTTONDOWN:
        playerpos[1] -=10
        jump.play()

    # 10 - Win/Lose check
    if score == 10:
        running = 0
        exitcode =1
    if playerrect.colliderect(bound_uprect):
        running = 0
        exitcode = 0
        crash.play()
    if playerrect.colliderect(bound_downrect):
        running = 0
        exitcode = 0
        crash.play()

    # 11 - Win/Lose display
if exitcode ==0:                                            #Lose
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Score: "+str(score), True, (136,0,21))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(gameover, (0,0))
    screen.blit(text, textRect)

else:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Score: "+str(score), True, (69,186,128))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(youwin, (0,0))
    screen.blit(text, textRect)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()




 

    
      





   
 
