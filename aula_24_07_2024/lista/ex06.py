# Faça um programa em python que leia 3 números e os mostre em ordem crescente.
a = int(input("Informe o primeiro número inteiro: "))
b = int(input("Informe o segundo número inteiro: "))
c = int(input("Informe o terceiro número inteiro: "))

if a < b and b < c:
    print(f"{a}, {b}, {c}")
else:
    if a < b and b > c and a < c:
        print(f"{a}, {c}, {b}")
    else:
        if b < a and a < c:
            print (f"{b}, {a}, {c}")
        else:
            if b < a and a > c and c > b:
                print(f"{b}, {c}, {a}")
            else:
                if c < a and a < b:
                    print(f"{c}, {a}, {b}")
                else:
                    if c < a and a < b and b > c:
                        print(f"{c}, {b}, {a}")