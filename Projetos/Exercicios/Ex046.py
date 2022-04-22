# Faça um programa q faça uma contagem regressiva indo de 10 até 0, com pausa de 1seg entre eles...

from time import sleep
for c in range(10,0,-1):
    print(c)
    sleep(1)
print('{:=^50}'.format('  FELIZ ANO NOVOOO!!!  '))