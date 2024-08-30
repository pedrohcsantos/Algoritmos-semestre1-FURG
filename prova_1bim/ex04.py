# Crie um programa em Python que leia um número inteiro e escreva todos os divisores desse número. Por exemplo:
# 14 | 1, 2, 7, 14
# 17 | 1, 17
# 24 | 1, 2, 3, 4, 6, 8, 12, 24

cont = 0
numero = int(input("Informe um número inteiro: "))
if numero < 0:
    while numero < 0:
        numero = int(input("Número inválido, informe um valor maior que 0: "))

while cont < numero:
    cont = cont + 1
    teste = numero % cont
    if cont == numero:
        print(f"{cont}")
    else:
        if teste == 0:
            print(f"{cont}",end=", ")