n = int(input('Digite o valor a ser convertido: '))
e = int(input('''                 [1] BINÁRIO
                 [2] OCTAL
                 [3]HEXADECIMAL
            Escolha o estilo da conversão: '''))
if (e == 1):
    a = bin(n)
elif (e == 2):
    a = oct(n)
elif (e == 3):
    a = hex(n)
print('O valor da sua opção é {}.'.format(a))

