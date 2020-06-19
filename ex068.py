from random import randint
j = 0
comp = 0
e = str
c = 0
while True:
    comp = randint(1,10)
    j = int(input('Digite um valor: '))
    e = input('Par ou Impár [P/I]: ').upper().strip()
    print(f'O computador jogou {comp}.')
    if e == 'P' and (c+j) % 2 == 0 or e == 'I' and (c+j) % 2 != 0:
        print('Você venceu')
        c += 1
    elif e == 'P' and (c+j) % 2 != 0 or e == 'I' and (c+j) % 2 == 0:
        print(('Você perdeu'))
        break
print(f'Você venceu {c} partidas seguidas')

