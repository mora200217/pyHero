# Proyecto de Programacion - 2019 - i
# Autores: 
#    - Juan Montes
#    - Andres Morales 
#    - Ivan Hernandez
# Python 3.7 


import pygame as pg 
import sys, os, random
import time
from pygame.locals import *
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

from Nota import Nota
from Selector import Selector
# from Selector import Selector

from pygame.locals import *

# Algunas Constantes 
SIZE = width, height = 700,500 
COLOR = (44, 62, 80)
RED = (255,0,0)
POSX = 201
SEPARACION_NOTAS = 100
TIEMPO_APARICION = 100
notas = []
selectores = []
# NOTA = import 
count = 0

ROOT = 'assets/music/'

poner_divisores = False

reloj = pg.time.Clock()


def main():
    puntaje=0
    print('Init Game...')
    count = 0
    pg.init()
    screen = pg.display.set_mode(SIZE)
    pg.display.set_caption('pyHero - Demo')
    

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill(COLOR)

    def lanzar_nota(): 
        id_nota = random.randint(0,3)
        fixed = (width / 2) - (2 * SEPARACION_NOTAS)
        return Nota(id_nota, fixed + SEPARACION_NOTAS * id_nota)

    def mostrar_traste():
        traste = pg.image.load("assets/notas/traste.png")
        traste_width  = 700
        traste_height = 750
        screen.blit(pg.transform.scale(traste, (traste_width , traste_height)), [(width - traste_width) * 0.5, height / 2 - 500]) # Posicion del traste / ONG
        

    def crear_divisor():
        pg.draw.line(screen, (0, 0, 0), [0,height * 0.9], [width, height * 0.9])

    def divisor_vertical(): 
        pg.draw.line(screen, (0, 0, 0), [width / 2,0], [width / 2, height])

    def get_music(cancion = 0): 
        return str(random.randint(1,15)) if cancion == 0 else str(cancion)

    #def eliminacion_notas():

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pg.display.flip()

    # Preconfiguracion del ciclo 
    POSX = 20
    
    show_selector = True
    pg.mixer.pre_init()
    pg.mixer.music.load(ROOT + get_music()+".mp3")
    pg.mixer.music.play(1)
    pg.mixer.music.pause()

    div = 100
    # Crear selectores -----------
    for selector in range(0, 4):
        selectores.append(Selector(selector, width, height))
    while True:
       
        54
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
            #evalua si la tecla presionada es la p de pausar
                if event.key == pg.K_p:
                #pausa la musica
                    pg.mixer.music.pause()
                if event.key == pg.K_u:
                #despausa la musica
                    pg.mixer.music.unpause()

        screen.blit(background, (0,0))
        mostrar_traste()
        
        
        for selector in selectores:
            pos_temp = selector.get_pos()[0]
            abs_pos = abs(width / 2 - pos_temp) / (width/2 - pos_temp)
            pos_temp = abs(width/2 - pos_temp)/2 * (abs_pos) + selector.get_pos()[0]
            pg.draw.line(screen, (255,255,255), selector.get_pos(), (pos_temp, height / 2 - 56), 20)
            selector.show(screen)

        if notas: # && selectores:
            for nota in notas:
                if show_selector:
                    nota.show(screen)
                    nota.move()
                if nota.pos[1] >= selectores[0].pos[1] + 20: 
                   notas.remove(nota)
                   print(puntaje)
                   puntaje=puntaje-1
                if abs(nota.pos[1] - selectores[nota.type].pos[1]) <= 10 and pg.key.get_pressed()[nota.get_type()] and pg.key.get_pressed()[K_SPACE]: 
                   notas.remove(nota)
                

    # Divisores --------------------
        if poner_divisores:
            crear_divisor() 
            divisor_vertical() 
         # show_selector = False if pg.key.get_pressed()[pg.K_SPACE] else pass  
        
        if count % TIEMPO_APARICION == 0: 
            notas.append(lanzar_nota())
        
        count += 1
         
          
        
        pg.display.flip()
    reloj.tick(500)
    pg.display.update()

    


if '__main__' == __name__: main()
