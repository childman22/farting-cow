#importing the libraries
import pygame
import os
import sys
import random
import time

#general setup
pygame.init()
clock = pygame.time.Clock()

#setting up the main window
screen_width = 900
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('cow')

#cords
cow_x = 400
cow_y = 200

sci1_x = 700
sci1_y = 200

sci2_x = 100
sci2_y = 100

#randoms
sounds = ['fart.mp3', 'fart2.mp3']

#importing the files
sciai = pygame.Rect(sci1_x,sci1_y,100,100)
sciimg = pygame.transform.scale(pygame.image.load("scientist1.jpg"), (100, 100))
cows = pygame.Rect(cow_x,cow_y,100,100)
cowimg = pygame.transform.scale(pygame.image.load("cow1.jpg"), (100, 100))

#colours
bgcolour = (185,185,185)
grey = pygame.Color('grey12')
in_colour = pygame.Color('black')
red = (213,50,80)
blue = (0,0,255)

#fonts
pygame.font.init()
font1 = pygame.font.SysFont(None, 30)

#instructions
cow_in = font1.render('wasd for cow', False, in_colour)
fart_in = font1.render('space = fart', False, in_colour)
lives_in = font1.render('3 lives', False, in_colour)
health_in = font1.render('health: 50', False, in_colour)

#speeds
cow_change_x = 0
cow_change_y = 0

sci_speed_x = 3
sci_speed_y = 3

#variables
damage1 = 0
game_close = False
game_over = 0
health = 50

#defining
def message(msg, color):
    mesg = font1.render(msg, True, color)
    screen.blit(mesg, [350, screen_height / 2])

while True:
    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            #sounds
            if event.key == pygame.K_SPACE:
                fart = random.choice(sounds)
                fartsnd = pygame.mixer.music.load(fart)
                pygame.mixer.music.play()
                damage1 +=1
                health -=1
                healths = 'health: %.0f' % health
                health_in = font1.render(healths, False, in_colour)
                print(healths)
            #cow controls
            if event.key == pygame.K_w:
                cow_change_y -=4
            if event.key == pygame.K_s:
                cow_change_y +=4
            if event.key == pygame.K_a:
                cow_change_x -=4
            if event.key == pygame.K_d:
                cow_change_x +=4
            #restart
            if event.key == pygame.K_c:
                health = 50
            #quit
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYUP:
            #cow controls
            if event.key == pygame.K_w:
                cow_change_y +=4
            if event.key == pygame.K_s:
                cow_change_y -=4
            if event.key == pygame.K_a:
                cow_change_x +=4
            if event.key == pygame.K_d:
                cow_change_x -=4

    #game functions
    cows.y += cow_change_y
    cows.x += cow_change_x
    cow_x += cow_change_x
    cow_y += cow_change_y
    sciai.y += sci_speed_y
    sciai.x += sci_speed_x

    #time functions
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    textsurface = font1.render(current_time, False, in_colour)
    
    #scientist animation
    if sciai.top <= 0 or sciai.bottom >= screen_height:
        sci_speed_y *= -1
    if sciai.left <= 0 or sciai.right >= screen_width:
        sci_speed_x *= -1

    #collision
    if cows.colliderect(sciai):
        print("game over")
        game_over +=1
    if game_over == 30:
        lives_in = font1.render('2 lives', False, in_colour)
    if game_over == 60:
        lives_in = font1.render('1 lives', False, in_colour)
    if game_over == 90:
        cowimg = pygame.transform.scale(pygame.image.load("burger1.jpg"), (100, 100))
    if game_over == 100:
        pygame.quit()
        sys.exit()
        
    #cow stopper
    if cows.top <= 0:
        cows.top = 0
    if cows.bottom >= screen_height:
        cows.bottom = screen_height
    if cows.left <= 0:
        cows.left = 0
    if cows.right >= screen_width:
        cows.right = screen_width

    #visuals
    screen.fill(bgcolour)
    screen.blit(cowimg, (cows))
    screen.blit(sciimg, (sciai))
    screen.blit(cow_in, (10, 30))
    screen.blit(fart_in, (10, 10))
    screen.blit(lives_in, (10, 50))
    screen.blit(textsurface, (800, 10))
    screen.blit(health_in, (10, 70))
    
    #scientist health
    if damage1 >= 50:
        screen.fill(blue)
        message("You Win! Press Q to quit", red)

    #updating the window
    pygame.display.flip()
    clock.tick(60)        
