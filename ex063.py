n = int(input('Digite quantos numeros tu quer ver na sequência de Fibonacci: '))
i = 1
c = 0
x = 1
a = 0
print('0-1-', end='')
while c != n - 2:
    a = x
    x = i
    if c == n - 3:
        print('{}'.format(x), end='')
    else:
        print('{}-'.format(x), end='')
    i += a
    c += 1