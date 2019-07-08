import pygame,sys
from pygame.locals import *

#variables globales
colorf=(0,0,0)
anchopantalla=640
altopantalla=426
py=75#posicion en y del titulo
cansionxdificultad=[None,None]#la primera posicion es el numero de la cancion y la segunda un caracter con el nombre de la dificultad
numcanciones=3

'''-----Variables para diseño de buttons del menu primsipal-----'''

dimensiones=[220,55]
pxb1=anchopantalla/2-dimensiones[0]/2#posicion en x bloque 1
db1t=150#distancia al titulo en eje y al primer bloque
pyb1=py+db1t-(dimensiones[1]/2)#posicion en y bloque 1
posicionb1=[pxb1,pyb1]
dif=10#espacio entre bloques
pyb2=pyb1+dimensiones[1]+dif#posicion en y bloque 2
posicionb2=[pxb1,pyb2]
'''buttons dificultad'''
posicionb3=[pxb1,pyb2+dif+dimensiones[1]]#posicion button dificil
colorb1=[50,50,51]#color bloques
'''Buttons creditos'''
pybr=altopantalla-30-dimensiones[1]
pbregresar=[pxb1,pybr]#posicion del boton regresar que lleva a primsipal
'''Buttons regresar para el frame canciones y el frame dificultad'''
dimensionesbrg=[anchopantalla,55]
pxbrg=0#pocision en x button general para regresar
pybrg=altopantalla-dimensiones[1]#pocision en y button general para regresar
posicionbrg=[pxbrg,pybrg]
#-------------------------------------------------------------------

#objetos
#se inicicaliza
pygame.init()
ventana=pygame.display.set_mode((anchopantalla,altopantalla))
pygame.display.set_caption("Chaparro Hero")
fondo=pygame.image.load("fondo.jpg").convert_alpha()
fondo_creditos=pygame.image.load("fondo_creditos.jpg").convert_alpha()
'''sonido aplausos en main al seleccioanr a jugar'''
'''Fuentes'''
fuentetitulo=pygame.font.SysFont("Nightmare_Hero_Normal",75)
fuenteopciones=pygame.font.SysFont("comicsansms",25,True)
fuentecanciones=pygame.font.SysFont("comicsansms",20,True)
fuentecreditos=pygame.font.SysFont("comicsansms",20,True)
#-------------------------------------------------------------------

#funciones

def escribir(msg,color,posx,posy,fuent):
        mitexto=fuent.render(msg,True,color)
        textorect=mitexto.get_rect()
        textorect.center=(posx),(posy)
        ventana.blit(mitexto,textorect)

def esta_en_boton(pos,ancho,largo):
        mousex,mousey=pygame.mouse.get_pos()
        esta=False
        if pos[0]+ancho>=mousex>=pos[0] and pos[1]+largo>=mousey>=pos[1]:
                esta=True
        return esta         

