# Escreva um programa que calcule e mostre a soma dos números de 1 a N. Não utilize as equações de progressão aritmética.

cont = 0
soma = 0
num = int(input("Informe um número: "))

while cont < num:
	cont = cont + 1
	soma = soma + cont
	print(soma)
