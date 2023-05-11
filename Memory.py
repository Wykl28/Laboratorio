"""Actividad 5: Memory"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = ['\U0001F600','\U0001F603','\U0001F604','\U0001F601',
         '\U0001F606','\U0001F605','\U0001F923','\U0001F602',
         '\U0001F642','\U0001F643','\U0001FAE0','\U0001F609',
         '\U0001F60A','\U0001F607','\U0001F611','\U0001F970',
         '\U0001F60D','\U0001F929','\U0001F618','\U0001F617',
         '\U0001F61A','\U0001F619','\U0001F972','\U0001F60B',
         '\U0001F61B','\U0001F61C','\U0001F92A','\U0001F61D',
         '\U0001F910','\U0001F928','\U0001F610','\U0001F636']*2 #Elemento de inovacion
state = {'mark': None}
hide = [True] * 64
taps=0

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global taps
    taps += 1
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def show_victory_message():
    """Show a victory message in the center of the screen."""
    message_turtle = Turtle()
    message_turtle.hideturtle()
    message_turtle.penup()
    message_turtle.goto(0, 0)
    message_turtle.color('green')
    message_turtle.write("¡Victoria!", align="center", font=("Arial", 48, "bold"))

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    numero_destapados=0

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
        else:
            numero_destapados +=1
    
    if numero_destapados == 64:
        ontimer(show_victory_message, 500)
        pass

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 4.5, y + 7) # Ajuste de coordenadas para centrar
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    up()
    goto(220, -220)
    color('red')
    write(f'Taps: {taps}', font=('Arial', 16, 'normal',))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(650, 650, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()