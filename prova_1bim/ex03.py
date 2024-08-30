#Crie um programa em Python que leia um número inteiro e escreva a soma dos números correspondentes a cada dígito do número. Por exemplo:
# 1412 | 8
# 4341220 | 16
# 101 | 2
# Nesta questão nõa pode utilizar strings. Deve utilizar operações matemáticas vistas em aula, como o resto e divisão inteira.

soma = 0
div = 10

numero = int(input("Informe um número inteiro: "))
if numero < 0:
    while numero < 0:
        numero = int(input("Número inválido, informe um valor maior que 0: "))

while numero > 0:
    numero_soma = numero % div
    soma = soma + numero_soma
    numero = numero // 10
print(soma)