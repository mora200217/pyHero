import pygame 
import sys, os 

#from pygame import math.Vector2 as Vector2

COLORES = ['amarilla','roja','verde', 'azul']

INICIAL_VERTICAL = 100 

# TODO: Convertir el objeto a un sprite de pygame 

class Nota(pygame.sprite.Sprite):
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
       self.ratio = 45 / 70
       self.factor = 1.1
       self.pos = [pos_inicio,INICIAL_VERTICAL] # Posicion inicial 
       self.vel = 0.6 # Pixeles por frame 
       self.fuente_imagen = pygame.image.load(os.path.join('assets/notas', 'nota_' + COLORES[color] + '.png')) # Importar imagen 
       self.dimensions = (int(self.height),int(self.ratio * self.height))
       self.image = pygame.transform.scale(self.fuente_imagen, self.dimensions)



    def show(self, screen): 
        
        self.image =  pygame.transform.scale(self.fuente_imagen,[int(x * self.factor) for x in self.dimensions])
        screen.blit(self.image, (self.pos[0], self.pos[1]))

    def move(self): 
        self.pos[1] += self.vel

    def destroy(self): 
        pass

