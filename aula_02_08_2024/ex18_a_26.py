# 18 Escreva um programa que calcule o fatorial de um número fornecido pelo usuário. O fatorial de um número n é o produto de todos os números inteiros de 1 a n.
'''
n = int(input('informe um número: '))
cont = 1
r = 1
while cont <= n :
	r = r * cont
	cont+=1
print(f'a fatorial de {n} é {r}')
'''
# 19 Escreva um programa que leia diversos números até que o usuário digite zero. Em seguida escreva a média dos números digitados.
'''
n = int(input('digite um número: '))
med = 0
div= 0

while n != 0 :
	med= med + n
	n = int(input('digite mais um número: '))
	div+=1
print(f'a média dos {div} números informados é: {med/div}')
'''
# 20 Escreva um programa que leia diversos funcionários e seu respectivo salario, ate que o nome de um funcionário seja “fim”. Em seguida escreva:
#	O nome do funcionário com maior salário
#	O nome do funcionário com menor salário
#	A média dos salários digitados
'''
nome = input('informe o nome do funcionário: ')
sal = int(input('informe o salário do funcionário: '))
cont = 1
somaSal = sal
tempNm = nome
tempNM = nome
salMax = sal
salMin = sal

while nome != 'fim' :
	nome = input('informe o nome do funcionário: ')
	if nome == 'fim' :
		print('cabou-se')
	else :
		sal = int(input('informe o salário do funcionário: '))
		if sal <= salMin :
			salMin = sal
			tempNm = nome
		if sal >= salMax :
			salMax = sal
			tempNM = nome
		somaSal = somaSal + sal
		cont = cont + 1
		medSal = somaSal/cont
print(f'MAIOR SALÁRIO: {tempNM}, R$:{salMax}\nMENOR SALÁRIO: {tempNm}, R$:{salMin}\nMÉDIA DOS SALÁRIOS: {medSal}\nSOMA DOS SALÁRIOS: {somaSal}\nSALÁRIOS INFORMADOS: {cont}')
'''
# 21 Escreva um programa de adivinhação de número. O programa deve conter um número secreto entre 1 e 1.000.000. O usuário deve chutar um número e o programa deve dizer se o número chutado é maior ou menor que o número secreto. O usuário deve tentar até acertar o número secreto. O código abaixo mostrar como sortear um número aleatório entre 0 e 10 em python:
# import random
# sorteado = random.randint(0,10)
'''
import random
sorteado = random.randint(0,100) 
r = int(input('qual número você acha que é?'))

while r != sorteado :
    if r > sorteado:
        r = int(input('errou! é um número menor, tente novamente: '))
    else :
        r = int(input('errou! é um número maior, tente novamente: '))
print('parabéns você acertou!')
'''
# 22Faça um programa em python que leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, inclusive o X se for o caso. Por exemplo, para o número 8, a saída será “9,11,13,15,17,19”.
'''
x = int(input('informe um número: '))
cont = 0

while cont < 6 :
	if x % 2 != 0 :
		print(x)
		x+=1
		cont+=1
	else :
		x+=1
cont+=1
'''
# 23 Escreva um programa que leia dois valores x e y. Em seguida escreva quais são os números primos contidos neste intervalo. Por exemplo, para x=3 e y=14 escreva: 3,5,7,11,13. Verifique se o usuário digitou x e y de modo que x<y.
'''
cont = 1
div = 0
num = int(input('informe um valor positivo: '))

while cont <= num:
    if num % cont == 0 :
        div = div + 1
    cont = cont + 1
if div > 2 :
    print('não é primo\nnúmero de dividores:',div)
else :
    print('é primo\nnúmero de dividores:',div)
    '''

# 24 Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Faça um programa em Python que receba o nome do(a) ginasta, e as notas de sua apresentação dadas pelos sete jurados. Ao final, informe a melhor nota, a pior nota e a sua média final, conforme a descrição acima informada (ou seja, retirar a melhor e a pior nota para calcular a média). As notas não são informadas em ordem (crescente ou decrescente).
'''
nome = input('informe o nome da ginasta: ')
nota = int(input('informe a nota do jurado: '))
cont = 1
somaNota = nota
notaMax = nota
notaMin = nota

while cont < 7 :
		nota = int(input('informe a nota do jurado: '))
		if nota < notaMin :
			notaMin = nota
		if nota > notaMax :
			notaMax = nota
		cont = cont + 1
		somaNota = somaNota + nota
medNota = ((somaNota-notaMin-notaMax)/5)
print(f'MAIOR NOTA: {notaMax}\nMENOR NOTA: {notaMin}\nMÉDIA DAS NOTAS(sem maior e menor): {medNota}')
'''
# 25 Considere uma sequência de números que atende a todos critérios abaixo:
# a - Possui sempre 2 dígitos , nem mais , nem menos.
# b - A representação do número possui pelo menos um dígito 1 ou um dígito 2.
# c - O número é múltiplo de 3.
# Faça um programa que implemente e mostre essa sequência.
# obs: tem que usar repetição para mostrar a sequência. Não pode mostrar os números “na mão”. 
'''
n = 10

while n < 100 :
    if n%3 == 0 and n%10 == 1 or n%10 == 2 or n//10 == 1 or n//10 == 2 :
        print(n)
    n+=1
'''
# 26 Construa um programa em Python que escreva uma contagem de 10 (dez) minutos, ou seja, mostre 0:00, e então 0:01, 0:02, ..., 0:58, 0:59, 1:00, 1:01,  ..., até 10:00.
'''
h = 0
m = 00
while h < 10 :
    m+=1
    if m == 60 and h < 10:
        h+=1
        m = -1
    else :
    	print(f'{h:02}:{m:02}')
print(f'{h:02}:{m+1:02}')   
'''