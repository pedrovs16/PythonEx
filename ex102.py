from math import factorial


def fatorial(numero, show=0):
    valor = factorial(numero)
    a = b = str
    resposta = str

    def true():
        for c in range(-numero, 0):
            if c == -1:
                print(f'{-c}', end='')
            else:
                print(f'{-c}X', end='')
        print( f' é igual a {valor}')


    def false():
        print(f'O fatorial de {numero} é igual a {valor}')

    if show == True:
        return true()
    else:
        return false()


print(fatorial(4, show=True))
