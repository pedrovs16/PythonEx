v1 = int(input('Digite o 1° valor: '))
v2 = int(input('Digite o 2° valor: '))
c = int
r = int
while c != 0:
    c = int(input('''Menu
    [1] Somar
    [2] Subtrair
    [3] Dividir
    [4] Multiplicar
    [0] Sair do programa
    Escolha: '''))
    if c == 1:
        r = v1 + v2
    elif c == 2:
        r = v1 - v2
    elif c == 3:
        r = v1 / v2
    elif c == 4:
        r = v1 * v2
    if c != 0:
        print('O resultado é {}.'.format(r))
print('Programa fechado')
