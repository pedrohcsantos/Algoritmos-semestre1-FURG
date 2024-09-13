# Leia um nome e escreva um anagrama aleatório desse nome.

import random
cont = 0
nome_num = ' '
nova_palavra = ' '
nome = input(str('Informe um nome: '))
for letra in nome:
    letra_num = ord(letra)
    letra_num = str(letra_num)
    nome_num = nome_num + ' ' + letra_num
lista = nome_num.split()
print(lista)

while cont < len(nome):
    elemento = random.choice(lista)
    lista.remove(elemento)
    elemento = int(elemento)
    elemento = chr(elemento)
    nova_palavra = nova_palavra + elemento
    cont += 1
print(nova_palavra)