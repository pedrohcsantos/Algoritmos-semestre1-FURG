# Aula de condicionais
# Comandos Estruturados: if/else; elif

idade = int(input("Digite sua idade: "))
print(idade)

if idade >= 18:
	print("Pode beber cerveja!")
	carteira = str(input("Possui carteira de motorista? "))
	if carteira == "sim":
		print("Pode dirigir!")
	else:
		print("Vá de ônibus!") 
else:
	print("Beba leite e ande de bike!")
