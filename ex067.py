n = 0
m = 0
c = 0
while True:
    c = 0
    n = int(input('Digite um número para ver a taboada (digite um número negativo para parar): '))
    if n < 0:
        break
    while c != 10:
        c += 1
        m = n * c
        print(f'{n} X {c} = {m}')