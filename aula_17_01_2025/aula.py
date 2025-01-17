# Similaridade de Strings: Crie uma função que receba 2 strings e retorne a similaridade entre elas. OBS: att, recebe 3 strings.

str1 = str(input("Digite algo: "))
str2 = str(input("Digite algo: "))
str3 = str(input("Digite algo: "))

def comparar(string1,string2):
    pc_final = 'prisco'
    if string1 > string2:
        cont = 1
        dif = len(string1) - len(string2)
        pc = 0
        while cont <= dif:
            string2 = string2 + ' '
            cont = cont + 1 
        for i,c in zip(string1,string2):
            if i == c:
                pc = pc + 1
        pc_final = (pc/len(string1)) * 100
        return pc_final
    elif string2 > string1:
        cont = 1
        dif = len(string1) - len(string2)
        pc = 0
        while cont <= dif:
            string1 = string1 + ' '
            cont = cont + 1 
        for i,c in zip(string2,string1):
            if i == c:
                pc = pc + 1
        pc_final = (pc/len(string2)) * 100
        return pc_final
    else:
        for i,c in zip(string2,string1):
            if i == c:
                pc = pc + 1
        pc_final = (pc/len(string1)) * 100
        return pc_final



similaridade1 = comparar(str1,str2)
similaridade2 = comparar(str1,str3)

if similaridade1 > similaridade2:
    print(f'As strings {str1} e {str2} são mais semelhantes entre elas.')
elif similaridade2 > similaridade1:
    print(f'As strings {str1} e {str3} são mais semelhantes entre elas.')
else: print(f'As strings {str2} e {str3} são mais semelhantes entre elas.')

#print(f'As strings são {similaridade}% iguais!')