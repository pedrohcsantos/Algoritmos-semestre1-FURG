# Escreva um programa que mostre a sequência de Fibonacci até o enésimo termo (n deve ser informado pelo usuário). A sequência de Fibonacci é aquela em que cada termo é a soma dos dois termos anteriores. Por exemplo, para n=8 escreva 0, 1, 1, 2, 3, 5, 8 e 13.

cont = 0
num1 = 0
num2 = 1
num3 = 0

print(f"{num1}\n{num2}")
while cont < 8:
	num1 = num1 + num2
	num2 = num2 + num3
	num3 = num2
	cont = cont + 1
	print(num1)

'''
1x:
num1 = 1
num2 = 1
num3 = 0

2x:
num1 = 2
num2 = 2
num3 = 1

3x:
num1 = 4
num2 = 4
num3 = 2
'''
