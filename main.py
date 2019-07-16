# Proyecto de Programacion - 2019 - i
# Autores: 
#    - Juan Montes
#    - Andres Morales 
#    - Ivan Hernandez
# Python 3.7 

import pygame as pg 
import sys, os, random
import time
import ctypes

from Nota import Nota
from Selector import Selector
from Punto import Punto
from guitar import get_color, toca
from pygame.locals import *



# Algunas Constantes 
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
SIZE = width, height = 700,500 
COLOR = (44, 62, 80)
RED = (255,0,0)
POSX = 201
SEPARACION_NOTAS = 100
TIEMPO_APARICION = 50
DIVISION_SELECTORES = 110


ROOT = 'assets/music/'
ROOT_2 = '/assets/images/'

notas = []
selectores = []

count = 0

reloj = pg.time.Clock()

def main(numero_cancion,dificulad):
    pg.joystick.init() # Iniciar el reconocimiento de controles (Joysticks)
    guitar = pg.joystick.Joystick(0) # Acceder al primer controlador (Guitarra)
    
    fondo = pg.display.set_mode((200, 200), HWSURFACE | DOUBLEBUF | RESIZABLE)

    puntaje = Punto() # Definir el sistema de puntuación como objeto

    #define la fuente del marcador
    font = pg.font.Font('assets/fonts/sb.ttf', 140)
    #renderiza la fuente
    
    count = 0
    pg.init()

    
    screen = pg.display.set_mode(SIZE)
    pic = pg.image.load(os.getcwd() + ROOT_2 + 'juego_fondo.png')
    #pygame.image.load("sin.png")
    pg.display.update()
    k  = 0.9
    pic = pg.transform.scale(pic, (width,height))
    
    pg.display.flip()
    pg.display.set_caption('pyHero - Demo')
    

    background = pg.Surface(screen.get_size())
    background = background.convert()
    
    background.blit(pic,[0,0])
    marcador=font.render(str(puntaje.puntuacion_actual()),0,(44, 62, 80))

    def lanzar_nota(): 
        '''
        Crear una nota 
        '''
        id_nota = random.randint(0,3)
        fixed = (width / 2) - (DIVISION_SELECTORES * 1.15)
        return Nota(id_nota, fixed + DIVISION_SELECTORES / 2* id_nota, width, height, DIVISION_SELECTORES, dificulad)

    def mostrar_traste():
        '''
        Mostrar la imagen cargada del traste
        '''
        traste = pg.image.load("assets/notas/traste.png")
        traste_width  = 700
        traste_height = 750
        screen.blit(pg.transform.scale(traste, (traste_width , traste_height)), [(width - traste_width) * 0.5, height / 2 - 500]) # Posicion del traste / ONG
    #def eliminacion_notas():

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pg.display.flip()

    # Preconfiguracion del ciclo 
    POSX = 20
    
    show_selector = True
    pg.mixer.pre_init()
    pg.mixer.music.load(ROOT + str(10 + numero_cancion) +".mp3")
    pg.mixer.music.play(1)
    #pg.mixer.music.pause()

    div = 100
    # Crear selectores -----------
    for selector in range(0, 4):
        selectores.append(Selector(selector, width, height, DIVISION_SELECTORES))
    game = True
    esta_tocando = False
    puntaj = 0
    while game:
       
        
        def get_color_type():
            if toca(guitar) and not(esta_tocando):
                col = get_color(guitar)
                if col != None:
                    return col

            


        if esta_tocando == True:
            if toca(guitar) == False:
                esta_tocando = False
        else:
            if toca(guitar) == True:
                esta_tocando = True


        
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                quit()
            if event.type==KEYDOWN:
                     if event.key==pg.K_s:
                            pg.quit()
                            game=False   
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
        sboard = pg.image.load('assets/images/scoreboard.png')
        sboardDim = [470, 150]
        sboard = pg.transform.scale(sboard, (sboardDim[0],sboardDim[1]))
        textorect=marcador.get_rect()

        textorect.center=(width / 2 ),(85)
        
        screen.blit(sboard, (width / 2 - sboardDim[0] / 2,20))
        screen.blit(marcador,textorect)
        
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
                   marcador=    font.render(str(puntaje.puntuacion_actual()),100,(44, 62, 80))
                   puntaje.cambiar_puntuacion(-10)
                  
                tipos = [ 'AZU','VER', 'ROJ', 'AMA']
                if get_color_type() != None:
                    
                    #print('El valor de la nota es %f - %f' % (nota.type, get_color_type()))
                    type_temp = round(get_color_type(),2) 
                else: 
                    type_temp = -1
                if abs(nota.pos[1] - selectores[nota.type].pos[1]) <= 20 and type_temp == round(nota.type,2): 
                   notas.remove(nota)
                   puntaje.cambiar_puntuacion(15)
                   #se define el marcador para que lo renderize y se pueda imprimir como un valor
                   marcador=        font.render(str(puntaje.puntuacion_actual()),100,(44, 62, 80)) 
                   print('Excelente - ' + str(puntaj))
                   puntaj += 1
              #imprime el mensaje de la pantalla     
               
        if count % TIEMPO_APARICION == 0:
            #LANZA LAS NOTAS con el objeto definido en notas.py 
            notas.append(lanzar_nota())
        count += 1
        pg.display.flip()
    #nos da como los fps del juego
    reloj.tick(500)
    #HACE UN UPDATE A LA PANTALLA
    sboard = pg.image.load(os.getcwd() + '/assets/images/' + 'scoreboard' + '.png')
    pg.display.update()


if '__main__' == __name__: 
    primsipal()
    