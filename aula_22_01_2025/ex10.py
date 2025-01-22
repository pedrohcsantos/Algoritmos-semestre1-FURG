# Escreva um programa em Python que calcule o comprimento da mais longa sequência de espaços em branco em uma string lida.

x = str(input("Digite uma frase: "))


var = {}
y = x.split()
test = len(y)
cont = 0
contvar = 0
cont_esp = 0


def criar_var(test):
    if x[0] == ' ':
        test = test + 1
    if x[-1] == ' ':
        test = test + 1
    test = test - 1
    for i in range(test):
        var["teste{0}".format(i)] = ' '
    return var

var = criar_var(test)



for i in x:
    
    if i == ' ':
        cont_esp = cont_esp + 1
        var["teste{0}".format(contvar)] = cont_esp
        if x[cont+1] != ' ':
            contvar = contvar + 1
            cont_esp = 0
    cont = cont + 1
    

print(var)