pessoas = []
pessoa = []
resposta = str
pesomin = 1000
pessoamin = []
pesomax = 0
pessoamax = []
count = 0
peso = int
nome = str
while resposta != 'n' and resposta != 'N':
    nome = (input('Digite o nome da pessoa: '))
    peso = (int(input('Digite a peso da pessoa: ')))
    pessoa.append(nome)
    pessoa.append(peso)
    if count == 0:
        pessoamin.append(nome)
        pesomin = peso
    count += 1
    if peso > pesomax:
        pesomax = peso
        pessoamax.clear()
        pessoamax.append(nome)
    elif peso == pesomax:
        pessoamax.append(nome)


    if peso < pesomin:
        pesomin = peso
        pessoamin.clear()
        pessoamin.append(nome)
    elif peso == pesomin:
        pessoamin.append(nome)

    pessoas.append(pessoa[:])
    pessoa.clear()
    resposta = input('Deseja continuar [S/N] ? ')


print(f'Foram cadastrada {count} pessoas.')
print(f'O maior peso foi {pesomax}, quem tinha esse pesso era {pessoamax}')
print(f'O menor peso foi {pesomin}, quem tinha esse pesso era {pessoamin}')