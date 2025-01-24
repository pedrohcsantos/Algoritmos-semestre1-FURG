# Escreva um programa em Python que calcule o comprimento da mais longa sequência de espaços em branco em uma string lida.

x = str(input("Digite uma frase: "))


var = {}
y = x.split()
test = len(y)

def criar_var(test): #Cria variáveis de acordo com a quantidade de espaços na string
    if x[0] == ' ': # se a string inicia com espaço então adiciona 1 no contador para criar as variáveis
        test = test + 1
    if x[-1] == ' ': # se a string termina com espaço então adiciona 1 no contador para criar as variáveis
        test = test + 1
    test = test - 1 # -1 espaço pois ex: str1 str2 str3, em 3 palavras possui 2 espaços entre elas
    for i in range(test):
        var["teste{0}".format(i)] = ' '
    return var

var = criar_var(test)

def contagem_espaco(x):
    cont = 0
    contvar = 0
    cont_esp = 0
    for i in x:
        if i == ' ':
            cont_esp = cont_esp + 1
            var["teste{0}".format(contvar)] = cont_esp
            if cont + 1 == len(x):
                break # Se a contagem + 1 for igual ao tamanho total da string q estamos percorrendo então acaba a execução do for, isso serve para não dar erro de index out of range, ao comparar um valor na frente no loop for.
            if x[cont+1] != ' ':
                contvar = contvar + 1
                cont_esp = 0   
        cont = cont + 1
    return var

var = contagem_espaco(x)

def teste_soma(var):   
    for n in var:
        if n == 'teste0':
            comparar = var[n]
        if n != 'teste0':
            armazenar = var[n]
            if comparar < armazenar:
                comparar = armazenar
    return comparar
    
soma = teste_soma(var)
print(soma)
print(var)
