def aumentar(valor, porcentagem, condição):
    resultado = valor * ((100 + porcentagem) / 100)
    resultadoPronto = str
    if condição is True:
        resultadoPronto = f'R${resultado}'
    else:
        resultadoPronto = resultado
    return resultadoPronto

def diminuir(valor, porcentagem, condição):
    resultado = valor * ((100 - porcentagem) / 100)
    resultadoPronto = str
    if condição is True:
        resultadoPronto = f'R${resultado}'
    else:
        resultadoPronto = resultado
    return resultadoPronto
def dobrar(valor, condição):
    resultado = valor * 2
    resultadoPronto = str
    if condição is True:
        resultadoPronto = f'R${resultado}'
    else:
        resultadoPronto = resultado
    return resultadoPronto
def metade(valor, condição):
    resultado = valor / 2
    resultadoPronto = str
    if condição is True:
        resultadoPronto = f'R${resultado}'
    else:
        resultadoPronto = resultado
    return resultadoPronto
def moeda(valor):
    resultadoPronto = f'R${valor}'
    return resultadoPronto
def resumo(valor):
    print('-=' * 30)
    print('                   Resumo')
    print('-=' * 30)
    print(f'O dobro do valor {moeda(valor)} é {dobrar(valor, True)}.')
    print(f'A metade do valor {moeda(valor)} é {metade(valor, True)}')
    print(f'O seu valor com um acréscimo de 10% é {aumentar(valor, 10, True)}')
    print(f'O seu valor com um descrescimo de 20% é {aumentar(valor, 20, True)}')
