from random import randint
from time import sleep
lista = list()
jogos = list()
cont = 0
quant = int(input('Qts jogos você quer que eu sorteie ?'))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(1)

