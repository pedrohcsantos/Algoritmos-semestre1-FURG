# Leia um nome e mostre-o separado por linhas

nome = str(input("Informe um nome: "))
cont = 1
character = nome[0]
while cont < len(nome):
    character = character + nome[cont]
    if nome[cont] == ' ':
        character = character + "\n"
    cont += 1
print(character)