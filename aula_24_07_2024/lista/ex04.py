'''
Crie um programa em Python que leia as notas do estudante nos 4 bimestres da nossa disciplina e a frequência (em porcentagem). A seguir informe se o estudante passou por média, rodou ou ficou em exame. Para passar por média, o estudante deve ter média maior ou igual a 7. Estudante com média abaixo de 3 roda sem ao menos fazer o exame. O estudante que tiver menos de 75% de frequência também está rodado na disciplina.
'''

n1 = float(input("Informe a nota do aluno no primeiro bimestre: "))
n2 = float(input("Informe a nota do aluno no segundo bimestre: "))
n3 = float(input("Informe a nota do aluno no terceiro bimestre: "))
n4 = float(input("Informe a nota do aluno no quarto bimestre: "))
frequencia = int(input("Informe a frequência do aluno: "))

nota_final = (n1 + n2 + n3 + n4)/4

if frequencia < 75 or nota_final < 3:
	print("O estudante rodou na disciplina sem direito a exame!")
else:
	if nota_final < 7 and nota_final >= 3:
		print("O estudante está em exame na disciplina!")
	else:
		print("O estudante passou na disciplina!")
