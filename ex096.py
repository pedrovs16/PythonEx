def funcaoArea(a,b):
    area = a * b
    print(f'A area do terreno {a}x{b} é {area}²')


print(' CALCULADORA DE TERRENO')
print('-' * 30)
largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))
funcaoArea(largura, altura)