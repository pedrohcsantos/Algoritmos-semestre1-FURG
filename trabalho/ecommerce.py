import graphics as gp
import csv

CSV_FILE = "estoque_ecommerce.csv"

def cria_botao(x1,y1,x2,y2):
    novo_botao = gp.Rectangle(gp.Point(x1,y1), gp.Point(x2,y2))
    novo_botao.setFill('white')
    novo_botao.draw(win)
    botoes.append(novo_botao)
    return novo_botao

def foi_no_botao(botao,onde_cliquei):
    btX = botao.getP1().getX()
    btY = botao.getP1().getY()
    bt2X = botao.getP2().getX()
    bt2Y = botao.getP2().getY()
    print(f'({btX},{btY})({bt2X},{bt2Y}) --- ({onde_cliquei.getX()},{onde_cliquei.getX()})({onde_cliquei.getY()},{onde_cliquei.getY()})')
    if onde_cliquei.getX() > btX and onde_cliquei.getX() < bt2X and onde_cliquei.getY() < btY and onde_cliquei.getY() > bt2Y:
        return True
    return False

def estoquecsv():
    with open('estoque.csv','r') as arq:
        linhas = arq.readlines()
    linhas_sem_cabecalho = linhas[1:]
    estoque = []
    for linha in linhas_sem_cabecalho:
        dados = linha.strip().split(',')
        estoque.append(dados)
    return estoque

def adicionar_estoque(nome,valor,estoque):
    quantidade = 0
    ver_estoque = estoquecsv()
    if len(ver_estoque) == 0:
        novo_id = 1
    else:
        ultimo_produto = ver_estoque[-1]
        ultimo_id = ultimo_produto[0]
        ultimo_id = int(ultimo_id)
        novo_id = ultimo_id + 1 
    with open('estoque.csv', 'a') as arq:
        arq = csv.writer(arq)
        arq.writerow([novo_id,nome,valor,estoque,quantidade])


def verificar_estoque():
    cont = 1
    title = gp.Circle(gp.Point(300,20),15)
    ver_estoque = estoquecsv()
    win = gp.GraphWin(  "Estoque"  , 600, 450)
    titulo = gp.Text(title.getCenter(), 'Estoque Atual')
    titulo.setSize(18)
    titulo.setStyle('bold')
    titulo.draw(win)
    retangulo_id = gp.Rectangle(gp.Point(30, 100), gp.Point(100, 70))
    retangulo_id.setFill('lightblue')
    retangulo_id.setOutline('black')
    retangulo_id.draw(win)
    retangulo_id_text = gp.Text(retangulo_id.getCenter(), 'ID')
    retangulo_id_text.draw(win)
    retangulo_nome = gp.Rectangle(gp.Point(101, 100), gp.Point(240, 70))
    retangulo_nome.setFill('lightblue')
    retangulo_nome.setOutline('black')
    retangulo_nome.draw(win)
    retangulo_nome_text = gp.Text(retangulo_nome.getCenter(), 'Nome')
    retangulo_nome_text.draw(win)
    retangulo_valor = gp.Rectangle(gp.Point(241, 100), gp.Point(320, 70))
    retangulo_valor.setFill('lightblue')
    retangulo_valor.setOutline('black')
    retangulo_valor.draw(win)
    retangulo_valor_text = gp.Text(retangulo_valor.getCenter(), 'Valor')
    retangulo_valor_text.draw(win)
    retangulo_estoque = gp.Rectangle(gp.Point(321, 100), gp.Point(400, 70))
    retangulo_estoque.setFill('lightblue')
    retangulo_estoque.setOutline('black')
    retangulo_estoque.draw(win)
    retangulo_estoque_text = gp.Text(retangulo_estoque.getCenter(), 'Estoque')
    retangulo_estoque_text.draw(win)
    retangulo_quantidade = gp.Rectangle(gp.Point(401, 100), gp.Point(570, 70))
    retangulo_quantidade.setFill('lightblue')
    retangulo_quantidade.setOutline('black')
    retangulo_quantidade.draw(win)
    retangulo_quantidade_text = gp.Text(retangulo_quantidade.getCenter(), 'Quantidade Vendida')
    retangulo_quantidade_text.draw(win)

    y1_rect = 131
    y2_rect = 101
    
    while cont <= len(ver_estoque):
        gp.Rectangle(gp.Point(30, y1_rect), gp.Point(100, 101)).draw(win)
        gp.Rectangle(gp.Point(101, y1_rect), gp.Point(240, 101)).draw(win)
        gp.Rectangle(gp.Point(241, y1_rect), gp.Point(320, 101)).draw(win)
        gp.Rectangle(gp.Point(321, y1_rect), gp.Point(400, 101)).draw(win)
        gp.Rectangle(gp.Point(401, y1_rect), gp.Point(570, 101)).draw(win)
        y1_rect += 30
        y2_rect += 30
        cont = cont + 1

    y = 116

    for item in ver_estoque:
        gp.Text(gp.Point(65, y), item[0]).draw(win)
        gp.Text(gp.Point(170.5, y), item[1]).draw(win)
        gp.Text(gp.Point(280.5, y), item[2]).draw(win)
        gp.Text(gp.Point(360.5, y), item[3]).draw(win)
        gp.Text(gp.Point(485.5, y), item[4]).draw(win)
        y = y + 30

