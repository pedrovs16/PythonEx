def leiaint(msg):
    resposta = str(input(msg))
    while resposta.isnumeric() == False:
        print('ERROR.Isso não é um número.')
        resposta = str(input(msg))
    return resposta



n = leiaint('Digite um número inteiro: ')
print(f'Voce acabou de digitar o número {n}.')