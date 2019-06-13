import pygame as pg 
import sys, os 

#define los colores como constantes
COLORES = ['amarillo','rojo','verde', 'azul']

#definimos el objero
class Selector(pg.sprite.Sprite):
    #caracteristicadel objeto 1
    def __init__(self, color, width, height, division): 
        self.color = color
        self.pos = [(145 + division *  color), height - 70]
        self.passive = pg.image.load('assets/selectores/selector-' + COLORES[color]+ '.png')
    #caracteristica del objeto 2
    def show(self, screen): 
        self.passive = pg.transform.scale(self.passive, [80,50])
        screen.blit(self.passive, (self.pos[0], self.pos[1]))
    #carcteristica del objeto 3
    def get_pos(self, offset = 0):
        return [self.pos[0] + 40, self.pos[1] + 25]     