def cadastrar():
    win = gp.GraphWin(  "Novo cadastro"  , 500, 450)
    title = gp.Circle(gp.Point(250,20),15)
    titulo = gp.Text(title.getCenter(), 'Novo Cadastro')
    titulo.setSize(18)
    titulo.setStyle('bold')
    titulo.draw(win)
    novo_nome = gp.Rectangle(gp.Point(100,100), gp.Point(200,70))
    novo_nome.setFill("#64e3a1")
    novo_nome.setOutline("black")
    novo_nome.draw(win)
    novo_nome_text = gp.Text(novo_nome.getCenter(), 'Nome')
    novo_nome_text.draw(win)
    novo_valor = gp.Rectangle(gp.Point(100,150), gp.Point(200,120))
    novo_valor.setFill("#64e3a1")
    novo_valor.setOutline("black")
    novo_valor.draw(win)
    novo_valor_text = gp.Text(novo_valor.getCenter(), 'Valor')
    novo_valor_text.draw(win)
    novo_estoque = gp.Rectangle(gp.Point(100,200), gp.Point(200,170))
    novo_estoque.setFill("#64e3a1")
    novo_estoque.setOutline("black")
    novo_estoque.draw(win)
    novo_estoque_text = gp.Text(novo_estoque.getCenter(), 'Estoque')
    novo_estoque_text.draw(win)

    texto_nome = gp.Rectangle(gp.Point(220,100), gp.Point(400,70))
    texto_nome.draw(win)
    entrada_nome = gp.Entry(texto_nome.getCenter(), 18)
    entrada_nome.setFill('white')
    entrada_nome.draw(win)

    texto_valor = gp.Rectangle(gp.Point(220,150), gp.Point(400,120))
    texto_valor.draw(win)
    entrada_valor = gp.Entry(texto_valor.getCenter(), 18)
    entrada_valor.setFill('white')
    entrada_valor.draw(win)

    texto_estoque = gp.Rectangle(gp.Point(220,200), gp.Point(400,170))
    texto_estoque.draw(win)
    entrada_estoque = gp.Entry(texto_estoque.getCenter(), 18)
    entrada_estoque.setFill('white')
    entrada_estoque.draw(win)

    enviar = gp.Rectangle(gp.Point(200,330), gp.Point(300,300))
    enviar.setFill("#64e3a1")
    enviar.setOutline("black")
    enviar.draw(win)
    enviar_text = gp.Text(enviar.getCenter(), 'Cadastrar')
    enviar_text.draw(win)
    while True:
        onde_cliquei = win.getMouse()
        if foi_no_botao(enviar,onde_cliquei):
            nome = entrada_nome.getText()
            valor = entrada_valor.getText()
            estoque = entrada_estoque.getText()
            adicionar_estoque(nome,valor,estoque)
    
    

win = gp.GraphWin(  "Loja"  , 500, 450)
click = gp.Point(0,0)
botoes = []


estoque = cria_botao(20,300,230,250)
texto = gp.Text(estoque.getCenter(), 'Verificar Estoque')
texto.draw(win)

peca = cria_botao(270,300,480,250)
texto = gp.Text(peca.getCenter(), 'Cadastrar novas peças')
texto.draw(win)

venda = cria_botao(20,400,230,350)
texto = gp.Text(venda.getCenter(), 'Registrar Venda')
texto.draw(win)




while True:
    onde_cliquei = win.getMouse()
    if foi_no_botao(estoque,onde_cliquei):
        verificar_estoque()
    if foi_no_botao(peca,onde_cliquei):
        cadastrar()