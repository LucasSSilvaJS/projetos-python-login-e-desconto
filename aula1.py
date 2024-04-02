tentativas = 0
SENHA = '123456'

while True:
    senha = input('Digite sua senha: ')
    if senha == SENHA:
        print('Login realizado!')
        break
    else:
        print('Acesso negado!')