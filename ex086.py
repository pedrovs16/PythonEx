matriz = [[0,0,0],[0,0,0],[0,0,0]]
valor = int
for l in range(0,3):
    for c in range(0,3):
        valor = int(input(f'Digite um valor para posição [{l},{c}] da matriz: '))
        matriz[l][c] = valor
print(matriz[0])
print(matriz[1])
print(matriz[2])
