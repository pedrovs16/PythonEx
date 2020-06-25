def contator(inicio, fim, passo):
    print('-+' * 30)
    print(f'Contando números entre {inicio} e {fim} pulando em {passo} em {passo}:')
    if fim > inicio and passo != 0:
        for c in range (inicio, fim + 1, passo):
            print(c, end=' ')
        print('*FIM*',)
        print('-+' * 30)
    elif inicio > fim and passo != 0:
        for c in range (-inicio, fim + 1, passo):
            print(-c, end=' ')
        print('*FIM*',)
        print('-+' * 30)
    elif inicio > fim and passo == 0:
        for c in range (-inicio, fim + 1, 1):
            print(-c, end=' ')
        print('*FIM*',)
        print('-+' * 30)
    elif fim > inicio and passo == 0:
        for c in range (inicio, fim + 1, 1):
            print(c, end=' ')
        print('*FIM*',)
        print('-+' * 30)



contator(1,10,1)
contator(10,0,2)
print('Agora é sua vez')
v1 = int(input("Inicio: "))
v2 = int(input("Fim: "))
v3 = int(input("Passo: "))
contator(v1, v2, v3)
