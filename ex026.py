f=str(input('Digite uma frase: ')).strip().upper()
print('Tem {} A na frase.'.format(f.count('A')))
print('O primeiro A esta em {} letra.'.format(f.find('A')+1))
print('O ultimo A esta em {} letra.'.format(f.rfind('A')+1))
