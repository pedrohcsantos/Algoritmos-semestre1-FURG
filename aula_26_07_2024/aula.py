# Leia um número e faça a tabuada.
'''
numero = int(input("Informe um número inteiro para ver sua tabuada: "))
tabuada = 0
C = 0
while C <= 10:
	print(f"{numero} x {C} = {numero*C}")
	C += 1
print("fim")
'''

# Crie um algoritmo que leia uma senha até acerta-la.

tentativas = 4
senha_correta = "gojo"
senha_teste = input("Digite a senha: ")
if senha_teste != senha_correta:
	while senha_teste != senha_correta and tentativas > 0:
		senha_teste = input(f"Senha incorreta, digite novamente ({tentativas} tentativas restantes): ")
		tentativas = tentativas - 1
		if tentativas == 0:
			print("Limite de tentativas atingido!")
else:
	print("Senha correta")
