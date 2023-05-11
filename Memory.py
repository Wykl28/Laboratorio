"""Actividad 5: Memory"""

from random import * #Importamos random
from turtle import * #Importamos turtle

from freegames import path #Importamos path de freegames

car = path('car.gif') # Se establece la ruta de la imagen del carro
tiles = ['\U0001F600','\U0001F603','\U0001F604','\U0001F601',
         '\U0001F606','\U0001F605','\U0001F923','\U0001F602',
         '\U0001F642','\U0001F643','\U0001FAE0','\U0001F609',
         '\U0001F60A','\U0001F607','\U0001F611','\U0001F970',
         '\U0001F60D','\U0001F929','\U0001F618','\U0001F617',
         '\U0001F61A','\U0001F619','\U0001F972','\U0001F60B',
         '\U0001F61B','\U0001F61C','\U0001F92A','\U0001F61D',
         '\U0001F910','\U0001F928','\U0001F610','\U0001F636']*2 # Lista de emojis duplicada
state = {'mark': None} # Creamos un diccionario que contendrá el estado actual del juego
hide = [True] * 64 # Creamos una lista que oculta cada casilla
taps=0 # Se inicializa la variable taps que cuenta los intentos

def square(x, y):
    """Dibuja un cuadrado blanco con contorno negro (x, y)."""
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
    """Conviete (x, y) coordenadas en tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convierte la cuenta de los tiles en (x, y) coordenadas."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Actualiza la mark y los tiles ocultos en base a los taps."""
    global taps
    taps += 1
    spot = index(x, y)
    mark = state['mark']

    # Si no hay casilla marcada, se marca la casilla en la que se hizo clic
    # Si la casilla ya está marcada, se desmarca la casilla
    # Si las dos casillas marcadas tienen emojis diferentes, se desmarcan ambas
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def show_victory_message():
    """Muestra un mensaje de victoria en el centro de la pantalla."""
    message_turtle = Turtle()
    message_turtle.hideturtle()
    message_turtle.penup()
    message_turtle.goto(0, 0)
    message_turtle.color('green')
    message_turtle.write("¡Victoria!", align="center", font=("Arial", 48, "bold"))

def draw():
    """Dibuja la imagen y los tiles."""
    clear() # Borra la pantalla
    goto(0, 0) # Se mueve al centro
    shape(car) # Asigna la imagen del carro
    stamp() # Dibuja lo anterior en la pantalla

    numero_destapados=0

    for count in range(64):
        if hide[count]:
            x, y = xy(count) # Si la ficha esta oculta dibuja un cuadrado
            square(x, y)
        else:
            numero_destapados +=1
    
    if numero_destapados == 64:
        ontimer(show_victory_message, 500) # Si se destapan todas las fichas muestra el mensaje de victoria
        pass

    mark = state['mark']

    if mark is not None and hide[mark]: 
        x, y = xy(mark)
        up()
        goto(x + 4.5, y + 7) # Ajuste de coordenadas para centrar
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal')) # Escribe el emoji

    up()
    goto(220, -220)
    color('red')
    write(f'Taps: {taps}', font=('Arial', 16, 'normal',)) # Escribe el número de taps en la pantalla

    update() # Actualiza la pantalla
    ontimer(draw, 100)


shuffle(tiles) # Mezcla las fichas
setup(650, 650, 370, 0) # Establece las proporciones de la pantalla 
addshape(car) # Agrega la imagen del carro
hideturtle()
tracer(False) # Desactiva la animación
onscreenclick(tap) 
draw()
done() # Finaliza el juego