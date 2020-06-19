f = str(input('Digite uma frase: ')).strip().upper()
lf = f.split()
jf = ''.join(lf)
inverso = ''
for c in range(len(jf) - 1, -1, -1):
    inverso += jf[c]
if inverso == jf:
    print('O inverso é igual')
else:
    print('O inverso é diferente')













