LOGIN = 'mahiro'
SENHA = '123'

tentativas = 0

aceitou_cupom = False
usou_o_link_do_influencer = False

CUPOM = 'vemserfeliz'
DESCONTO = 0.2

YOUTUBERS = ['brksedu', 'alanzoka']

while True:
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')
    if login == LOGIN and senha == SENHA:
        print('Login realizado')

        cupom = input('Digite o código do cupom de desconto de 20%? ')
        if cupom == CUPOM:
            aceitou_cupom = True
            print('Cupom aceito')
        else:
            print('Cupom negado')

        influencer = input('Você entrou nessa página por meio do link de qual influencer? ')
        for youtuber in YOUTUBERS:
            if youtuber == influencer:
                usou_o_link_do_influencer = True
                print('Desconto aplicado')
        
        if not usou_o_link_do_influencer:
            print('Desconto negado')

        break
    else:
        print('Acesso negado')
        tentativas += 1
        if tentativas > 3:
            print('Numero limite de tentativas ultrapassado')
            break