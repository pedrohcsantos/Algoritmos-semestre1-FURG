#Leia um nome e faça o espelho do nome. 'Pedro Santos' -> 'Ordep Sotnas'

x = str(input("Informe um nome: "))
cont = 0
palavra = ' '


while cont < len(x):
    if x[cont] == ' ':
        palavra = x[cont] + palavra
        cont_palavra = len(palavra)
        cont += 1
        while x[cont_palavra-1] != ' ':
            cont_palavra = cont_palavra - 1
            espelho = palavra + palavra[cont_palavra -1]
            espelho = espelho + ' '
    palavra = x[cont] + palavra
    cont_palavra = len(palavra)
    cont += 1
print(espelho)
        