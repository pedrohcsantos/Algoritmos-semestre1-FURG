'''Escreva um programa que mostre a seguinte sequência de números para um valor N informado pelo usuário:

   1

   2 2

   3 3 3

   4 4 4 4

   5 5 5 5 5

   …

   N N N N N N N …'''

cont = 1
num = int(input("Informe um número: "))
while cont <= num:
	cont_num = 1
	while cont_num <= cont:
		print(cont, end=' ')
		cont_num += 1 
	print()
	cont += 1

