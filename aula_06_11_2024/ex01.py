# Faça um script que converta um número decimal em binário.

def conversor(x):
    binario = ' '
    if x == 0:
        binario = str(0)
    while x > 0:
        resto = x % 2
        x = x // 2
        binario = str(resto) + binario
    return(binario)

for i in range(20):
    print(f"{i} em binário: {conversor(i)}")