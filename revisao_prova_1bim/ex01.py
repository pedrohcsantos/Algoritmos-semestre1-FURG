# Crie um programa que leia os dois lados de um retângulo e escreva a sua área. 
# Verifique para que o usuário digite apenas números positivos para representar os lados.

lado1 = int(input("Informe o primeiro lado do retângulo: "))
lado2 = int(input("Informe o segundo lado do retângulo: "))

if lado1 <= 0 or lado2 <= 0:
    while lado1 <= 0 or lado2 <= 0:
        print("Os números informados são inválidos, por favor informe números positivos maiores que 0!")
        lado1 = int(input("Informe o primeiro lado do retângulo: "))
        lado2 = int(input("Informe o segundo lado do retângulo: "))
    if lado1 == lado2:
        while lado1 == lado2 or lado1 <= 0 or lado2 <= 0:
            print("Os lados informados são iguais, por favor digite números diferentes para os lados e que sejam diferentes, para que a forma geométrica seja um retângulo!")
            lado1 = int(input("Informe o primeiro lado do retângulo: "))
            lado2 = int(input("Informe o segundo lado do retângulo: "))
        area = lado1 * lado2
        print(f"A área do retângulo é {area}!")
    else:     
        area = lado1 * lado2
        print(f"A área do retângulo é {area}!")
else:
    if lado1 == lado2:
        while lado1 == lado2:
            print("Os lados informados são iguais, por favor digite números diferentes para os lados, para que a forma geométrica seja um retângulo!")
            lado1 = int(input("Informe o primeiro lado do retângulo: "))
            lado2 = int(input("Informe o segundo lado do retângulo: "))
        area = lado1 * lado2
        print(f"A área do retângulo é {area}!")
    else:
        area = lado1 * lado2
        print(f"A área do retângulo é {area}!")