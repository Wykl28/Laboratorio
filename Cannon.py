"""Actividad 4: Cannon"""

from random import randrange #importamos randrange de random
from turtle import * #impotamos turtle

from freegames import vector #importamos vector de freegames

# Se crean las variables globales
ball = vector(-200, -200) # Posición inicial de la pelota
speed = vector(0, 0) # Velocidad inicial de la pelota
targets = [] # Lista vacía de objetivos

"""Funcion para responder al tap"""
def tap(x, y):
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 16
        speed.y = (y + 200) / 16

"""Función que determina si un punto está dentro de la pantalla"""
def inside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200

"""Funcion para dibujar la pelota y los objetivos"""
def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        # Se dibujan los objetivos como puntos azules
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        # Si la pelota está dentro de la pantalla, la dibuja como un punto rojo
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

"""Función para mover la pelota y los objetivos"""
def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        # Cada cierto tiempo se agrega un nuevo objetivo
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Modificación para reposicionar los objetivos que se salen de la pantalla
    for target in targets:
        if not inside(target):
            # Si el objetivo está fuera de la pantalla, se lo reposiciona del otro lado
            target.x = 200
            target.y = randrange(-150, 150)
        target.x -= 1.5

    if inside(ball):
        # Si la pelota está dentro de la pantalla, se actualiza su velocidad y posición
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    # Se eliminan los objetivos que hayan sido impactados por la pelota
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    # Se llama a la función para dibujar la pelota y los objetivos
    draw()

    # Se llama a la función move de nuevo después de un breve tiempo
    ontimer(move, 50)

# Configuración de la pantalla
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)

# Se llama a la función tap cuando se hace clic en la pantalla
onscreenclick(tap)

# Se llama a la función move para iniciar el movimiento de la pelota y los objetivos
move()
done()