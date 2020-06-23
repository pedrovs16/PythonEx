matriz = [[0,0,0],[0,0,0],[0,0,0]]
valor = int
par = 0
coluna2 = 0
valormax= 0
for l in range(0,3):
    for c in range(0,3):
        valor = int(input(f'Digite um valor para posição [{l + 1},{c + 1}] da matriz: '))
        matriz[l][c] = valor
        if valor % 2 == 0:
            par += valor
        if c == 1:
            coluna2 += valor
        if l == 1 and valor > valormax:
            valormax = valor
print(matriz[0])
print(matriz[1])
print(matriz[2])
print(f'A soma dos números pares é {par}.')
print(f'A soma dos números da 2° coluna é {coluna2}. ')
print(f'O maior valor da 2° linha é {valormax}')
