import pygame as pg 
import sys, os 


COLORES = ['amarillo','rojo','verde', 'azul']


class Selector(pg.sprite.Sprite):
    def __init__(self, color): 
        print('New Selector')
        div  = 107
        self.color = color
        self.pos = [(145 + div *  color), 450]
        self.passive = pg.image.load('assets/selectores/selector-' + COLORES[color]+ '.png')
    
    def show(self, screen): 
        self.passive = pg.transform.scale(self.passive, [80,50])
        screen.blit(self.passive, (self.pos[0], self.pos[1]))