# Escreva um programa que mostre a sequência de Fibonacci até o enésimo termo (n deve ser informado pelo usuário). A sequência de Fibonacci é aquela em que cada termo é a soma dos dois termos anteriores. Por exemplo, para n=8 escreva 0, 1, 1, 2, 3, 5, 8 e 13.

n = int(input('informe quantos números terá a sequência: '))
cont = 0
fibo1 = 0
fibo2 = 1
fiboX = 0

while cont <= n :
	print(fibo1)
	fiboX = fibo1 + fibo2
	fibo1 = fibo2
	fibo2 = fiboX
	cont+=1