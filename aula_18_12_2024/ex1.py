# Fechar a janela quando der double click.

import graphics as gf
import random as rd

win = gf.GraphWin(  "Minha Janela"  , 400, 350) 
cores = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'pink', 'purple']
click = gf.Point(0,0)
segue = True

while segue:
    last_click = click
    click = win.getMouse()
    print(click.getX(), click.getY())
    if last_click.getX() == click.getX() and last_click.getY() == click.getY(): 
        segue = False
    nova_bolinha = gf.Circle(click, 10)
    cor = rd.randint(0, len(cores) - 1)
    nova_bolinha.setFill(cores[cor])
    nova_bolinha.draw(win)