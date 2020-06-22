expressao = input('Digite a expressao: ')
if expressao.count('(') == expressao.count(')'):
    print('Essa expressão é válida.')
else:
    print('Essa expressão é inválida')