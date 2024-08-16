#Leia um nome e escreva apenas as vogais do nome, diga quantas vogais

x = str(input("Informe um nome: "))
cont = 0
vogal = 0

while cont < len(x):
    if x[cont] == 'a' or x[cont] == 'e' or x[cont] == 'i' or x[cont] == 'o' or x[cont] == 'u':
        vogal = vogal + 1
        print(x[cont])
    cont = cont + 1
print(f"O nome {x} possui {vogal} vogais")