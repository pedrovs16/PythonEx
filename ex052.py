n = int(input('Digite um número: '))
s = 0
for c in range(1, n+1):
    if n % c == 0:
        s = s + 1
    else:
        s = s + 0
if s == 2:
    print('Esse número é primo')
elif s != 2:
    print('Esse número não é primo')