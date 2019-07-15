
"""Implementación fondo de pantalla, se ajusta el tamaño
Integrantes:
Andrés Morales
Iván Hernandez 
Juan Ramirez
Leider Rozo"""

import os
import pygame
from pygame.locals import *

ROOT = '/assets/images/'

def create_fondo():
    return 


pygame.init()
screen = pygame.display.set_mode((200, 200), HWSURFACE | DOUBLEBUF | RESIZABLE)
pic = pygame.image.load(os.getcwd() + ROOT + 'juego_fondo.png')
#pygame.image.load("sin.png")
pygame.display.update()
screen.blit(pygame.transform.scale(pic, (200, 200)), (0, 0))
pygame.display.flip()







while True:
    pygame.event.pump()
    event = pygame.event.wait()
    if event.type == QUIT:

        pygame.display.quit()
    elif event.type == VIDEORESIZE:
        screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
        screen.blit(pygame.transform.scale(pic, event.dict['size']), (0, 0))
        pygame.display.flip()

