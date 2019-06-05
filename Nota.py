
import pygame 
import sys, os 
import random

COLORES = ['amarilla','roja','verde', 'azul'] # Lista de colores
type_ = [pygame.K_a, pygame.K_s, pygame.K_j, pygame.K_k] #  Identificadores de teclas tipo pygame
INICIAL_VERTICAL = 180 

# TODO: Convertir el objeto a un sprite de pygame 

class Nota(pygame.sprite.Sprite):
    '''
        CLASE_ Nota. Encargada de generar las notas del juego.
    '''
    def __init__(self, color, pos_inicio):
       """
        Claves de Color: 
        0 -> amarillo
        1 -> rojo
        2 -> verde
        3 -> azul
       """
       pygame.sprite.Sprite.__init__(self)
       # Definicion de Variables
       self.height = 70 
       self.type = color # El identificador de color se guarda como tipo de nota, para mejorar lectura  
       self.ratio = 45 / 70 # Razón entre la altura y el ancho
       self.factor = 1.1 # Factor de escala de transformación. 
       self.pos = [pos_inicio,INICIAL_VERTICAL]
       self.vel = random.randint(10,15) / 10 # Pixeles por frame
       self.fuente_imagen = pygame.image.load(os.path.join('assets/notas', 'nota_' + COLORES[color] + '.png')) 
       self.dimensions = (int(self.height),int(self.ratio * self.height)) 
       self.image = pygame.transform.scale(self.fuente_imagen, self.dimensions)



    def show(self, screen): 
        '''
        Muestra la nota dentro de la superficies dada
        screen: Superficie (Pygame)
        '''
        self.image =  pygame.transform.scale(self.fuente_imagen,[int(x * self.factor) for x in self.dimensions])
        screen.blit(self.image, (self.pos[0], self.pos[1]))

    def move(self): 
        '''
        Genera el movimiento de la nota
        '''
        self.pos[1] += self.vel

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