def boton(Nombre,superficie,posicionesboton,ancho,largo,colorb,colortexto,fuente,dondeesta):
        if colorb==(0,0,0):
                colorestab=(224,224,224)
                colorestatexto=(0,0,0)
        if colorb==(254,254,254):
                colorestab=(0,0,0)
                colorestatexto=(254,254,254)
        if esta_en_boton(posicionesboton,ancho,largo)==False:
                pygame.draw.rect(superficie,colorb,(posicionesboton[0],posicionesboton[1],ancho,largo))
                escribir(Nombre,colortexto,(posicionesboton[0]+ancho/2),(posicionesboton[1]+largo/2),fuente)
        else:
                pygame.draw.rect(superficie,colorestab,(posicionesboton[0],posicionesboton[1],ancho,largo))
                escribir(Nombre,colorestatexto,(posicionesboton[0]+ancho/2),(posicionesboton[1]+largo/2),fuente)
                for event in pygame.event.get():
                        if dondeesta=="main":
                                if Nombre=="¡A jugar!" and event.type==pygame.MOUSEBUTTONDOWN:
                                        canciones()
                                elif Nombre=="Creditos" and event.type==pygame.MOUSEBUTTONDOWN:
                                        creditos() 

                        elif dondeesta=="creditos":
                                if Nombre=="Regresar" and event.type==pygame.MOUSEBUTTONDOWN:
                                        primsipal()   

                        elif dondeesta=="canciones":
                                if Nombre=="Cancion1" and event.type==pygame.MOUSEBUTTONDOWN:
                                        cansionxdificultad[0]=1
                                        dificultad()  
                                if Nombre=="Cancion2" and event.type==pygame.MOUSEBUTTONDOWN:
                                        cansionxdificultad[0]=2
                                        dificultad()  
                                if Nombre=="Cancion3" and event.type==pygame.MOUSEBUTTONDOWN:
                                        cansionxdificultad[0]=3
                                        dificultad()
                                if Nombre=="Regresar" and event.type==pygame.MOUSEBUTTONDOWN:
                                        primsipal() 

                        elif dondeesta=="dificultad":
                                if Nombre=="Facil" and event.type==pygame.MOUSEBUTTONDOWN:
                                        cansionxdificultad[1]=Nombre
                                        ciclodeljuego()#aca se debe poner aquello que me lleva al comienzo del juego
                                if Nombre=="Medio" and event.type==pygame.MOUSEBUTTONDOWN:
                                        cansionxdificultad[1]=Nombre
                                        ciclodeljuego()
                                if Nombre=="Dificil" and event.type==pygame.MOUSEBUTTONDOWN:
                                        cansionxdificultad[1]=Nombre
                                        ciclodeljuego()   
                                if Nombre=="Regresar" and event.type==pygame.MOUSEBUTTONDOWN:
                                        canciones()  

                        elif dondeesta=="ciclodeljuego":
                                if Nombre=="Regresar" and event.type==pygame.MOUSEBUTTONDOWN:
                                        dificultad()                                                                  

def primsipal():
    pygame.mixer.music.pause()    
    pygame.mixer.music.load("musicamp.mp3")
    pygame.mixer.music.play(2,1) 
    intro=True  
    while intro:
        ventana.fill(colorf)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==KEYDOWN:
                    if event.key==pygame.K_s:
                            pygame.quit()
                            intro=False                                                                  
        ventana.blit(fondo,(0,0))
        escribir("Chaparro Hero",(254,254,254),anchopantalla/2,py,fuentetitulo)
        '''Botones'''
        boton("¡A jugar!",ventana,posicionb1,dimensiones[0],dimensiones[1],(0,0,0),(254,254,254),fuenteopciones,"main")
        boton("Creditos",ventana,posicionb2,dimensiones[0],dimensiones[1],(0,0,0),(254,254,254),fuenteopciones,"main")
        pygame.display.update() 

def canciones():
        pygame.mixer.music.pause() 
        pxbc=20#posicion en x del primer boton de la cancion1
        pybc=py+60#posicion en y del primer boton de la cancion1
        dimensionesbc=[200,55]   
        sep=20#separacion entre button de canciones verticalmente
        continuar=True    
        while continuar:
                ventana.fill(colorf)
                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                                pygame.quit()
                                quit() 
                        if event.type==KEYDOWN:
                                if event.key==pygame.K_s:
                                        pygame.quit()
                                        continuar=False       
                ventana.blit(fondo,(0,0))
                escribir("¡Elige tu cancion!",(254,254,254),anchopantalla/2,py,fuentetitulo)
                for i in range(0,3):
                        boton("Cancion"+str(i+1),ventana,[pxbc,pybc+sep*i+dimensionesbc[1]*i],dimensionesbc[0],dimensionesbc[1],(254,254,254),(0,0,0),fuenteopciones,"canciones")
                boton("Regresar",ventana,posicionbrg,dimensionesbrg[0],dimensionesbrg[1],(0,0,0),(254,254,254),fuenteopciones,"canciones")
                pygame.display.update()   

