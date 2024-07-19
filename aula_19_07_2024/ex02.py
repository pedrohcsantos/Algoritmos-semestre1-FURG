# Peça para o usuário informar seu nome e a hora do dia e escreva uma mensagem conforme a hora. 
# Ex: Bom dia, Pedro 

nome = input("Qual o seu nome? ")
hora = input("Que horas são? ")

if "00:00" <= hora < "06:00":
	print(f"Boa madrugada, {nome}!")
elif "06:00" <= hora < "12:00":
	print(f"Bom dia, {nome}!")
elif "12:00" <= hora < "18:00":
	print(f"Boa tarde, {nome}!")
elif "18:00" <= hora < "00:00":
	print(f"Boa noite, {nome}!")
