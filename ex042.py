
r1 = int(input('Digite a 1° reta: '))
r2 = int(input('Digite a 2° reta: '))
r3 = int(input('Digite a 3° reta: '))

if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
    print('Não forma um triângulo.')
    a = False
else:
    print('Forma um triângulo')
    a = True

if r1 == r2 == r3 and a == True :
    print('Esse triângulo é equilátero.')
elif r1 != r2 != r3 and a == True:
    print('Esse triângulo é escaleno.')
elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1 and a == True:
    print('Esse triângulo é isóseles.')