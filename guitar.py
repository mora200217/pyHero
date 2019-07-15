'''
Grupo de funciones para reconocimiento de eventos de guitarra
'''
# Lista de valores para depuración 
# tipos = [ 'AZU','VER', 'ROJ', 'AMA']

'''
Regresa si se mueve el hat
guitar: Objeto Joystick para extraer el hat
'''
def toca(guitar):
    if abs(guitar.get_hat(0)[1]) == 1 :
        return True
    return False

'''
Regresa el valor del boton que se usa
guitar: Objeto Joystick para extraer el hat
'''
def get_color(guitar):
    toca = False
    if abs(guitar.get_hat(0)[1]) == 1:
        toca = True
    for tipo in range(5):
        but = guitar.get_button(tipo) # Declarar el button por tipo
        if but == 1: # Verificar si esta siendo presionado
            '''
            Condicionales para conversión de tipos 
            y Solucionar los cambios de posición y color
            entre guitarra y aplicación
            '''
            if tipo == 0:
                return 3
            if tipo == 1:
                return 0
            if tipo == 2:
                return 1
            if tipo == 3:
                return 2

    return None # En caso de no oprimir ningun boton

    