#Leia o ano que nasceu e escreva se pode votar, se não pode voltar ou se é facultativo.

from datetime import date
ano_atual = (date.today().year)

ano_nasc = int(input("Informe o ano que você nasceu: "))
idade = ano_atual - ano_nasc

if idade < 16:
	print("Você não pode votar!")
elif 16 <= idade < 18 or idade >= 70:
	print("Seu voto é facultativo!")
elif idade >= 18:
	print("Você pode e deve votar!")

