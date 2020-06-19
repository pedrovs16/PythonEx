from math import factorial
v1 = int(input('Digite um valor: '))
c = v1
while v1 != 0:
    print('{}'.format(v1), end='')
    if v1 > 1:
        print(' X ', end='')
    else:
        print(' = ', end='')
    if v1 == 1:
        print(factorial(c))
    v1 -= 1
