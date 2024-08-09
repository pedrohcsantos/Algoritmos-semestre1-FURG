# Escreva um programa que receba um número inteiro positivo do usuário e verifique se ele é primo.
cont = 1
div = 0
num = int(input("Informe um número inteiro positivo: "))

if num < 2:
	print("O número não é primo!")
else:
	while cont <= num:
		if num % cont == 0:
			div = div + 1
		cont = cont + 1
if div > 2:
	print(f"não é primo\nnúmero de dividores:{div}")
else:
	print(f"é primo\nnúmero de dividores:{div}")
