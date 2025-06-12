import pygame
import random

#Inizializzazione
pygame.init()


#Creazione immagini
sfondo = pygame.image.load('img/sfondo.png')
uccello = pygame.image.load('img/uccello.png')
base = pygame.image.load('img/base.png')
gameover = pygame.image.load('img/gameover.png')
tubo_under = pygame.image.load('img/tubo.png')
tubo_up = pygame.transform.flip(tubo_under, False, True)

#Global const
WINDOW = pygame.display.set_mode((300, 550))
FPS = 60

running = True

while running:


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


pygame.quit()