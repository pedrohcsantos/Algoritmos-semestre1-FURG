# Cada carro tem um desempenho, que é geralmente medido por quantos quilômetros ele pode percorrer com 1 litro de gasolina.
# Por exemplo, os carros mais econômicos podem fazer 16km/l. Escreva um programa em python que leia
# o desempenho de um carro e um trajeto percorrido em um mês.
# Escreva o quanto foi gasto em reais, considerando a gasolina 5,85 reais. Por exemplo:
# Desempenho | Trajeto | Gasto
# 12 km/l    | 1000 km | 487,50 reais
# 16 km/l    | 1500 km | 548,44 reais
# 8,9 km/l   | 2000 km | 1314,60 reais
# Permita apenas valores positivos para desempenho e trajeto

gasolina = 5.85

desempenho = float(input("Informe o desempenho do carro: "))
if desempenho < 0:
    while desempenho < 0:
        desempenho = float(input("Valor inválido, forneça um número maior que 0: "))
trajeto = int(input("Informe o trajeto percorrido em um mês: "))
if trajeto < 0:
    while trajeto < 0:
        trajeto = float(input("Valor inválido, forneça um número maior que 0: "))

gasto_litros = trajeto / desempenho
gasto_reais = gasto_litros * 5.85
print(f"Foi gasto {gasto_reais:.2f} reais em gasolina!")

