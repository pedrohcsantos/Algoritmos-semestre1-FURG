#Faça um programa que converta graus celcius para Fahrenheitwhile != "C" or "F"

temp = input("Escolha a temperatura que vai ser convertida: Celsius(C) ou Fahrenheit(F): ")
while temp != "C" and temp != "F":
        temp = input("Escolha a temperatura certa: Celsius(C) ou Fahrenheit(F): ")
if temp == "C":
        tc = float(input("Escreva o valor da temperatura em celcius: "))
        tf = ((tc/5)*9)+32
        print(f"O valor de {tc:.2f} graus celcius em graus Fahrenheit {tf:.2f} é de ")
elif temp == "F":
        tf = float(input("Escreva o valor da temperatura em Fahrenheit: "))
        tc = ((tf -32)/9)*5
        print(f"O valor de {tf:.2f} graus Fahrenheit em graus Celcius {tc:.2f} é de ")
