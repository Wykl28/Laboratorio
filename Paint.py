"""Actividad 1: Paint"""

from turtle import * #Importamos turtle
from freegames import vector #importamos vector de freegames

"""Funcion que dibuja la linea"""
def line(start, end):
    """Draw line from start to end."""
    up() #Levantamos la tortuga
    goto(start.x, start.y) #Es el punto del que comienza la linea
    down() #Bajamos la tortuga
    goto(end.x, end.y) #Es el punto en el que termina la linea 

"""Funcion que dibuja el cuadrado"""
def square(start, end):
    """Draw square from start to end."""
    up() #Levantamos la tortuga
    goto(start.x, start.y) #Es el punto en el que comienza
    down() #Bajamos la tortuga
    begin_fill() #comenzamos a rellenar la figura

    """Ciclo for que dibuja el cuadrado"""
    for count in range(4):
        forward(end.x - start.x) #Para avanzar la distancia de los lados del cuadrado
        left(90) #Gira 90 grados a la izquierda

    end_fill() #terminamos de rellenar la figura

"""Funcion que dibuja el circulo"""
def cir(start, end):
    """Draw circle from start to end."""
    #t = turtle.Turtle()
    up() #Levantamos la tortuga
    goto(start.x, start.y) #Es el punto en el que comienza
    down() #Bajamos la tortuga
    begin_fill() #comenzamos a rellenar la figura
    r = (end.x-start.x) #calculamos el radio que va a tener el circulo
    circle(r) #Dibuja el circulo utilizando el radio ya calculado
    end_fill() #terminamos de rellenar la figura

"""Funcion que dibuja el rectangulo"""
def rectangle(start, end):
    """Draw rectangle from start to end."""
    up() #Levantamos la tortuga
    goto(start.x, start.y) #Es el punto en el que comienza
    down() #Bajamos la tortuga
    begin_fill() #comenzamos a rellenar la figura
    """Ciclo for que dibuja el rectangulo"""
    for count in range(2):
        forward(end.x - start.x) #Para avanzar la distancia de las lineas horizontales
        left(90) #Gira 90 grados a la izquierda
        forward(end.y - start.y) #Para avanzar la distancia de las lineas verticales
        left(90) #Gira 90 grados a la izquierda
    end_fill() #terminamos de rellenar la figura

"""Funcion que dibuja el triangulo"""
def triangle(start, end):
    """Draw triangle from start to end."""
    up() #Levantamos la tortuga
    goto(start.x, start.y) #Es el punto en el que comienza
    down() #Bajamos la tortuga
    begin_fill() #comenzamos a rellenar la figura
    """Ciclo for que dibuja el triangulo"""
    for i in range(3):
        forward(end.x - start.x) #Para avanzar la distancia de los lados del cuadrado
        left(120) #Gira 120 grados a la izquierda
    end_fill() #terminamos de rellenar la figura

"""Funcion que agarra las coordenadas x e y"""
def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

"""Funcion almacena todo"""
def store(key, value):
    """Store value in state at key."""
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
onkey(lambda: store('shape', line), 'l') #Linea con tecla l
onkey(lambda: store('shape', square), 's') #Cuadrado con tecla s
onkey(lambda: store('shape', cir), 'c') #Circulo con tecla c
onkey(lambda: store('shape', rectangle), 'r') #Rectangulo con tecla r
onkey(lambda: store('shape', triangle), 't') #Triangulo con tecla t
done()