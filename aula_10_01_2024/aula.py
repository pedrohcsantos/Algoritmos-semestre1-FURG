import sys
texto = ["678"]
print("Ponteiros --->",sys.getrefcount(texto))
outro = texto
print(texto,id(texto))
print(outro,id(outro))
print("-------------")
print("Ponteiros --->",sys.getrefcount(texto))