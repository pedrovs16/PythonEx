a = float(input('Digite sua altura em cm: '))
m = float(input('Digite sua massa corporal em kg: '))

imc = 10000 * (m / (a * a))
print('Seu imc é {:.1f}.'.format(imc))

if imc < 18.5:
    print('Abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal.')
elif imc >= 25 and imc < 30:
    print('Acima do peso.')
elif imc >= 30 and imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade mórbita')