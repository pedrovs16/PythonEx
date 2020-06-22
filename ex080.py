lista = []
x = int

for c in range(1,6):
    x = input('Digite um valor:')
    if x in lista:
        while x in lista:
            x = input('Valor repetido esse número não contou. Tente novamente: ')
        if c == 1:
            lista.append(x)
        if c == 2:
            if x > lista[-1]:
                lista.insert(-1, x)
        elif c == 3:
            if x > lista[-2]:
                lista.insert(-2, x)
            elif x > lista[-1]:
                lista.insert(-1, x)
        elif c == 4:
            if x > lista[-3]:
                lista.insert(-3, x)
            elif x > lista[-2]:
                lista.insert(-2, x)
            elif x > lista[-1]:
                lista.insert(-1, x)
        elif c == 5:
            if x > lista[-4]:
                lista.insert(-4, x)
            elif x > lista[-3]:
                lista.insert(-3, x)
            elif x > lista[-2]:
                lista.insert(-2, x)
            elif x > lista[-1]:
                lista.insert(-1, x)
    else:
        if c == 1:
            lista.append(x)
        if c == 2:
            if x > lista[-1]:
                lista.insert(-1, x)
        elif c == 3:
            if x > lista[-2]:
                lista.insert(-2, x)
            elif x > lista[-1]:
                lista.insert(-1, x)
        elif c == 4:
            if x > lista[-3]:
                lista.insert(-3, x)
            elif x > lista[-2]:
                lista.insert(-2, x)
            elif x > lista[-1]:
                lista.insert(-1, x)
        elif c == 5:
            if x > lista[-4]:
                lista.insert(-4, x)
            elif x > lista[-3]:
                lista.insert(-3, x)
            elif x > lista[-2]:
                lista.insert(-2, x)
            elif x > lista[-1]:
                lista.insert(-1, x)
    print(lista)

print(lista)
