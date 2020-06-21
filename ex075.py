v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))
v4 = int(input('Digite o quarto valor: '))
v5 = int(input('Digite o quinto valor: '))
lista = (v1, v2, v3, v4, v5)
print(f'O 9 apareceu {lista.count(9)} vezes.')
if lista.count(3) > 0:
    print(f'O primeiro 3 esta na {lista.index(3) + 1} posição.')
else:
    print('Não tem nenhum 3')
print('Os números pares são: ', end='')
for n in lista:
    if n % 2 == 0:
        print(n, end=' ')
