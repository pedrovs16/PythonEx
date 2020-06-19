i = c1 = c2 = c3 = 0
s = str
p = str
while True:
    i = int(input('Digite a idade: '))
    s = input('Digite o sexo [M/F]: ').upper().strip()
    p = input('Quer continuar[S/N]? ').upper().strip()
    if i > 18:
        c1 += 1
    if s == 'M':
        c2 += 1
    if s == 'F' and i < 20:
        c3 += 1
    if p == 'N':
        break
print(f'{c1} pessoas tem mais de 18 anos.')
print(f'{c2} são homens.')
print(f'{c3} são mulheres com menos de 20 anos.')
