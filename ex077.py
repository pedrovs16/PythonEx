a = e = i = o = u = ""
lista = ('pao', 'bacon', 'cenoura', 'mel', 'uva')
for c in range(0, len(lista)):
    palavra = lista[c]
    if palavra.count('a') > 0:
        a = "a"
    if palavra.count('e') > 0:
        e = "e"
    if palavra.count('i') > 0:
        i = "i"
    if palavra.count('o') > 0:
        o = "o"
    if palavra.count('u') > 0:
        u = "u"
    print(f'Na palavra {palavra} tem as seguintes vogais: {a} {e} {i} {o} {u}')
    a = e = i = o = u = ""
