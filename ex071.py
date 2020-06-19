import math
c1 = c2 = c3 = c4 = c5 = int
q = c1 = c2 = c3 = c4 = c5 = d1 = d2 = d3 = d4 = d5 = 0
while True:
    q = int(input('Digite quantos reais tu quer sacar: '))
    c1 = q / 50
    d1 = q % 50
    c2 = d1 / 20
    d2 = d1 % 20
    c3 = d2 / 10
    d3 = d2 % 10
    c4 = d3 / 5
    d4 = d3 % 5
    c5 = d4 / 1
    d5 = d4 % 1
    break
e1 = math.floor(c1)
e2 = math.floor(c2)
e3 = math.floor(c3)
e4 = math.floor(c4)
e5 = math.floor(c5)
print(f'''{e1} cédulas de 50
{e2} cédulas de 20
{e3} cédulas de 10
{e4} cédulas de 5
{e5} cédulas de 1''')