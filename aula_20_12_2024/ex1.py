# Criar uma caixa de texto que ao escrever "ânimo" e der "ok" a aplicação se fecha.

import graphics as gp
import random as rd

def foi_no_botao(botao,onde_cliquei):
    btX = botao.getP1().getX()
    btY = botao.getP1().getY()
    bt2X = botao.getP2().getX()
    bt2Y = botao.getP2().getY()
    print(f'({btX},{btY})({bt2X},{bt2Y}) --- ({onde_cliquei.getX()},{onde_cliquei.getX()})({onde_cliquei.getY()}{onde_cliquei.getY()})')
    if onde_cliquei.getX() > btX and onde_cliquei.getX() < bt2X and onde_cliquei.getY() > btY and onde_cliquei.getY() < bt2Y:
        return True
    return False

def cria_botao(x1,y1,x2,y2):
    novo_botao = gp.Rectangle(gp.Point(x1,y1), gp.Point(x2,y2))
    novo_botao.setFill('yellow')
    novo_botao.draw(win)
    botoes.append(novo_botao)
    return novo_botao

botoes = []
win = gp.GraphWin(  "Minha Janela"  , 400, 350) 
cores = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'pink', 'purple']
click = gp.Point(0,0)

botao = cria_botao(200,60,320,100)
texto = gp.Text(botao.getCenter(), 'Ok')
texto.draw(win)

botao_texto = cria_botao(10,60,190,100)
entrada = gp.Entry(botao_texto.getCenter(), 15)
entrada.setFill('white')
entrada.draw(win)

saida = gp.Text(gp.Point(200,150)," ")
saida.setSize(20)
saida.setTextColor('red')
saida.draw(win)

while True:
    onde_cliquei = win.getMouse()
    if foi_no_botao(botao,onde_cliquei):
        if entrada.getText() == 'ânimo':
            break
        else:
            saida.setText(f'Não é a entrada correta.')