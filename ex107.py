from ex111 import moeda

valor = int(input('Digite um valor: '))
print(f'O dobro do seu valor é {moeda.dobrar(valor)}.')
print(f'A metade do seu valor é {moeda.metade(valor)}')
print(f'O seu valor com um acréscimo de 10% é {moeda.aumentar(valor, 10)}')
print(f'O seu valor com um descrescimo de 20% é {moeda.aumentar(valor, 20)}')