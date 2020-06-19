n = str
p = 0
perg = str
t = 0
mb = 100000
nb = str
a = 0
while True:
    n = input('Digite o nome do produto: ')
    p = int(input('Qual o preço do produto: '))
    perg = input('Quer continuar[S/N]').upper().strip()
    t += p
    if p > 1000 :
        a += 1
    if mb >> p:
        mb = p
        nb = n
    if perg == 'N':
        break
print(f'O total gasto é {t} reais.')
print(f'{a} produtos custam mais de 1000 reais.')
print(f'O nome do mais barato é {nb}.')
