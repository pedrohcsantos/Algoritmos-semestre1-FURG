'''
	Faça um programa em python que pergunte ao usuário o seguinte:
- A viagem custará menos de R$ 30?
- Terá Wifi?
- Terá piscina?
- Terá churrasqueira?
	O programa deverá mostrar se a viagem ocorrerá de acordo com as seguintes regras:
- Deverá custar menos de R$ 30
- Tem que ter wifi e piscina
- Se não tiver wifi ou piscina, tem que ter churrasqueira
'''

valor_viagem = float(input("Quanto custará a viagem? "))
wifi = str(input("Terá Wi-fi? "))
piscina = str(input("Terá piscina? "))
churrasqueira = str(input("Terá churrasqueira? "))

if valor_viagem > 30 or valor_viagem <0:
	print("A viagem não ocorrerá!")
else:
	if wifi == 'não' or piscina == 'não':
		if churrasqueira == 'não':
			print("A viagem não ocorrerá!")
		if churrasqueira == 'sim':
			print("A viagem ocorrerá!")
	if wifi == 'sim' and piscina == 'sim':
		print("A viagem ocorrerá!")
