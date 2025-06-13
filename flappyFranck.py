import pygame
import random
import math

#Inizializzazione
pygame.init()


#Creazione immagini
sfondo = pygame.image.load('img/sfondo.png')
uccello = pygame.image.load('img/uccello.png')
base = pygame.image.load('img/base.png')
gameover = pygame.image.load('img/gameover.png')
tubo_under = pygame.image.load('img/tubo.png')
tubo_up = pygame.transform.flip(tubo_under, False, True)

#Posizione immagini

posizione_sfondo = (0, 0)
posizione_base = (-50, 400)

#POSIZIONE UCCELLO
x_bird = 90
y_bird = 200
pos_bird = (x_bird, y_bird)
vertical_speed = 0
n = 0

#Global const
WINDOW = pygame.display.set_mode((284, 488))
FPS = 60


def print_objects():

    WINDOW.blit(sfondo, posizione_sfondo)
    WINDOW.blit(uccello, pos_bird)
    WINDOW.blit(base, posizione_base)

def update():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def bird_action(y_bird, vertical_speed, n):

    vertical_speed += 1^n

    y_bird += vertical_speed

    return y_bird

def bird_up(y_bird, vertical_speed):

    vertical_speed = -130    

    y_bird += vertical_speed  

    return y_bird





#___MAIN___

running = True

while running:

    n += 1

    print_objects()
    y_bird = bird_action(y_bird, vertical_speed, n)
    pos_bird = (x_bird, y_bird)
    update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                y_bird = bird_up(y_bird, vertical_speed)
                pos_bird = (x_bird, y_bird)
                n = 0

   



pygame.quit()