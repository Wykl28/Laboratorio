"""Actividad 2: Snake"""

from turtle import * #Importamos turtle
from random import choice, randrange #importamos choice y randrange de random
from freegames import square, vector #importamos vector y square de freegames

food = vector(0, 0) #definimos la posición inicial de la comida
snake = [vector(10, 0)] #definimos la posición inicial de la serpiente
aim = vector(0, -10) #definimos el vector a donde apunta inicialmente la serpiente

"""Colores aleatorios sin repetirse"""
colors = ['black', 'cyan', 'magenta', 'yellow', 'green']#definimos los colores
rand_colors_1 = choice(colors) #escoge un color al azar para el cuerpo de la serpiente
colors.remove(rand_colors_1)#quita el color que escogió antes para que no se repitan los colores de la comida y la serpiente
rand_colors_2 = choice(colors)#escoge un color al azar de los restantes para la comida

"""Función que cambia la dirección de la serpiente"""
def change(x, y):
    aim.x = x
    aim.y = y

"""Función que checa si la cabeza de la serpiente está dentro de los límites"""
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

"""Función que mueve la comida aleatoriamente por la pantalla"""
def move_food():
    #espacio donde se mueve constantemente la comida
    food.x += randrange(-1, 2, 1) * 10
    food.y += randrange(-1, 2, 1) * 10

    if not inside(food):
        food.x = 0
        food.y = 0

    ontimer(move_food, 100) # Se llama a la función move_food cada 100 milisegundos

"""Función que mueve la serpiente hacia adelante"""
def move():
    # Se crea una copia de la cabeza de la serpiente
    head = snake[-1].copy()
    # Se mueve la cabeza de la serpiente en la dirección definida anteriormente por "aim"
    head.move(aim)

    # Si la cabeza está fuera de los límites o choca con el cuerpo de la serpiente, el juego se acaba
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    # Si la cabeza de la serpiente está en la posición de la comida, se come la comida y se crea otra comida
    if head == food:
        print('Snake:', len(snake))
        move_food()
    # Si no hay comida, se mueve la serpiente y se quita la última sección del cuerpo de la misma 
    else:
        snake.pop(0)

    # Se limpia la pantalla y se dibuja la serpiente y la comida en sus nuevas posiciones
    clear()

    for body in snake:
        square(body.x, body.y, 9, rand_colors_1)

    square(food.x, food.y, 9, rand_colors_2)
    update()
    ontimer(move, 100) # Se llama a la función move cada 100 milisegundos


setup(420, 420, 370, 0) # Configuración inicial de la pantalla
hideturtle()
tracer(False)
# Se definen las teclas para cambiar la dirección de la serpiente
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
# Se inicia el movimiento de la comida y la serpiente
move_food()
move()

done()