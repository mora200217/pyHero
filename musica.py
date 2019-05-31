import pygame
from pygame.locals import *
 
pygame.init()
 #definen los aspectos del juego como pantalla
pantalla = pygame.display.set_mode((470,300),0,32)
pygame.display.set_caption("pruebas musica")
 
reloj = pygame.time.Clock()
 #se importa la cancion que tienen que estar dentro de la carpeta
pygame.mixer.music.load("Pastor Lopez - El hijo ausente.mp3")
#se comienza a reproducir indefinidamente
pygame.mixer.music.play(1)
#el ciclo que es infinito hasta que se pause la cancion
while True:
    for eventos in pygame.event.get():
        #quita la cancion cuando uno cierrra el jego
        if eventos.type == pygame.QUIT:
            exit()
            #evalua si hay una tecla precionada
        if eventos.type == pygame.KEYDOWN:
            #evalua si la tecla presionada es la p de pausar
            if eventos.key == pygame.K_p:
                #pausa la musica
                pygame.mixer.music.stop()
#da el frame count practicamente pero es en py game
    reloj.tick(20)
#actualiza la pantalla
    pygame.display.update()


