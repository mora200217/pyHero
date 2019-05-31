import pygame

pygame.init()

window = pygame.display.set_mode((400,400))

pygame.display.set_caption("Nick el guitarrista")

white = (255,255,255)

clock = pygame.time.Clock()


# Nick sprites
m1 = pygame.image.load("nick/pixil-frame-1.png")
m2 = pygame.image.load("nick/pixil-frame-2.png")
m3 = pygame.image.load("nick/pixil-frame-3.png")
m4 = pygame.image.load("nick/pixil-frame-4.png")
m5 = pygame.image.load("nick/pixil-frame-5.png")
m6 = pygame.image.load("nick/pixil-frame-6.png")
m7 = pygame.image.load("nick/pixil-frame-7.png")


marioCurrentImage = 1

gameLoop=True
while gameLoop:

    for event in pygame.event.get():

        if (event.type==pygame.QUIT):

            gameLoop=False

    window.fill(white)

    if (marioCurrentImage==1):

        window.blit(m1, (10,10))


    if (marioCurrentImage==2):

        window.blit(m2, (10,10))
    
    if (marioCurrentImage==3):

        window.blit(m3, (10,10))

    if (marioCurrentImage==4):

        window.blit(m4, (10,10))
    
    if (marioCurrentImage==5):

        window.blit(m5, (10,10))

    if (marioCurrentImage==6):

        window.blit(m6, (10,10))
    
    if (marioCurrentImage==7):

        window.blit(m7, (10,10))



    if (marioCurrentImage==8):

        marioCurrentImage=1

    else:

        marioCurrentImage+=1;
    
    pygame.display.flip()

    clock.tick(20)

pygame.quit()
