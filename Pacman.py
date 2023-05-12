"""Actividad 3: Pacman"""

from random import choice #importamos choice de random
from turtle import * #Importamos turtle
from freegames import floor, vector #importamos vector y floor de freegames

# Creamos un diccionario llamado state con una llave score cuyo valor inicial es 0.
state = {'score': 0}

# Creamos una tortuga invisible llamada path para que dibuje el camino que seguirán los fantasmas.
path = Turtle(visible=False)

# Creamos una tortuga invisible llamada writer para que escriba el puntaje del jugador.
writer = Turtle(visible=False)

# Creamos un vector llamado aim que determina la dirección hacia la que se mueve Pac-Man inicialmente.
aim = vector(5, 0)

# Creamos un vector llamado pacman que determina la posición inicial de Pac-Man en el juego.
pacman = vector(-40, -80)

# Creamos una lista llamada ghosts que contiene cuatro listas, cada una con dos vectores: el primer vector determina la posición inicial del fantasma y el segundo vector determina la dirección hacia la que se mueve inicialmente.
ghosts = [
    [vector(-180, 160), vector(10, 0)],
    [vector(-180, -160), vector(0, 10)],
    [vector(100, 160), vector(0, -10)],
    [vector(100, -160), vector(-10, 0)],
]

# Creamos una lista llamada tiles que representa el mapa del juego, donde 0 indica una casilla vacía y 1 indica una casilla con un punto.
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

def square(x, y):
    """Función que dibuja square usando path en (x, y)"""
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

def offset(point):
    """Función que regresa offset de un point en los tiles"""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

def valid(point):
    """Función que regresa True si point es válido en los tiles"""
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0

def world():
    """Función que dibuja el mundo usando path."""
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')

def move():
    """Función que mueve el pacman y todos los fantasmas."""
    writer.undo()
    writer.write(state['score'])

    clear()

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')


    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            dx, dy = pacman.x - point.x, pacman.y - point.y
            optionsx = [
                vector(10, 0),
                vector(-10, 0),
            ]
            optionsy = [
                vector(0, 10),
                vector(0, -10),
            ]
            if abs(dx)>abs(dy):
                plan = choice(optionsx)
            else:
                plan = choice(optionsy)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 100)

def change(x, y):
    """Función que cambia el aim del pacman si es posible."""
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y


setup(420, 420, 370, 0) # Configuración inicial de la pantalla
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
# Se definen las teclas para cambiar la dirección del pacman
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
#se inicia el mundo 
world()
# Se inicia el movimiento del pacman y los fantasmas
move()
done()