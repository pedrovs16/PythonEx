lista = []
impares = []
pares = []
resposta = str
valor = int
while resposta != 'n' and resposta != 'N':
    valor = int(input('Digite um valor: '))
    if lista.count(valor) != 0:
        print('Esse valor ja foi digitado tente outro')
    else:
        lista.append(valor)
        if valor % 2 == 0:
            pares.append(valor)
        else:
            impares.append(valor)
    resposta = input('Deseja continuar [S/N] ?')
print(f'Os números digitados foram {lista}.')
print(f'Os números ímpares foram {impares}.')
print(f'Os números pares foram {pares}.')
