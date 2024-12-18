# Fechar a janela quando der um click proximo a bola anterior.

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
    clickposiX = 10 + last_click.getX()
    clickposiY = 10 + last_click.getY()
    clicknegatX = last_click.getX() - 10
    clicknegatY = last_click.getY() - 10
    if click.getX() < clickposiX and click.getY() < clickposiY: 
        segue = False
    if click.getX() < clicknegatX and click.getY() < clicknegatY:
        segue = False 
    nova_bolinha = gf.Circle(click, 10)
    cor = rd.randint(0, len(cores) - 1)
    nova_bolinha.setFill(cores[cor])
    nova_bolinha.draw(win)