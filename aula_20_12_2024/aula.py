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


def aciona_botoes(onde_cliquei):
    for um_botao in botoes:
        if foi_no_botao(um_botao,onde_cliquei):
            um_botao.setFill('red')
        else:
            um_botao.setFill('yellow')


botoes = []
win = gp.GraphWin(  "Minha Janela"  , 400, 350) 
cores = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'pink', 'purple']
click = gp.Point(0,0)

botao = cria_botao(10,60,190,100)
texto = gp.Text(botao.getCenter(), 'Botão')
texto.draw(win)

while True:
    onde_cliquei = win.getMouse()
    aciona_botoes(onde_cliquei)