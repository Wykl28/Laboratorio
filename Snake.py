"""Actividad 2: Sanke"""

from turtle import * #importamos turtle
from random import choice, randrange #importamos randrange
from freegames import square, vector #importamos square y vector de freegames

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Colores aleatorios sin repetirse
colors = ['black', 'cyan', 'magenta', 'yellow', 'green']
rand_colors_1 = choice(colors)
colors.remove(rand_colors_1)
rand_colors_2 = choice(colors)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move_food():
    """Move food location randomly."""
    food.x += randrange(-1, 2, 1) * 10
    food.y += randrange(-1, 2, 1) * 10

    if not inside(food):
        food.x = 0
        food.y = 0

    ontimer(move_food, 100)


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        move_food()
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, rand_colors_1)

    square(food.x, food.y, 9, rand_colors_2)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move_food()
move()

done()