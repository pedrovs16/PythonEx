from random import randint
from time import sleep
from operator import itemgetter

jogador = {'jogador1':randint(1,6),
            'jogador2':randint(1,6),
            'jogador3':randint(1,6),
            'jogador4':randint(1,6),
           }
for j,n in jogador.items():
    print(f'O {j} tirou o número {n}.')
    sleep(1)
rank = []
rank = sorted(jogador.items(), key=itemgetter(1), reverse=True)
print('A colocação ficou:')
for j in range(0,4):
    print(f'{j + 1}° {rank[j][0]} ')
