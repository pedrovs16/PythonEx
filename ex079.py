lista = []
a = int
resposta = str
while resposta != 'N' and resposta != 'n':
    a = (int(input('Digite um valor: ')))
    if a in lista:
        print('Numero duplicado, não foi adicionado')
    else:
        lista.append(a)
        print('Número adicionado')
    resposta = input('Quer continuar? [S/N]')
print(lista.sort())