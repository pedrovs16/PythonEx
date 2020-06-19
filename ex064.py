c = s = n = 0
while n != 999:
    n = int(input('Digite um valor [999 para parar]: '))
    s += n
    c += 1
print('Foram digitados {} números e a soma deles é {}.'.format(c -1, s - 999))