#Leia um nome e faça o espelho do nome. 'Pedro Santos' -> 'Ordep Sotnas'

nome = str(input("Informe um nome: "))
cont = 1
cont_palavras = 0
palavra_reversa = ''

while cont < len(nome):
    cont += 1
    if nome[cont-1] == ' ':
        while nome[cont] != ' ' and nome[cont] != nome[0]:
            cont_reverse = cont - 1
            palavra_reversa = palavra_reversa + nome[cont]
        print(palavra_reversa)
