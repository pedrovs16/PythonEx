p = float(input('Digite o valor da compra: '))
f = float(input('''Forma de pagamento
1 --- Dinheiro/cheque
2 --- Crédito.
3 --- 2x no cartão.
4 --- 3x ou mais no cartão.
    Escolha:'''))
if f == 1:
    a = p * 0.9
elif f == 2:
    a = p * 0.95
elif f == 3:
    a = p
elif f == 4:
    a = p * 1.2

print('O valor com acréscimo é de {} reais.'.format(a))
