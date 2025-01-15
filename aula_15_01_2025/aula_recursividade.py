#Chamar a própria função nela mesma
#Fibonacci
'''
def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
    
print(fibonacci(7))
'''

def torres_de_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
        return
    torres_de_hanoi(n - 1, origem, auxiliar, destino)
    print(f"Mover disco {n} de {origem} para {destino}")
    torres_de_hanoi(n - 1, auxiliar, destino, origem)

torres_de_hanoi(3,'A', 'B', 'C')


    
