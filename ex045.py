import random
j = int(input('''JOKENPO
1 --- Pedra
2 --- Papel
3 --- Tesoura
Digite a sua escolha: '''))
a = random.randint(1,3)
if a == 1:
    c = 'pedra'
elif a == 2:
    c = 'papel'
elif a == 3:
    c = 'tesoura'
if j == 1 and a == 3 or j == 2 and a == 1 or j == 3 and a == 2:
    print('Você venceu, o computador escolheu {}.'.format(c))
elif a == j:
    print('Empatou, você e o computador escolheram {}.'.format(c))
elif j == 1 and a == 2 or j == 2 and a == 3 or j == 3 and a == 1:
    print('Você perdeu, o computador escolheu {}.'.format(c))