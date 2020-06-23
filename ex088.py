from random import randint
from time import sleep
lista =[randint(0,60), randint(0,60), randint(0,60), randint(0,60), randint(0,60), randint(0,60), ]
vezes = int(input('Digite quantos jogos queres sortear: '))
for c in range (0,vezes):
    lista = [randint(0,60), randint(0,60), randint(0,60), randint(0,60), randint(0,60), randint(0,60), ]
    print(lista)
    sleep(2)