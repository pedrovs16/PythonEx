resposta = ''
escolha = ''
while resposta != 'FIM':
    escolha = input('Digite uma função ou biblioteca: ')
    resposta = escolha.upper()
    if resposta != 'FIM':
        help(escolha)
