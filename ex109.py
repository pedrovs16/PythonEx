from ex111 import moeda

valor = int(input('Digite um valor: '))
print(f'O dobro do valor {moeda.moeda(valor)} é {moeda.dobrar(valor, True)}.')
print(f'A metade do valor {moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print(f'O seu valor com um acréscimo de 10% é {moeda.aumentar(valor, 10, True)}')
print(f'O seu valor com um descrescimo de 20% é {moeda.aumentar(valor, 20, True)}')