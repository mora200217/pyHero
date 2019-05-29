import pygame 
import sys, os 

from pygame.math import Vector2

COLORES = ['amarilla','roja','verde', 'azul']
# TODO: Convertir el objeto a un sprite de pygame 

class Nota(pygame.sprite.Sprite):
    def __init__(self, color, initial_pos):
       """
        Claves de Color: 
        0 -> amarillo
        1 -> rojo
        2 -> verde
        3 -> azul
       """
       pygame.sprite.Sprite.__init__(self)
       # Definicion de Variables
       self.pos = Vector2(initial_pos[0],initial_pos[1]) # Posicion inicial 
       self.vel = 0.6 # Pixeles por frame 
       self.image =  pygame.image.load(os.path.join('assets/notas', 'nota_' + COLORES[color] + '.png')) # Importar imagen 
       self.rect = self.image.get_rect()

    def show(self, screen): 
        screen.blit(self.image, (self.pos[0], self.pos[1]))

    def move(self): 
        self.pos[1] += self.vel

    def destroy(self): 
        pass

