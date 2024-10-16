def primo(num):
	cont = 2
	while cont < num:
		if num % cont == 0:
			return False
		cont = cont + 1
	return True

for i in range(1000,2000):
	if primo(i):
		print(i)
