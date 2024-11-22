# Mostre os dados na tela:
'''
arq = open('aula.csv', 'r')

plan = arq.read()

print(plan)'''

# Liste apenas os nomes dos alunos:
'''
arq = open('aula.csv', 'r')

plan = arq.readlines()

for linha in plan:
    x = linha.split(',')
    print(x[1])
'''
# Mostre o aluno mais novo
arq = open('aula.csv', 'r')
y = []

plan = arq.readlines()
novo = '10351231'
nome_novo = ''
for linha in plan[1:]:
    x = linha.split(',')
    data = x[2][:-1]
    lista_data = data.split('/')
    data_padrao = lista_data[2] + lista_data[1] + lista_data[0]
    if data_padrao > novo:
        novo = data_padrao
        nome_novo = x[1]
print(nome_novo, novo)