import pygame
from pygame.locals import *
 
pygame.init()
 
pantalla = pygame.display.set_mode((470,300),0,32)
pygame.display.set_caption("Modulo Music")
 
reloj = pygame.time.Clock()
 
pygame.mixer.music.load("Pastor Lopez - El hijo ausente.mp3")
pygame.mixer.music.play(1)
while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()
        if eventos.type == pygame.KEYDOWN:
            if eventos.key == pygame.K_p:
                pygame.mixer.music.stop()
    reloj.tick(20)
    pygame.display.update()


