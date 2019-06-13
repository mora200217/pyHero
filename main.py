# Proyecto de Programacion - 2019 - i
# Autores: 
#    - Juan Montes
#    - Andres Morales 
#    - Ivan Hernandez
# Python 3.7 

import pygame as pg 
import sys, os, random
import time

from Nota import Nota
from Selector import Selector
from pygame.locals import *
pg.init()
# Algunas Constantes 
SIZE = width, height = 700,500 
COLOR = (44, 62, 80)
RED = (255,0,0)
POSX = 201
SEPARACION_NOTAS = 100
TIEMPO_APARICION = 100
DIVISION_SELECTORES = 110


ROOT = 'assets/music/'

notas = []
selectores = []

count = 0

reloj = pg.time.Clock()

def main():
    puntaje=0
    fuente=pg.font.Font(None,30)
    
    marcador=fuente.render(str(puntaje),0,(255,255,255))
    count = 0
    pg.init()

    screen = pg.display.set_mode(SIZE)
    pg.display.set_caption('pyHero - Demo')
    

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill(COLOR)

    def lanzar_nota(): 
        '''
        Crear una nota 
        '''
        id_nota = random.randint(0,3)
        fixed = (width / 2) - (DIVISION_SELECTORES * 1.15)
        return Nota(id_nota, fixed + DIVISION_SELECTORES / 2* id_nota, width, height, DIVISION_SELECTORES)

    def mostrar_traste():
        '''
        Mostrar la imagen cargada del traste
        '''
        traste = pg.image.load("assets/notas/traste.png")
        traste_width  = 700
        traste_height = 750
        screen.blit(pg.transform.scale(traste, (traste_width , traste_height)), [(width - traste_width) * 0.5, height / 2 - 500]) # Posicion del traste / ONG
        
    def get_music(cancion = 0): 
        '''
        Devolver la ruta de una canción aleatoria. 
        Canción 0 como por defecto
        '''
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
    #pg.mixer.music.pause()

    div = 100
    # Crear selectores -----------
    for selector in range(0, 4):
        selectores.append(Selector(selector, width, height, DIVISION_SELECTORES))
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
                if nota.pos[1] >= selectores[0].pos[1] + 50: 
                   notas.remove(nota)
                   marcador=fuente.render(str(puntaje),0,(255,255,255))
                   puntaje=puntaje-10
                   #screen.blit(marcador,(100,100))
                if abs(nota.pos[1] - selectores[nota.type].pos[1]) <= 10 and pg.key.get_pressed()[nota.get_type()] and pg.key.get_pressed()[K_SPACE]: 
                   notas.remove(nota)
                   puntaje=(puntaje+10-0.5*abs(nota.pos[1] - selectores[nota.type].pos[1]))//1
                   marcador=fuente.render(str(puntaje),0,(255,255,255)) 
                   #screen.blit(marcador,(100,100))
                screen.blit(marcador,(100,100))    
        if count % TIEMPO_APARICION == 0: 
            notas.append(lanzar_nota())
        count += 1
        pg.display.flip()
    reloj.tick(500)
    pg.display.update()

if '__main__' == __name__: main()
