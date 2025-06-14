import pygame
import random
import math

#Inizializzazione
pygame.init()
random.seed()

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
pipe_distance = 100


#METODI

def inizializza():

    global birdX, birdY, birdVY
    birdX, birdY, = 70, 150
    birdVY = 0

    global baseX, baseY, baseVX
    baseX = 0
    baseY = 400
    baseVX = -2

    global tuboUpX, tuboUpY, tuboUpVX
    tuboUpX = -100
    tuboUpY = 0
    tuboUpVX = -2

    global tuboUnX, tuboUnY, tuboUnVX
    tuboUnX = -100
    tuboUnY = 0 
    tuboUnVX = -2 

def upload():

    pygame.display.update()
    pygame.time.Clock().tick(FPS)

#piazzamento PNG

def printa():

    WINDOW.blit(sfondo, posizione_sfondo)
    WINDOW.blit(uccello, (birdX, birdY))
    WINDOW.blit(tubo_up, (tuboUpX, tuboUpY))
    WINDOW.blit(tubo_under, (tuboUnX, tuboUnY))
    WINDOW.blit(base, (baseX, baseY))







#___MAIN___

running = True

inizializza()


while running:


    birdVY += 1
    birdY += birdVY
    baseX += baseVX
    tuboUpX += tuboUpVX
    tuboUnX += tuboUnVX

    if baseX < -50: baseX = 0
    
    if tuboUpX < -100:

        tmp = random.randrange(50, 320)

        tuboUpX = random.randrange(250, 400)
        tuboUnX = tuboUpX
        tuboUpY = tmp - 320 - (pipe_distance / 2)
        tuboUnY = tmp + (pipe_distance / 2)
        

    printa()
    upload() 


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                
                birdVY = -10

    
 
 