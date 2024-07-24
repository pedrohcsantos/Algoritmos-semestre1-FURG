# Leia os lados de um triângulo e escreva :
# A) Se é um triângulo válido
# B) O tipo:
# -Equilátero
# -Escaleno
# -Isósceles
a = float(input("Informe o lado a: "))
if a < 0:
	while a > 0:
		a = float(input("Informe um valor válido para o lado a: "))
b = float(input("Informe o lado b: "))
if b < 0:
	while b > 0:
		b = float(input("Informe um valor válido para o lado b: "))
c = float(input("Informe o lado c: "))
if c < 0:
	while c > 0:
		c = float(input("Informe um valor válido para o lado c: "))

soma_ab = a + b
soma_ac = a + c
soma_bc = b + c

if soma_ab < c and soma_ac < b and soma_bc < a:
	print("Não é um triângulo válido!")
else:
	if a == b and b == c:
		print("É um triângulo válido e equilátero!")
	else:
		if a == b and b != c:
			print("É um triângulo válido e isósceles!")
		else:
			if b == c and c != a:
				print("É um triângulo válido e isósceles!")
			else:
				print("É um triângulo válido e escaleno!")




