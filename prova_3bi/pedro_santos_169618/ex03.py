# Um email válido possui o seguinte formato meu.nome@gmail.com: nome do utilizador: meu.nome; nome do subdominio: gmail;
# nome do dominio: com; endereço do servidor do email: gmail.com
'''O arquivo emails.txt possui uma lista de emails. No entanto, alguns emails não
foram digitados corretamente e precisam ser corrigidos. Leia o arquivo email.txt e
crie um novo arquivos emails_invalidos.txt apenas com os emails inválidos.
Veja alguns exemplos:
# E-mails válidos
joao.silva@gmail.com
maria_oliveira@outlook.com
ana123@yahoo.com.br
contato@empresa.com
jose-da-silva@provedor.net
email.teste@sub.dominio.com
andre.prisco@furg.br
# E-mails inválidos
joao.silva_gmail.com # Falta o "@"
@outlook.com # Falta o nome antes do "@"
maria@@yahoo.com.br # Dois "@"
anateste@.com # Servidor ausente
email@dominio..com # Dois pontos consecutivos
ana@dominio,com # Vírgula ao invés de ponto
sem-arroba-sem-nada # Sem "@" e domínio
123@456.789 # Domínio apenas numérico'''

def emails_invalidos():
    cont = 0
    with open('emails.txt', 'r') as arq:
        linhas = arq.readlines()
    novo_arq = 'emails_invalidos.txt'
    with open(novo_arq, 'w') as arquivo:
        for emails in linhas:
            if emails[0] == '@':
                arquivo.write(f'{emails}')
            elif '@' not in emails and 'com' not in emails:
                arquivo.write(f'{emails}')
            elif '@' not in emails:
                arquivo.write(f'{emails}')
            elif 'com' not in emails and 'br' not in emails and 'net' not in emails:
                arquivo.write(f'{emails}')
            for i in emails:
                if cont + 1 == len(emails):
                    break
                if i == '@' and emails[cont+1] == '.':
                    arquivo.write(f'{emails}')
                if i == '@' and emails[cont+1] == '@':
                    arquivo.write(f'{emails}')
                if i == '.' and emails[cont+1] == '.':
                    arquivo.write(f'{emails}')
                if i == ',' and emails[cont+1] == 'c':
                    arquivo.write(f'{emails}')
                cont = cont + 1
            cont = 0
    return novo_arq

emails_invalidos()
