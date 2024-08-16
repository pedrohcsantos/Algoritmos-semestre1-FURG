#Leia uma palavra e mostre sei epelho. Pedro -> Ordep, casa -> asac, ana -> ana

x = str(input("Digite uma palavra: "))
cont = len(x)
espelho = ' '
while cont > 0:
    espelho = espelho + x[cont-1]
    cont = cont - 1
print(espelho)