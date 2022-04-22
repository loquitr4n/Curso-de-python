#Exercício Python 067: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    print(f"{'  TABUADAS  ':=^40}")
    num = int(input('Digite o numero qual deseja saber a tabuada: '))
    if num < 0:
        break
    for n in range(1,11):
        result = num * n
        print(f'{n} x {num} = {result}')
print(f'{" Programa de tabuadas encerrado! ":=^51}')