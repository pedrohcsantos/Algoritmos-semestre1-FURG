# listas -> Tipo estruturado
#						Armazena qualquer coisa
#						Mutável

compras = ['nutella','pão','queijo','coquinha','patê','carne']
pedro = ['pedro','1,80','RG',['arroz','feijão','bife']]
compras[4] = 'brigadeiro'
compras.append('nescau')

'''
i = 0
while i < len(compras):
	print(compras[i])
	i = i + 1
'''
'''
for produto in compras:
	print(produto)

'''

# Perguntar as compras do usuário.

compras = []
gastos = []
cont = 0
i = 0
total = 0

numero = int(input('Informe o número de produtos comprados: '))

while cont < numero:
	item = str(input('Informe o produto comprado: '))
	preco = float(input('Informe o preço desse produto: '))
	compras.append(item)
	gastos.append(preco)
	cont = cont + 1

cont = cont * 0

print('Produto --------- Preço')
while cont < numero:
	print(f'{compras[i]} --------- {gastos[i]}')
	total = total + gastos[i]
	cont = cont + 1
	i = i + 1

print(f'Total --------- {total:.2f}')
