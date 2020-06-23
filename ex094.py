nome = []
sexo = []
idade = []
dicionario = {'nome': nome, 'sexo': sexo, 'idade': idade}
resposta = str
resposta2 = str
x = 0
while resposta != 'n' and resposta != 'N':
    nome.append(input('Digite o nome:'))
    while True:
        resposta2 = (input('Digite o sexo [M/F]'))
        if resposta2 != 'm' and resposta2 != 'M' and resposta2 != 'f' and resposta2 != 'F':
            print('ERROR. digite M ou F.')
        else:
            break
    sexo.append(resposta2)
    idade.append(int(input('Digite a idade: ')))
    while True:
        resposta = input('Voce quer continuar? [S/N]')
        if resposta != 'S' and resposta != 's' and resposta != 'N' and resposta != 'n':
            print('ERROR. digite S ou N.')
        else:
            break
print(f'A) Temos {len(dicionario["nome"])} cadastradas')
for p in range(0,len(dicionario['idade'])):
    x += dicionario['idade'][p]
media = x/len(dicionario['idade'])
print(f'B) A média das idades é {media:5.2f}')

print(f'C)As mulheres cadastradas são:')
for p in range(0,len(dicionario['sexo'])):
    if len(dicionario['sexo'][p]) == 'F' or 'f':
        print(dicionario['nome'][p])

print(f'D)As pessoas acima da média são:')
for p in range(0,len(dicionario['idade'])):
    if dicionario['idade'][p] > media:
        print(f'{dicionario["nome"][p]} --- {dicionario["idade"][p]}')
