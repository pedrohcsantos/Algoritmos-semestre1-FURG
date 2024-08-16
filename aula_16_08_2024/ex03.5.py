#Leia um nome e faça o espelho do nome. 'Pedro Santos' -> 'Ordep Sotnas'

x = str(input("Informe um nome: "))
cont = 0
palavra = ' '
espelho = ' '
cont_palavras = 0


while cont < len(x):
    palavra = x[cont] + palavra
    cont += 1
    if x[cont] == ' ':
        while x[cont_palavra] != x[cont]:
            cont_palavra = cont_palavra - 1
            espelho = palavra + palavra[cont_palavra -1]
            espelho = espelho + ' '
            cont_palavras += 1
    palavra = x[cont] + palavra
    cont_palavra = len(palavra)
    cont += 1
print(espelho)
