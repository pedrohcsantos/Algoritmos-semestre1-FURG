#Leia uma data DD,MM,AAAA e diga se ela é válida
#A) Desconsidere ano bissexto
#B) Considere ano Bissexto


#A) 

'''
dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))

if dia > 31 or dia < 1:
	print("Data inválida!")
else:
	if mes > 12 or mes < 1:
		print("Data inválida!") 
	else:
		if mes == 2 and dia > 28:
			print("Data inválida!") 
		else:
			if mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia > 30:
				print("Data inválida!")
			else:
				print(f"A data {dia}/{mes}/{ano} é válida!")
'''   

#B)

dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))

bissexto = ano % 4 == 0 and ano % 100 == 0

if dia > 31 or dia < 1:
	print("Data inválida!")
else:
	if mes > 12 or mes < 1:
		print("Data inválida!") 
	else:
		if bissexto == True:
			if mes == 2 and dia > 29:
				print("Data inválida!") 
			else:
				if mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia > 30:
					print("Data inválida!")
				else:
					print(f"A data {dia}/{mes}/{ano} é válida!")
		else: 	
			if mes == 2 and dia > 28:
				print("Data inválida!") 
			else:
				if mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia > 30:
					print("Data inválida!")
				else:
					print(f"A data {dia}/{mes}/{ano} é válida!")		

