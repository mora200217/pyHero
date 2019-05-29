import pygame
pygame.init()
reloj = pygame.time.Clock()
 #definen los aspectos del juego como pantalla
pantalla = pygame.display.set_mode((470,300),0,32)
pygame.display.set_caption("pruebas musica")
class musica:
    def __init__(self):
        pygame.mixer.music.load("Pastor Lopez - El hijo ausente.mp3")
    def reproducir(self,opcion):
        while opcion ==1:
            pygame.mixer.music.play(1)
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

        reloj.tick(20)

        pygame.display.update()
        
    
musica = musica()
musica.reproducir(1) 

#actualiza la pantalla
