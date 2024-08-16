#Leia um string e escreva letra por letra

x = str(input("Informe uma string: "))

cont = 0
while cont < len(x):
    print(x[cont])
    cont = cont + 1