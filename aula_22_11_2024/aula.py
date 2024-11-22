arq = open('poema.txt','r')

# r - read
# w - write
# a - append

# texto = arq.read()
# print(texto)

text_list = arq.readlines()
print(text_list)

arq.close
