# Faça um programa que leia a distancia em km de uma viagem. Calcule o preço da passagem
# cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

d = int(input('Qual a distancia da viagem? '))           # Distancia da viagem
if d <= 200:                                             # se for menor ou igual a 200, a km custará R$0,50
    preço = d*0.5
    print('Sua viagem custará R${}'.format(preço))
else:                                                    # distancias maiores que 200km, custará R$0,45
    preço_2 = d*0.45
    print('Sua viagem custará R${}'.format(preço_2))

