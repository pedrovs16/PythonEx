from random import randint
def sorteia():
    for a, c in enumerate(lista):
        print(c, end=' ',)
    print('foram sorteados')
def pares():
    soma = 0
    for a, c in enumerate(lista):
        if c % 2 == 0:
            soma += c
    print(f'A soma dos números pares na lista {lista} é {soma}')


lista = [randint(0,10), randint(0,10), randint(0,10), randint(0,10) ,randint(0,10)]
sorteia()
pares()