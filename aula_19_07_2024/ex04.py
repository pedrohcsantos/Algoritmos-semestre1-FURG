# Leia os lados de um triângulo e escreva :
# A) Se é um triângulo válido
# B) O tipo:
# -Equilátero
# -Escaleno
# -Isósceles

lado_a = float(input("informe o lado A: "))
lado_b = float(input("informe o lado B: "))
lado_c = float(input("informe o lado C: "))

if lado_a > lado_b - lado_c and lado_a < lado_b + lado_c and lado_b > lado_a - lado_c and lado_b < lado_a + lado_c and lado_c > lado_a - lado_b and lado_c < lado_a + lado_b:
	if lado_a == lado_b and lado_b == lado_c:
		print("O triângulo é válido, e é um triângulo equilátero!")
	else: 
		if lado_a != lado_b and lado_b != lado_c:
			print("O triângulo é válido, e é um triângulo escaleno!")
		else:
			print("O triângulo é válido, e é um triângulo isósceles!")
else:
	print("O triângulo não é válido!")


