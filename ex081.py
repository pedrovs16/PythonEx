lista = []
continuar = str
contagem = 0
valor = int
while continuar != 'N' and continuar != 'n':
    valor = (int(input('Digite um valor: ')))
    if lista.count(valor) == 0:
        lista.append(valor)
        contagem += 1
    else:
        print('Esse valor ja tem tente novamente.')
    continuar = input('Deseja continuar [S/N]? ')
lista.sort(reverse=True)
if lista.count(5) > 0:
    print('O número 5 faz parte da tua lista')
else:
    print('O número 5 não faz parte da tua lista')
print(lista)
print(f'Você digitou {contagem} valores.')