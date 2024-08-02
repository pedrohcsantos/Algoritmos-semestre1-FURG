# Escreva um programa que mostre a tabuada (0 a 10) de um número fornecido pelo usuário.

cont = 0
num = int(input("Informe um número: "))
while cont <= 10:
	result = num * cont
	print(f"{cont}: {result}")
	cont = cont + 1
