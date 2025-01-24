# Aprendemos que em Python é usual representar uma matriz como uma lista de listas. Crie uma função de receba uma matriz representada dessa forma e:
# a) Verifique se ela é uma matriz válida retangular ou quadrada;
# b) Retorne um texto indicando se é válida e qual é o maior valor na matriz;
# c) Se a matriz for quadrada (o número de linhas igual ao número de colunas),
# acrescente ao texto o somatório dos valores da diagonal principal.


matriz1 = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
matriz2 = [[1, 2], [3, 4, 5], [5, 6]]
matriz3 = [[1, 2], [3, 8], [5, 6]]

def verificar_matriz(matriz):    
    teste = matriz[0]
    cont_diag = 0
    soma = 0
    maior = 0
    for x in matriz:
        if len(teste) != len(x):
            return(f'{matriz} não é uma matriz válida')
        else:
            armazenar = x[0]
            for n in x:
                if n > armazenar:
                    armazenar = n
            if armazenar > maior:
                maior = armazenar              
        if len(teste) == len(matriz):
            soma = soma + x[cont_diag]
            cont_diag = cont_diag + 1
    if len(teste) == len(matriz):
        return(f'{matriz} é uma matriz válida, {maior} é o maior valor e a soma da diagonal é {soma}')
    else:
        return(f'{matriz} é uma matriz válida, e {maior} é o maior valor.')

ver1 = verificar_matriz(matriz1)
ver2 = verificar_matriz(matriz2)
ver3 = verificar_matriz(matriz3)


print(ver1)
print(ver2)
print(ver3)

