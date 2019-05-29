# Proyecto de Programacion - 2019 - i
# Autores: 
#    - Juan Montes
#    - Andres Morales 
#    - Ivan Hernandez
# Python 3.7 


import pygame as pg 
import sys, os 

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

from Nota import Nota
from Selector import Selector

from pygame.locals import *

# Algunas Constantes 
SIZE = width, height = 700,500 
COLOR = (0, 240 ,240)
RED = (255,0,0)
POSX = 20
# NOTA = import 

def main():
    print('Init Game...')
    nota = Nota(0,[200, 100])
    pg.init()
    screen = pg.display.set_mode(SIZE)
    pg.display.set_caption('pyHero - Demo')
    

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill(COLOR)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pg.display.flip()

    # Preconfiguracion del ciclo 
    POSX = 20
    show_selector = True

    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0,0))
        if show_selector:
            nota.show(screen)
            nota.move()

        if pg.key.get_pressed()[pg.K_SPACE]: 
           show_selector = False
        
        pg.display.flip()

    

if '__main__' == __name__: main()
