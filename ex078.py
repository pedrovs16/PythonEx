lista = []
for c in range(0,5):
    lista.append(int(input('Digite um valor:')))

print(f'O maior valor da lista é {max(lista)} que se encontra na {(lista.index(max(lista))) + 1} e o menor é {min(lista)} que se encontra na posição {lista.index(min(lista)) + 1}°')
print(lista.index(max(lista)))

