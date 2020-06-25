from time import sleep
def funcaoMaior(*num):
    sleep(1)
    print('=-' * 30)
    print('Analizando os valores...')
    c = 0
    maior = 0
    while c < len(num):
        print(num[c], end=' ')

        if num[c] > maior:
            maior = num[c]
        c += 1
    print(f'Foram escolhidos {len(num)} números. ')
    print(f'O maior valor é {maior}.')
    print('=-' * 30)


funcaoMaior(1 ,2 ,7, 3, 4)
funcaoMaior(5,4,2,1,5,6)
funcaoMaior(3,4,7)