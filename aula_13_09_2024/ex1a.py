# Leia duas palavras e escreva se elas são anagramas.

palavra1 = input(str("Digite uma palavra: "))
palavra2 = input(str("Digite outra palavra: "))
contagem1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
contagem2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
palavra1 = palavra1.lower()
palavra2 = palavra2.lower()

if len(palavra1) == len(palavra2):
    for letra in palavra1:
        indice = ord(letra) - ord('a')
        contagem1[indice] = contagem1[indice] + 1
    for letra in palavra2:
        indice = ord(letra) - ord('a')
        contagem2[indice] = contagem2[indice] + 1        
    anagrama = True
    cont = 0
    while anagrama and cont < len(contagem1):
        if contagem1[cont] != contagem2[cont]:
            anagrama = False
        cont = cont + 1
    if anagrama:
        print('É um anagrama!')
    else:
        print('Não é um anagrama!')
else:
    print("Não é um anagrama!")