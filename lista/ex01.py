# Faça um programa que, ao receber os valores da largura e do comprimento de uma figura geométrica, mostre se esta é um quadrado ou apenas um retângulo. Caso um valor seja menor ou igual a zero, deve-se mostrar um erro.

largura = float(input("Informe o valor da largura: "))
if largura == 0:
	while largura == 0: 
		largura = float(input("Informe um valor valor válido para a largura: "))

comprimento = float(input("Informe o valor do comprimento: "))		
if comprimento == 0:
	while comprimento == 0: 
		comprimento = float(input("Informe um valor válido para o comprimento: "))
if largura == comprimento:
	print("A figura geométrica é um quadrado!")
else:
	print("A figura geométrica é um retângulo!")
