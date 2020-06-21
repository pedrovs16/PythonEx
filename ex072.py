escolha = 0
contagem = ('um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desseseis', 'dessesete', 'dezoito', 'dezenove', 'vinte')
while escolha > 20 or escolha < 1:
    escolha = int(input('Digite um número de 1 até 20:'))
print(f'{escolha} por extenso é {contagem[escolha - 1]}')

