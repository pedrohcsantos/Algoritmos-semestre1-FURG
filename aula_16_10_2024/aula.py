def dobro(num):
	saida = num * 2
	return saida

def par_impar(valor):
	if valor % 2 == 0:
		return True
	return False

def teste():
	print("Volta às aulas ")
	return 2
	print("Amamos grama sendo cortada")

numero = int(input("Num: "))

duplo = dobro(numero)
print(duplo)

print(par_impar(12))

if par_impar(numero):
	print("Par!")
else:
	print("IMPAR!")
