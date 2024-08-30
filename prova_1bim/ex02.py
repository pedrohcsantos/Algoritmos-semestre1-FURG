# Crie um programa em Python que leia uma data de 2024 ou 2025 e escreva qual o dia da semana corresponde à data.
# Observe que 2024 é um ano bissexto e que o ano começou em uma segunda-feira. Por exemplo:
# 12/01 | Segunda-feira
# 03/04 | quarta-feira
# 31/03 | domingo
# 31/12 | terça-feira



dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano (2024 ou 2025): "))

if ano != 2024 and ano != 2025:
    while ano != 2024 or ano != 2025:
        ano = int(input("Data inválida, deve escolher o ano de 2024 ou o ano de 2025: "))

if ano == 2024:
    if mes == 2 and dia > 29:
        dia = int(input("Dia inválido para esse mês, o dia deve ser entre 1 e 29: "))
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia > 31:
        dia = int(input("Dia inválido para esse mês, o dia deve ser entre 1 e 31: "))
    if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
        dia = int(input("Dia inválido para esse mês, o dia deve ser entre 1 e 31: "))
    if mes == 1:
        # dia_inicial = segunda
        data = dia % 7
        if data == 1:
            print("segunda")
        if data == 2:
            print("terça")
        if data == 3:
            print("quarta")
        if data == 4:
            print("quinta")
        if data == 5:
            print("sexta")
        if data == 6:
            print("sábado")
        if data == 0:
            print("domingo")
    if mes == 2:
        # dia_inicial = quinta
        data = dia % 7
        if data == 5:
            print("segunda")
        if data == 6:
            print("terça")
        if data == 0:
            print("quarta")
        if data == 1:
            print("quinta")
        if data == 2:
            print("sexta")
        if data == 3:
            print("sábado")
        if data == 4:
            print("domingo")
    if mes == 3:
        # dia_inicial = sexta
        data = dia % 7
        if data == 4:
            print("segunda")
        if data == 5:
            print("terça")
        if data == 6:
            print("quarta")
        if data == 0:
            print("quinta")
        if data == 1:
            print("sexta")
        if data == 2:
            print("sábado")
        if data == 3:
            print("domingo")
    if mes == 4:
        # dia_inicial = quinta
        data = dia % 7
        if data == 1:
            print("segunda")
        if data == 2:
            print("terça")
        if data == 3:
            print("quarta")
        if data == 4:
            print("quinta")
        if data == 5:
            print("sexta")
        if data == 6:
            print("sábado")
        if data == 0:
            print("domingo")
    if mes == 5:
        # dia_inicial = quarta
        data = dia % 7
        if data == 6:
            print("segunda")
        if data == 0:
            print("terça")
        if data == 1:
            print("quarta")
        if data == 2:
            print("quinta")
        if data == 3:
            print("sexta")
        if data == 4:
            print("sábado")
        if data == 5:
            print("domingo")
    if mes == 6:
        # dia_inicial = quinta
        data = dia % 7
        if data == 3:
            print("segunda")
        if data == 4:
            print("terça")
        if data == 5:
            print("quarta")
        if data == 6:
            print("quinta")
        if data == 0:
            print("sexta")
        if data == 1:
            print("sábado")
        if data == 2:
            print("domingo")
    if mes == 7:
        # dia_inicial = segunda
        data = dia % 7
        if data == 1:
            print("segunda")
        if data == 2:
            print("terça")
        if data == 3:
            print("quarta")
        if data == 4:
            print("quinta")
        if data == 5:
            print("sexta")
        if data == 6:
            print("sábado")
        if data == 0:
            print("domingo")
    if mes == 8:
        # dia_inicial = quinta
        data = dia % 7
        if data == 5:
            print("segunda")
        if data == 6:
            print("terça")
        if data == 0:
            print("quarta")
        if data == 1:
            print("quinta")
        if data == 2:
            print("sexta")
        if data == 3:
            print("sábado")
        if data == 4:
            print("domingo")
    if mes == 9:
        # dia_inicial = domingo
        data = dia % 7
        if data == 2:
            print("segunda")
        if data == 3:
            print("terça")
        if data == 4:
            print("quarta")
        if data == 5:
            print("quinta")
        if data == 6:
            print("sexta")
        if data == 0:
            print("sábado")
        if data == 1:
            print("domingo")
    if mes == 10:
        # dia_inicial = terça
        data = dia % 7
        if data == 1:
            print("segunda")
        if data == 2:
            print("terça")
        if data == 3:
            print("quarta")
        if data == 4:
            print("quinta")
        if data == 5:
            print("sexta")
        if data == 6:
            print("sábado")
        if data == 0:
            print("domingo")
    if mes == 11:
        # dia_inicial = novembro
        data = dia % 7
        if data == 4:
            print("segunda")
        if data == 5:
            print("terça")
        if data == 6:
            print("quarta")
        if data == 0:
            print("quinta")
        if data == 1:
            print("sexta")
        if data == 2:
            print("sábado")
        if data == 3:
            print("domingo")
    if mes == 12:
        # dia_inicial = domingo
        data = dia % 7
        if data == 2:
            print("segunda")
        if data == 3:
            print("terça")
        if data == 4:
            print("quarta")
        if data == 5:
            print("quinta")
        if data == 6:
            print("sexta")
        if data == 0:
            print("sábado")
        if data == 1:
            print("domingo")

