# Crie uma função que receba uma data em formato DD/MM/AAAA e retorne seu nome por extenso. A função deve receber como parâmetro o nome da
# cidade base. Considere que a data entregue é válida. Não precisa perder tempo validando a data.

data1 = '24/01/2025'
local1 = 'Rio Grande'
data2 = '01/04/4000'
local2 = 'Marte'
data3 = '31/05/2000'
local3 = 'Itu'
meses = {'01': 'Janeiro', '02': 'Fevereiro','03': 'Março', '04': 'Abril', '05': 'Maio', '06': 'Junho', '07': 'Julho', '08': 'Agosto', '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'}
def verificar_data(data,local):
    data_list = data.split('/')
    if data_list[0] == '01' or data_list[0] == '1':
        data_list[0] = '1°'
    data_list = f'{local}, {data_list[0]} de {meses[data_list[1]]} de {data_list[2]}'
    return data_list
data_list1 = verificar_data(data1,local1)
data_list2 = verificar_data(data2,local2)
data_list3 = verificar_data(data3,local3)

print(data_list1)
print(data_list2)
print(data_list3)