def dificultad():
        pxb1=anchopantalla/2-dimensiones[0]/2#posicion en x bloque 1
        '''variable que se debe cambiar para subir todos los button o bajarlos teniendo como referencia al tituulo
        bb1t'''
        db1t=110#distancia del boton 1 al titulo
        pyb1=py+db1t-(dimensiones[1]/2)#posicion en y bloque 1
        posicionb1=[pxb1,pyb1]
        dif=10#espacio entre bloques
        pyb2=pyb1+dimensiones[1]+dif#posicion en y bloque 2
        posicionb2=[pxb1,pyb2]
        '''buttons dificultad'''
        posicionb3=[pxb1,pyb2+dif+dimensiones[1]]#posicion button dificil
        posicionb1d=posicionb1[:]
        posicionb1d[1]=posicionb1[1]-50
        anchobd=250#ancho en generañl de los botones para dificultad
        largobd=55#largo en generañl de los botones para dificultad
        intro=True  
        pbrx=anchopantalla-5-dimensiones[0]
        pbry=altopantalla-20-dimensiones[1]   
        while intro:
                ventana.fill(colorf)
                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                                pygame.quit()
                                quit()
                        if event.type==KEYDOWN:
                                if event.key==pygame.K_s:
                                        pygame.quit()
                                        intro=False                                                                  
                ventana.blit(fondo,(0,0))
                escribir("Selecciona Dificultad",(254,254,254),anchopantalla/2,py,fuentetitulo)
                '''Botones'''
                boton("Facil",ventana,posicionb1,anchobd,largobd,(0,0,0),(254,254,254),fuenteopciones,"dificultad")
                boton("Medio",ventana,posicionb2,anchobd,largobd,(0,0,0),(254,254,254),fuenteopciones,"dificultad")
                boton("Dificil",ventana,posicionb3,anchobd,largobd,(0,0,0),(254,254,254),fuenteopciones,"dificultad")
                boton("Regresar",ventana,posicionbrg,dimensionesbrg[0],dimensionesbrg[1],(0,0,0),(254,254,254),fuenteopciones,"dificultad")                
                pygame.display.update()        

def creditos():
    pygame.mixer.music.play() 
    pygame.mixer.music.load("music creditos.mp3")
    pygame.mixer.music.play() 
    integrantes_del_grupo=["Andres Morales","Ivan Hernandez","Juan Ramirez","Leider Rozo","Depronto Laura aun no se sabe xd"]
    sep=35
    st=56#separacion que tiene la posicion en y desde el titulo del primer integrante del grupo
    continuar=True    
    while continuar:
        ventana.fill(colorf)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==KEYDOWN:
                     if event.key==pygame.K_s:
                            pygame.quit()
                            continuar=False   
        ventana.blit(fondo_creditos,(0,0))                    
        escribir("Creditos",(254,254,254),anchopantalla/2,py+10,fuentetitulo)
        for i in range(0,len(integrantes_del_grupo)):
                escribir(integrantes_del_grupo[i],(254,254,254),anchopantalla/2,py+st+sep*(i+1),fuentecreditos)
        boton("Regresar",ventana,pbregresar,dimensiones[0],dimensiones[1],(0,0,0),(254,254,254),fuenteopciones,"creditos")
        pygame.display.update()       

def ciclodeljuego():#esto representa el comienzo del juego
    pbrx=anchopantalla-5-dimensiones[0]
    pbry=altopantalla-20-dimensiones[1]    
    continuar=True    
    while continuar:
        ventana.fill(colorf)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==KEYDOWN:
                     if event.key==pygame.K_s:
                            pygame.quit()
                            continuar=False   
        ventana.blit(fondo,(0,0))
        escribir("Ciclo del juego",(254,254,254),anchopantalla/2,py,fuentetitulo)
        escribir(str(cansionxdificultad),(254,254,254),anchopantalla/2,py+150,fuenteopciones)
        boton("Regresar",ventana,(pbrx,pbry),dimensiones[0]-30,dimensiones[1],(0,0,0),(254,254,254),fuenteopciones,"ciclodeljuego")
        pygame.display.update()                        
#-------------------------------------------------------------------
#main
primsipal()