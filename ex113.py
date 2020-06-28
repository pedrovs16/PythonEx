def leiaint(msg):
    while True:
        try:
            resposta = int(input(msg))
        except (ValueError, TypeError):
            print('Teve um problema na digitação do número, digite um número inteiro')
        else:
            break
    return resposta
def leiafloat(msg):
    while True:
        try:
            resposta = float(input(msg))
        except (ValueError, TypeError):
            print('Teve um problema na digitação do número, digite um número')
        else:
            break
    return resposta



n = leiaint('Digite um número inteiro: ')
print(f'Voce acabou de digitar o número {n}.')
n1 = leiafloat('Digite um número qualquer: ')
print(f'Voce acabou de digitar o número {n1}.')