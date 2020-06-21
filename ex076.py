lista = ('TV', 1000, 'Chapa', 300, 'Batedeira', 200)
for c in range(0, len(lista), 2):
    valor = lista[c + 1]
    print(f'PRODUTO: {lista[c]} //////// VALOR: {valor }')