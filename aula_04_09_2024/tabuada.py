cont = 0
cont2 = 0
while cont <= 10:
	while cont2 < 10:
		numero = cont * cont2
		print('<table border=1>')
		print('<tr>')
		print(f'<td>{cont} x {cont2} = {numero}</td>')
		print('</tr>')
		print('</table>')
		cont2 = cont2 + 1
	cont2 = (cont2 * 0) + 1
	cont = cont + 1
