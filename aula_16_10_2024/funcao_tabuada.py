def tabuada(num):
	saida = ''
	for i in range(11):
		mult = num * i
		saida = saida + f'{num} x {i} = {mult}\n'
	return saida
		
for i in range(11):
	print(f'     Tabuada do {i}     ')
	print(tabuada(i))
	print('--------------------------')