if ano == 2025:
    if mes == 2 and dia > 28:
        dia = int(input("Dia inválido para esse mês, o dia deve ser entre 1 e 28: "))
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia > 31:
        dia = int(input("Dia inválido para esse mês, o dia deve ser entre 1 e 31: "))
    if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
        dia = int(input("Dia inválido para esse mês, o dia deve ser entre 1 e 31: "))
    if mes == 1:
        # dia_inicial = quarta
        data = dia % 7
        if data == 6:
            print("segunda")
        if data == 0:
            print("terça")
        if data == 1:
            print("quarta")
        if data == 2:
            print("quinta")
        if data == 3:
            print("sexta")
        if data == 4:
            print("sábado")
        if data == 5:
            print("domingo")
    if mes == 2:
        # dia_inicial = sabado
        data = dia % 7
        if data == 3:
            print("segunda")
        if data == 4:
            print("terça")
        if data == 5:
            print("quarta")
        if data == 6:
            print("quinta")
        if data == 0:
            print("sexta")
        if data == 1:
            print("sábado")
        if data == 2:
            print("domingo")
    if mes == 3:
        # dia_inicial = sabado
        data = dia % 7
        if data == 3:
            print("segunda")
        if data == 4:
            print("terça")
        if data == 5:
            print("quarta")
        if data == 6:
            print("quinta")
        if data == 0:
            print("sexta")
        if data == 1:
            print("sábado")
        if data == 2:
            print("domingo")
    if mes == 4:
        # dia_inicial = terça
        data = dia % 7
        if data == 0:
            print("segunda")
        if data == 1:
            print("terça")
        if data == 2:
            print("quarta")
        if data == 3:
            print("quinta")
        if data == 4:
            print("sexta")
        if data == 5:
            print("sábado")
        if data == 6:
            print("domingo")
    if mes == 5:
        # dia_inicial = quinta
        data = dia % 7
        if data == 5:
            print("segunda")
        if data == 6:
            print("terça")
        if data == 0:
            print("quarta")
        if data == 1:
            print("quinta")
        if data == 2:
            print("sexta")
        if data == 3:
            print("sábado")
        if data == 4:
            print("domingo")
    if mes == 6:
        # dia_inicial = domingo
        data = dia % 7
        if data == 2:
            print("segunda")
        if data == 3:
            print("terça")
        if data == 4:
            print("quarta")
        if data == 5:
            print("quinta")
        if data == 6:
            print("sexta")
        if data == 0:
            print("sábado")
        if data == 1:
            print("domingo")
    if mes == 7:
        # dia_inicial = terça
        data = dia % 7
        if data == 0:
            print("segunda")
        if data == 1:
            print("terça")
        if data == 2:
            print("quarta")
        if data == 3:
            print("quinta")
        if data == 4:
            print("sexta")
        if data == 5:
            print("sábado")
        if data == 6:
            print("domingo")
    if mes == 8:
        # dia_inicial = sexta
        data = dia % 7
        if data == 4:
            print("segunda")
        if data == 5:
            print("terça")
        if data == 6:
            print("quarta")
        if data == 0:
            print("quinta")
        if data == 1:
            print("sexta")
        if data == 2:
            print("sábado")
        if data == 3:
            print("domingo")
    if mes == 9:
        # dia_inicial = segunda
        data = dia % 7
        if data == 1:
            print("segunda")
        if data == 2:
            print("terça")
        if data == 3:
            print("quarta")
        if data == 4:
            print("quinta")
        if data == 5:
            print("sexta")
        if data == 6:
            print("sábado")
        if data == 0:
            print("domingo")
    if mes == 10:
        # dia_inicial = quarta
        data = dia % 7
        if data == 6:
            print("segunda")
        if data == 0:
            print("terça")
        if data == 1:
            print("quarta")
        if data == 2:
            print("quinta")
        if data == 3:
            print("sexta")
        if data == 4:
            print("sábado")
        if data == 5:
            print("domingo")
    if mes == 11:
        # dia_inicial = sábado
        data = dia % 7
        if data == 3:
            print("segunda")
        if data == 4:
            print("terça")
        if data == 5:
            print("quarta")
        if data == 6:
            print("quinta")
        if data == 0:
            print("sexta")
        if data == 1:
            print("sábado")
        if data == 2:
            print("domingo")
    if mes == 12:
        # dia_inicial = segunda
        data = dia % 7
        if data == 1:
            print("segunda")
        if data == 2:
            print("terça")
        if data == 3:
            print("quarta")
        if data == 4:
            print("quinta")
        if data == 5:
            print("sexta")
        if data == 6:
            print("sábado")
        if data == 0:
            print("domingo")