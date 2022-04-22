# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem
# dizendo que ele foi multado. A multa vai custar R$7,00 a cada km acima do limite.

v = float(input('Qual a velocidade do carro (em km/h)? '))
if v > 80:
    multa = (v - 80) * 7
    print('Voce foi multado, e a multa é de R${:.2f}.'.format(multa))
else:
    print('Esta dentro do limite de velocidade.')

