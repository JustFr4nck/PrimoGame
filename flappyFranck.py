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

#Inizializzazione finestra

WINDOW = pygame.display.set_mode((280, 488))
FPS = 60


#METODI

def inizializza():

    global birdX, birdY, birdVY
    birdX, birdY, = 70, 150
    birdVY = 0

    global baseX, baseY, baseVX
    baseX = -50
    baseY = 400
    baseVX = -2   

def upload():

    pygame.display.update()
    pygame.time.Clock().tick(FPS)

#piazzamento PNG

def printa():

    WINDOW.blit(sfondo, posizione_sfondo)
    WINDOW.blit(base, (baseX, baseY))
    WINDOW.blit(uccello, (birdX, birdY))




#___MAIN___

running = True

inizializza()

while running:

    birdVY += 1
    birdY += birdVY
    baseX += baseVX

    printa()
    upload()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                
                birdVY = -10
 
