
import pygame as pg
import sys, os 
import random
from pygame.math import Vector2 as Vector

COLORES = ['amarilla','roja','verde', 'azul'] # Lista de colores
type_ = [pg.K_a, pg.K_s, pg.K_j, pg.K_k] #  Identificadores de teclas tipo pg
INICIAL_VERTICAL = 180 # Posición 

# TODO: Convertir el objeto a un sprite de pg 

class Nota():
    '''
        CLASE_ Nota. Encargada de generar las notas del juego.
    '''
    def __init__(self, color, pos_inicio, width, height, division):
       """
        Claves de Color: 
        0 -> amarillo
        1 -> rojo
        2 -> verde
        3 -> azul
       """

       # Definicion de Variables
       self.height = 70 
       self.type = color # El identificador de color se guarda como tipo de nota, para mejorar lectura  
       self.ratio = 45 / 70 # Razón entre la altura y el ancho
       self.factor = 1.1 # Factor de escala de transformación. 
       self.pos = Vector(pos_inicio, INICIAL_VERTICAL)
       # self.pos = [pos_inicio,INICIAL_VERTICAL]
       
       self.temp_f = Vector((145 + division *  color), height - 70)
       self.temp_i = Vector(pos_inicio, INICIAL_VERTICAL)
       
       self.vel  =(self.temp_f - self.temp_i).normalize()
       self.fuente_imagen = pg.image.load(os.path.join('assets/notas', 'nota_' + COLORES[color] + '.png')) 
       self.dimensions = (int(self.height),int(self.ratio * self.height)) 
       self.image = pg.transform.scale(self.fuente_imagen, self.dimensions)



    def show(self, screen): 
        '''
        Muestra la nota dentro de la superficies dada
        screen: Superficie (pg)
        '''
        self.image =  pg.transform.scale(self.fuente_imagen,[int(x * self.factor) for x in self.dimensions])
        screen.blit(self.image, (self.pos.x, self.pos.y))

    def move(self): 
        '''
        Genera el movimiento de la nota
        '''
        self.pos +=  self.vel

    def get_type(self):
        '''
        Devuelve el tipo de nota desde 0 a 3 
        para definir el color y demás atributos
        '''
        return type_[self.type]

    def destroy(self):
        '''
        Destruye la nota
        '''
        del self


