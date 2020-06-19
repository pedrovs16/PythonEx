v=int(input('Digite a velocidade do seu carro: '))
m= (v-80) * 7
if (v > 80):
    print('Você esta acima da velocidade de 70km/h, recebesse uma multa de {} reais'.format(m))
else:
    print('Você está abaixo do limite, continue assim:')