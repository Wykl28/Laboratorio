"""Actividad 1: Paint"""

from turtle import * #Importamos turtle
from freegames import vector #importamos vector de freegames

def line(start, end):
    """Función que dibuja la línea"""
    up() #Levantamos la tortuga
    goto(start.x, start.y) #Es el punto del que comienza la línea
    down() #Bajamos la tortuga
    goto(end.x, end.y) #Es el punto en el que termina la línea 

def square(start, end):
    """Función que dibuja el cuadrado"""
    up() #Levantamos la tortuga
    goto(start.x, start.y) #Es el punto en el que comienza
    down() #Bajamos la tortuga
    begin_fill() #comenzamos a rellenar la figura

    """Ciclo for que dibuja el cuadrado"""
    for count in range(4):
        forward(end.x - start.x) #Para avanzar la distancia de los lados del cuadrado
        left(90) #Gira 90 grados a la izquierda

    end_fill() #terminamos de rellenar la figura

def cir(start, end):
    """Función que dibuja el círculo"""
    up() #Levantamos la tortuga
    goto(start.x, start.y) #Es el punto en el que comienza
    down() #Bajamos la tortuga
    begin_fill() #comenzamos a rellenar la figura
    r = (end.x-start.x) #calculamos el radio que va a tener el círculo
    circle(r) #Dibuja el círculo utilizando el radio ya calculado
    end_fill() #terminamos de rellenar la figura

def rectangle(start, end):
    """Función que dibuja el rectángulo"""
    up() #Levantamos la tortuga
    goto(start.x, start.y) #Es el punto en el que comienza
    down() #Bajamos la tortuga
    begin_fill() #comenzamos a rellenar la figura
    """Ciclo for que dibuja el rectángulo"""
    for count in range(2):
        forward(end.x - start.x) #Para avanzar la distancia de las líneas horizontales
        left(90) #Gira 90 grados a la izquierda
        forward(end.y - start.y) #Para avanzar la distancia de las líneas verticales
        left(90) #Gira 90 grados a la izquierda
    end_fill() #terminamos de rellenar la figura

def triangle(start, end):
    """Funcion que dibuja el triángulo"""
    up() #Levantamos la tortuga
    goto(start.x, start.y) #Es el punto en el que comienza
    down() #Bajamos la tortuga
    begin_fill() #comenzamos a rellenar la figura
    """Ciclo for que dibuja el triángulo"""
    for i in range(3):
        forward(end.x - start.x) #Para avanzar la distancia de los lados del cuadrado
        left(120) #Gira 120 grados a la izquierda
    end_fill() #terminamos de rellenar la figura

def tap(x, y):
    """Funcion que agarra las coordenadas x e y"""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    """Funcion almacena todo"""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
"""Colores con sus respectivas teclas"""
onkey(lambda: color('black'), 'K') #Color negro con la tecla K
onkey(lambda: color('white'), 'W') #Color blanco con la tecla W
onkey(lambda: color('green'), 'G') #Color verde con la tecla G
onkey(lambda: color('blue'), 'B') #Color azul con la tecla B
onkey(lambda: color('red'), 'R') #Color rojo con la tecla R
onkey(lambda: color('magenta'), 'M') #Color magenta con la tecla M
"""Figuras con sus respectivas teclas"""
onkey(lambda: store('shape', line), 'l') #Línea con tecla l
onkey(lambda: store('shape', square), 's') #Cuadrado con tecla s
onkey(lambda: store('shape', cir), 'c') #Círculo con tecla c
onkey(lambda: store('shape', rectangle), 'r') #Rectángulo con tecla r
onkey(lambda: store('shape', triangle), 't') #Triángulo con tecla t
done()