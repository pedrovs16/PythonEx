primerioTermo = int(input('Digite o 1° termo da PA: '))
razao = int(input('Digite a razão: '))
const = 0
valor = 0
pergunta = int
y = 0
valor2= 0
final = 0
while const != 10:
    const += 1
    valor = primerioTermo + ((const - 1) * razao)
    print('A{} = {}'.format(const, valor))
while pergunta != 0:
    pergunta = int(input('Você quer mais quantos termos: '))
    final += pergunta
    if pergunta != 0:
        while y != final  :
            y += 1
            valor2 = primerioTermo + ((const + y - 1) * razao)
            print('A{} = {}'.format(const + y, valor2))