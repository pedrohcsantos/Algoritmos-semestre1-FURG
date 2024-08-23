# Capitalizar um nome. Exemplo: "pedro henrique cardoso dos santos" -> "Pedro Henrique Cardoso dos Santos"

nome = str(input("Informe um nome: "))

cont = 1
character = nome[0]
while cont < len(nome):
    if character == nome[0]:
        character = chr(ord(character)-32)
    if nome[cont-1] == ' ' and nome[cont] != 'd' and nome[cont] != 'e':
        character = character + chr(ord(nome[cont])-32)
    else:
        character = character + nome[cont]
    cont += 1
print(character)
        
