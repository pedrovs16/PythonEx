lista = [[],[]]
valor = int
for c in range(0,7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Os númers pares são {lista[0]}.')
print(f'Os númers ímpares são {lista[1]}.')