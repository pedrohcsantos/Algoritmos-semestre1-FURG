'''    Faça um programa em python que desenhe uma pirâmide conforme 2 dados informados pelo usuário. O primeiro dado indica o "tijolo" e o segundo a quantidade de andares.

Ex:         Informe o tijolo: A

        Informe a quantidade de andares: 5

        A
       AAA
      AAAAA
     AAAAAAA
    AAAAAAAAA
'''
cont_espacos = 0
cont_tijolos = 1
x = ' '
tijolo = str(input("Informe o tijolo: "))
andares = int(input("Informe o número de andares: "))

while cont_espacos < andares:
	print((x * (andares - cont_espacos)) + tijolo * cont_tijolos)
	cont_espacos = cont_espacos + 1
	cont_tijolos = cont_tijolos + 2
